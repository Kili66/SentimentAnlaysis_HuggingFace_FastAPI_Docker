from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

sentiment_pipe= pipeline("sentiment-analysis")

app= FastAPI()

data= ["I dont love you", "I dont hate you"]

print(sentiment_pipe(data))

class requestModel(BaseModel):
    input_string: str
    
@app.post("/analyze")

def your_funtion(request: requestModel):
    input_string= request.input_string
    sentiment= sentiment_pipe(input_string)
    return {"result":
        {
            "sentiment_category": sentiment[0]["label"],
            "score_for_sentiment": sentiment[0]["score"]
        }
        }

