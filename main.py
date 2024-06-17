# 1. Library imports
import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import joblib

with open('prediction_pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)
# pipe = joblib.load('prediction_pipe2.pkl')

class HouseData(BaseModel):
    ask_desc: str
    ask_loc:str
    ask_bed: int
    ask_bath: int
    ask_floor: float
    ask_lat: float
    ask_long: float

# 2. Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials="true",
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_price(item:HouseData):
    df = pd.DataFrame([item.model_dump().values()], columns=['Description', 'Location', 'Bedrooms', 'Bath', 'Area', 'Latitude', 'Longitude'])
    prediction = pipe.predict(df)
    return {"Price Prediction: ": float(prediction)}

# Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)

uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload
