# Movie Rating Predictor API with BentoML

This project demonstrates how to deploy a machine learning model as a REST API using **BentoML**.  
Built as part of the **CS 594: Responsible AI Engineering (Spring 2025)** course, the system predicts how a user might rate a movie based on their viewing data — simulating a real-world use case like Netflix or Prime Video.

---

## Requirements

- Python 3.8+
- pandas  
- scikit-learn  
- bentoml  

### Install them using:
    pip install -r requirements.txt

---

## How to Run

### 1. Clone the Repository
    git clone https://github.com/YOUR_USERNAME/bentoml-movie-recommender.git
    cd bentoml-movie-recommender 
   
### 2. Serve the Model
    bentoml serve movie_service:svc

### 3. Test the API
  Send a POST request to:
    http://localhost:3000/predict

    With this JSON body:

    {
      "userId": 1,
      "movieId": 10,
      "timestamp": 964982703
    }

You’ll get a predicted rating in the response.
