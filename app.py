import requests
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database import get_db
from database.models import User
from utils import create_user_from_json

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, name="home")
async def get_users(request: Request, session: Session = Depends(get_db)):
    users = User.get_all(session)
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


@app.post("/", response_class=HTMLResponse)
async def fetch_user(request: Request, session: Session = Depends(get_db)):
    response = requests.get("https://randomuser.me/api/")
    json_data = response.json()

    user = create_user_from_json(json_data)
    user.save(session)
    return RedirectResponse(app.url_path_for("home"), status_code=302)


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def user_details(request: Request, user_id: int, session: Session = Depends(get_db)):
    user = User.get_by_id(session, user_id)
    return templates.TemplateResponse("user_details.html", {"request": request, "user": user})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
