# https://www.youtube.com/watch?v=N6bpBkwFdc8
from fastapi import FastAPI, UploadFile, File
from app.model.model import query
import shutil

app = FastAPI()


@app.get("/")
def home():
    return {"statusText": "OK"}


@app.post("/predict")
async def predict(in_file: UploadFile = File(...)):
    with open(f"{in_file.filename}", "wb") as out_file:
        shutil.copyfileobj(in_file.file, out_file)

    result = query(in_file.filename)
    prediction = result[0]["label"]
    return {"ImageNet Class": prediction}
