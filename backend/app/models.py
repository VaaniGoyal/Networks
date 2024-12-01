from pydantic import BaseModel, Field
from bson import ObjectId

class User(BaseModel):
    username: str
    password: str

class File(BaseModel):
    filename: str
    category: str
    uploader: str
