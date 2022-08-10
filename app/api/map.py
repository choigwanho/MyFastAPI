from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates/")

router = APIRouter()

class Spot(BaseModel):
    lat: str
    lng: str

@router.get("/main", response_class=HTMLResponse)
async def get_map(request: Request):
    return templates.TemplateResponse("map_main.html",{"request": request})

@router.post("/search", response_class=HTMLResponse)
async def get_map(spot: Spot):
    dicted_spot = dict(spot)
    dicted_spot['success'] = True

    return JSONResponse(dicted_spot)