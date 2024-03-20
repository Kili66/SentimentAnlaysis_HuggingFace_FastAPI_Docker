# Use an official python runtime as a parent image
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the current directory content to the container

COPY . /app
# install all necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available outside to the world of container
EXPOSE 8000

# run app.py when the container lunched

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]