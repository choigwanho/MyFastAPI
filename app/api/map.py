from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")

router = APIRouter()

@router.get("/main", response_class=HTMLResponse)
async def get_map(request: Request):
    return templates.TemplateResponse("map_main.html",{"request": request})