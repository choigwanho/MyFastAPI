from fastapi import APIRouter
from app.db.db_connection import engineconn
from app.db.db_class import Test

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

@router.get("/get", tags=["get"])
async def first_get():
    example = session.query(Test).all()
    return example