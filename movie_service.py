from bentoml import Service
import bentoml
from bentoml.io import JSON
import pandas as pd

# ✅ Correct way to load model and create a runner
model_ref = bentoml.sklearn.get("movie_rating_model:latest")
model_runner = model_ref.to_runner()

# Create the BentoML service
svc = Service("movie_rating_service", runners=[model_runner])

# Define a REST API for prediction
@svc.api(input=JSON(), output=JSON())
def predict(input_data):
    df = pd.DataFrame([input_data])
    prediction = model_runner.run(df)[0]
    return {"predicted_rating": round(float(prediction), 2)}
