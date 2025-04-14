# Movie Rating Predictor API with BentoML

This project demonstrates how to deploy a machine learning model as a REST API using **BentoML**.  
Built as part of the **CS 594: Responsible AI Engineering (Spring 2025)** course, the system predicts how a user might rate a movie based on their viewing data — simulating a real-world use case like Netflix or Prime Video.

---

## Features

- Trains a `RandomForestRegressor` on the MovieLens dataset
- Saves and versions the model with BentoML
- Serves predictions via a REST API
- Fully local and beginner-friendly deployment — no Docker or cloud required

---

## Requirements

- Python 3.8+
- pandas  
- scikit-learn  
- bentoml  

### Install them using:

```bash
pip install -r requirements.txt

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/bentoml-movie-recommender.git
cd bentoml-movie-recommender

### 2. Serve the Model
Run this command in the terminal:
```bash
bentoml serve movie_service:svc

### 3. Test the API
Send a POST request to:
```bash
http://localhost:3000/predict

With this JSON body:

```json
{
  "userId": 1,
  "movieId": 10,
  "timestamp": 964982703
}

You’ll get a predicted rating in the response.
