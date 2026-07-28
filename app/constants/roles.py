from enum import Enum

# describe rols
class Role(str, Enum):
  USER = "user"
  ADMIN = "admin"
  SELLER="seller"
