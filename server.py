from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime


app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/start.html")

# Раздаём только JS-файл вручную (без StaticFiles)
@app.get("/ingame.js")
def ingame_js():
    return FileResponse("public/ingame.js")

@app.post("/start_game")
def start_game(duration):
    global start_time
    start_time = datetime.now()
    return {"message": "Game started", "duration": duration}

@app.get("/get_timer")
def get_timer(duration):
    return duration - (datetime.now() - start_time)