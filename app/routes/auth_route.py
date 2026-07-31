# built in module imports
from fastapi import APIRouter, status



# custom module imports
from app.schemas.user_schema import UserResponse, UserCreate, UserLogin
from app.services.auth_service import auth_service



# create instance
router = APIRouter(prefix="/auth", tags=["Authentication"])

# POST: sign up route
@router.post("/signup" , response_model=UserResponse , status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate):
  return await auth_service.signup(user_data)


# post: login route
@router.post("login")
async def login(user_data: UserLogin):
  return await auth_service.login(user_data)


# post: verify OTP 
@router.post("verify_otp")
async def verify_otp(user_id: str, otp: str):
  return await auth_service.verify_signup_otp(user_id , otp)