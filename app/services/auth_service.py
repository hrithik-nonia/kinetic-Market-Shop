# built in module imports



# custom module imports 
from app.repositories.user_repository import user_repository
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin
from app.custom_exception.custom_exceptions import UserAlreadyExistsException, InvalidCredentialsException, UserNotVerifiedException
from app.security.password_handler import hash_password
from app.models.user_model import UserModel
from app.security.password_handler import verify_password
from app.security.jwt_handler import create_access_token , create_refresh_token
from app.services.otp_service import otp_service

class AuthService:
  # create constructor
  def __init__(self):
    self.user_repository = user_repository


  # sign up method
  async def signup(self, user_data : UserCreate)-> UserResponse:
    # 1 . find from DB
    existing_user = await user_repository.find_by_email(user_data.email)

    # 2 . check user exist if yes raise error , if not move to the next step 
    if existing_user :
      raise UserAlreadyExistsException(user_data.email)

    # 3 . now hashed the password
    hashed_pw = hash_password(user_data.password)

    # 4 . create a data model which will store in DB
    new_user=UserModel(
      name=user_data.name,
      email=user_data.email,
      hashed_password=hashed_pw
      )

    # 5 . create user in DB
    created_user = await self.user_repository.create(new_user)

    # 6 . extract id
    user_id = str(created_user["_id"])

    # 7. send otp and store session id
    session_id = await otp_service.send_otp(user_data.phone)

    # 8. store session id into data base
    await self.user_repository.update_otp_session(user_id, session_id)

    #  . make a structure response for client
    return UserResponse(
        id=user_id,
        name=created_user["name"],
        email=created_user["email"],
        role=created_user["role"],
        is_active=created_user["is_active"],
        is_verified=created_user["is_verified"],
        created_at=created_user["created_at"],
        )



  # verify otp method
  async def verify_signup_otp(self, user_id: str, otp: str) -> dict:
    user = await self.user_repository.find_by_id(user_id)
    if not user or not user.get("otp_session_id"):
        raise ValueError("No OTP session found, please signup again")

    is_verified = await otp_service.verify_otp(user["otp_session_id"], otp)
    if not is_verified:
        raise ValueError("Invalid or expired OTP")

    await self.user_repository.mark_verified(user_id)
    return {"message": "Phone verified successfully"}



  # login method
  async def login(self, credentials: UserLogin) -> dict:
    # 1. find user
    user = await self.user_repository.find_by_email(credentials.email)
    if not user:
        raise InvalidCredentialsException()

    # 2: Password verify karo
    if not verify_password(credentials.password, user["hashed_password"]):
        raise InvalidCredentialsException()

    # 3. Check karo account active hai ya nahi
    if not user["is_active"]:
        raise InvalidCredentialsException()

    # 3.5 . check account verified hai ya nahi
    if not user["is_verified"]:
       raise UserNotVerifiedException()

    # 4. convert _id into id
    user_id = str(user["_id"])

    # 5. create a token payload 
    token_payload = {"sub": user_id, "role": user["role"]}

    # 6. create access token and refresh token
    access_token = create_access_token(token_payload)
    refresh_token = create_refresh_token(token_payload)

    # 7. save refresh toke into DB
    await self.user_repository.update_refresh_token(user_id, refresh_token)

    # return access token
    return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
          }




auth_service = AuthService()