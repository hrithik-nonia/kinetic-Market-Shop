# built in module imports



# custom module imports 
from app.repositories.user_repository import user_repository
from app.schemas.user_schema import UserCreate, UserResponse
from app.custom_exception.custom_exceptions import UserAlreadyExistsException
from app.security.password_handler import hash_password
from app.models.user_model import UserModel


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

    # 7 . make a structure response for client
    return UserResponse(
        id=user_id,
        name=created_user["name"],
        email=created_user["email"],
        role=created_user["role"],
        is_active=created_user["is_active"],
        is_verified=created_user["is_verified"],
        created_at=created_user["created_at"],
        )


auth_service = AuthService()