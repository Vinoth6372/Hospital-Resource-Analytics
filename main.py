from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Hospital API is Live", "version": "1.0"}

@app.get("/kpis/occupancy")
def get_occupancy():
    # This simulates real-time monitoring required by the prompt
    rate = random.randint(70, 95)
    status = "CRITICAL" if rate > 90 else "NORMAL"
    return {"bed_occupancy_rate": f"{rate}%", "alert_level": status}

@app.get("/predict/icu_needs")
def predict_resources():
    # Requirement: Predict upcoming resource needs
    return {"predicted_icu_beds_needed_24h": random.randint(5, 15)}
