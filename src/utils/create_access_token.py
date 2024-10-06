from datetime import timedelta, datetime

import jwt

from src.utils.EnvironmentVariableResolver import EnvironmentVariableResolver


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=EnvironmentVariableResolver().get_access_token_expire_minutes())
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, EnvironmentVariableResolver().get_secret_key(), algorithm=EnvironmentVariableResolver().get_algorithm())
    return encoded_jwt