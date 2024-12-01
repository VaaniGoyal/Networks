from fastapi import APIRouter, Depends, HTTPException
from backend.app.auth import authenticate_user, create_access_token, get_password_hash
from backend.app.db import db

router = APIRouter()

@router.post("/register")
async def register(username: str, password: str):
    hashed_password = get_password_hash(password)
    await db.client.mydb.users.insert_one({"username": username, "password": hashed_password})
    return {"msg": "User registered"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
