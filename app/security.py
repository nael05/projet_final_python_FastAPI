import os
import secrets
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from app.database import create_user_if_missing, get_user

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "Albums2026!"
SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hasher = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def initialize_default_user() -> None:
	if get_user(DEFAULT_USERNAME) is None:
		password_hash = password_hasher.hash(DEFAULT_PASSWORD)
		create_user_if_missing(DEFAULT_USERNAME, password_hash)


def verify_password(password: str, password_hash: str) -> bool:
	return password_hasher.verify(password, password_hash)


def create_access_token(
	username: str, expires_delta: timedelta | None = None
) -> str:
	expires_at = datetime.now(timezone.utc) + (
		expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	)
	return jwt.encode(
		{"sub": username, "exp": expires_at}, SECRET_KEY, algorithm=ALGORITHM
	)


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
	unauthorized = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Jeton invalide ou expiré",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username = payload.get("sub")
		if username is None:
			raise unauthorized
	except InvalidTokenError:
		raise unauthorized

	user = get_user(username)
	if user is None:
		raise unauthorized
	return user
