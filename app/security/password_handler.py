# built in module imports
from passlib.context import CryptContext


# custom module imports


"""object create kiya parameter 1 algorithm bata raha hai like (argon2/bcrypt) , parameter 2 future me agar algorithm change kiya to Passlib automatically samajh lega Kaunsa algorithm use hua tha. """
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# hash password 
def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


# verify login password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
