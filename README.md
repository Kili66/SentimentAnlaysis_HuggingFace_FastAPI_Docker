# Sentiment Analysis with HuggingFace, FastAPI, and Docker
This project demonstrates how to perform sentiment analysis using HuggingFace's transformers library, FastAPI, and Docker. Sentiment analysis is a natural language processing task that involves determining the sentiment or emotional tone expressed in a piece of text.

### Installation
To run this project locally, you need to have Docker installed on your machine.

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker container:
```
docker build -t sentiment-analysis .
```
4. Run the docker container
```
docker run -d --name sentiment-api -p 8000:8000 sentiment-analysis
```
5. The FastAPI server will be accessible at http://localhost:8000.

### Usage
Once the Docker container is running, you can interact with the FastAPI server to perform sentiment analysis on text input. The API endpoint /analyze accepts POST requests with JSON payload containing the text to analyze.
* Example request using curl:
  
```curl -X 'POST' \
  'http://localhost:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input_string": "I love this project!"
}'

```
Example response:
```{
  "result": {
    "sentiment_category": "POSITIVE",
    "score_for_sentiment": 0.998
  }
}
```
### Endpoint
POST /analyze: Accepts a JSON payload with a single attribute input_string representing the text to analyze. Returns a JSON response containing the sentiment category and corresponding score.
### Dependencies (Requirements)
* transformers: Library for state-of-the-art natural language processing.
* FastAPI: Web framework for building APIs with Python.
* Docker: Platform for developing, shipping, and running applications in containers.
