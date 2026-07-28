# built in module imports
import re


class AuthValidator:

  # check password strength
  def validate_password_strength(self , value: str) -> str:
    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", value):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"\d", value):
        raise ValueError("Password must contain at least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise ValueError("Password must contain at least one special character")
    return value


  # email must be an gmail account
  def email_validator(self, value: str)-> str:
    if not value.lower().endswith("@gmail.com"):
      raise ValueError("Only Gmail addresses are allowed (e.g. example@gmail.com)")
    return value.lower()


  # phone number validater
  def phone_validater(self, value: str) -> str:
        if not re.match(r"^[6-9]\d{9}$", value):  # Indian mobile: 10 digit, starts 6-9
            raise ValueError("Invalid phone number")
        if value == value[0] * 10:  # 9999999999 jaisa repeated digit
            raise ValueError("Invalid phone number")
        return value




auth_validator = AuthValidator()
       