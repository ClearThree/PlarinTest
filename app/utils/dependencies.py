from fastapi import Header, HTTPException

from app.config import APP_SECRET_TOKEN


async def check_secret_token(token: str = Header(...)) -> bool:
    if token != APP_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Secret token is invalid")
    return True
