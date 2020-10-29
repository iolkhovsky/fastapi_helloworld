from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(BaseModel):
    speed: int
    angle: int
    led1: bool
    led2: bool


external_data = {
    'speed': 0,
    'angle': 0,
    'led1': False,
    'led2': True
}
data = Item(**external_data)


@app.get("/")
async def root():
    page = ""
    with open("index.html") as f:
        page = f.read()
    return HTMLResponse(content=page)


@app.post("/control")
async def root(item: Item):
    data = item
    print(data.angle, data.speed, data.led1, data.led2)
    return {"message": "Ok you posted smth"}


@app.get("/telemetry")
async def root():
    response = {"speed": data.speed, "angle": data.angle, "led1": data.led1, "led2": data.led2}
    print("sending telemetry: ", response)
    return JSONResponse(content=response)
