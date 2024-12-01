from fastapi import APIRouter, UploadFile, Depends
from backend.app.db import db

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile, category: str, current_user: str = Depends(oauth2_scheme)):
    file_data = {"filename": file.filename, "category": category, "uploader": current_user}
    await db.client.mydb.files.insert_one(file_data)
    return {"msg": "File uploaded successfully"}

@router.get("/files")
async def get_files(category: str = None):
    query = {"category": category} if category else {}
    files = await db.client.mydb.files.find(query).to_list(100)
    return files

@router.get("/search")
async def search_files(filename: str):
    files = await db.client.mydb.files.find({"filename": {"$regex": filename, "$options": "i"}}).to_list(100)
    return files
