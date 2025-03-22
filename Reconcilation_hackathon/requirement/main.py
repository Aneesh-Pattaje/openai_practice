from fastapi import FastAPI
from pydantic import BaseModel
from aiUtil import generate_output

app = FastAPI()

class Data(BaseModel):
    name: str
    quant: int

class Movie(BaseModel):
    movieName: str

@app.get("/ok")
async def ok_endpoint():
    return {"message":"ok"}

@app.post("/data")
async def data_endpoint(name: str, quant: int):
    return {"message": f"Data : {name} with {quant} quantity received"}

@app.post("/data_obj")
async def data_endpoint(obj : Data):
    return {"message": f"Data : {obj.name} with {obj.quant} quantity received"}

@app.post("/movieCast")
async def movieCast_endpoint(movie : Movie):
    cast = generate_output(f"movieName: {movie.movieName}")
    return {"movieCast": cast}
    