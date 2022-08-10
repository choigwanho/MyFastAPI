from fastapi import APIRouter
from pydantic import BaseModel
from app.db.db_connection import engineconn
from app.db.db_class import Test

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    name : str
    number : int

@router.post("/post", tags=["post"])
async def first_post(item:Item):
    addMemo = Test(name=item.name, number=item.number)
    session.add(addMemo)
    session.commit()
    return item