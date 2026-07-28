# built in module imports
from pydantic import BaseModel, EmailStr, field_validator, Field
from typing import Annotated, Optional
from datetime import datetime




# custom module imports
from app.utils.auth_validator import auth_validator
from app.constants.roles import Role


# create a data validation class
class BaseClass(BaseModel):
  email: EmailStr
  password: str

  # custom validation for email (email must be an gmail account)
  @field_validator("email")
  @classmethod
  def validate_gmail_only(cls, value: str)-> str:
    return auth_validator.email_validator(value)


  # custom validation for password 
  @field_validator("password")
  @classmethod
  def validate_password(cls, value: str)-> str:
    return auth_validator.validate_password_strength(value)



# validation for user create
class UserCreate(BaseClass):
  name:Annotated[str , Field(min_length=1, max_length=100, description="Full Name")]
  phone: Optional[str] = None

  # validate phone number
  @field_validator("phone")
  @classmethod
  def validate_phone(cls, value: str)-> str:
    return auth_validator.phone_validater(value)


# validation for user login
class UserLogin(BaseClass):
  pass
  

# validation class for user response
class UserResponse(BaseModel):
  id: str
  name: str
  email: EmailStr
  role: Role
  is_active: bool
  is_verified: bool
  created_at: datetime

  model_config = {
      "from_attributes": True
  }



# validation refresh token request
class RefreshTokenRequest(BaseModel):
  pass


# verify email for OTP 
class VerifyEmailRequest(BaseModel):
  pass


# validate data for password change request
class ChangePasswordRequest(BaseModel):
  pass