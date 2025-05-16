from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional
from fastapi import HTTPException


JWT_SECRET_KEY = "your-secret"  # Replace with env if preferred
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 60

def create_jwt_token(user_id: int, username: str, role: str):
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    payload = {"sub": username, "id": user_id, "role": role, "exp": expire}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token

def decode_jwt_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

def decode_jwt_token(token: str):
    try:
        print("Decoding token:", token)
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        print("Decoded payload:", decoded_token)
        return decoded_token
    except JWTError as e:
        print("JWT Decode failed:", str(e))
        raise HTTPException(status_code=401, detail="Invalid token")