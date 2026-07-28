# built in module imports
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError


# custom module imports
from app.config.setting import setting


# create access token
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(
        to_encode, setting.JWT_SECRET_KEY, algorithm=setting.JWT_ALGORITHM
    )
    return encoded_jwt



# create refresh token
def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        days=setting.REFRESH_TOKEN_EXPIRE_DAYS
    )
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(
        to_encode, setting.JWT_SECRET_KEY, algorithm=setting.JWT_ALGORITHM
    )
    return encoded_jwt



# decode token
def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token, setting.JWT_SECRET_KEY, algorithms=[setting.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        return None