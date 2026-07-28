# built in module imports
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime, timezone


# custom module imports
from app.constants.roles import Role
from app.utils.py_object_id import PyObjectId


class UserModel(BaseModel):
  """
  Yeh represent karta hai User document MongoDB mein kaise store hota hai.
  """
  id: Optional[PyObjectId] = Field(default=None, alias="_id")
  name: str
  email: EmailStr
  hashed_password: str
  role: Role = Role.USER
  phone: Optional[str] = None
  is_active: bool = True
  is_verified: bool = False
  refresh_token: Optional[str] = None
  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

  is_verified: bool = False
  verification_otp: Optional[str] = None
  otp_expires_at: Optional[datetime] = None

  model_config = {
      "populate_by_name": True,
      "arbitrary_types_allowed": True,
      "json_encoders": {},
  }