# FastAPI

## Stacks
- FastAPI
- HTML, CSS, Javascript
- Docker



### 04 프로젝트 구조 바꾸기
templates 추가
```

```

### 04 화면 띄우기
Jinja2 사용
```
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/main", response_class=HTMLResponse)
async def read_users(request: Request):
    context={}
    context["request"] = request
    return templates.TemplateResponse("map_main.html", context)
```

### 03 배포 쉽게하기
pip freeze 사용
```
pip freeze > requirements.txt
```
가상환경 준비
```
C:\project>python -m venv 가상환경명
C:\project>cd 가상환경명
C:\project\가상환경명>Scripts\activate.bat
(가상환경명) C:\project\가상환경명> # 활성화된 상태
```
가상환경에 셋팅
```
pip install -r requirements.txt
```

### 02 FastAPI APIRouter 사용하여 캡슐화
라우터만들기
```
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def first_get():
    return {"message":"success"}
```
라우터를 main FastAPI에 합치기
```
from fastapi import FastAPI
from app.api import api_get

def start_application():
  app = FastAPI()
  include_router(app.include_router(api_get.router, prefix='/main'))
  return app
  
app = start_application()
```

### 01 FastAPI 프로젝트 시작하기
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}
```

