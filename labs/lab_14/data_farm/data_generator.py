import random
import pandas as pd
import os

# Constants
N_COWS = 50
N_DAYS = 42
LS_FARMS = ["farm_alpha", "farm_beta", "farm_gamma"]
LS_BREEDS = ["Holstein", "Jersey", "Guernsey"]
LS_WEIGHTS = [1200, 1000, 1100]
LS_W = [1.3, 1.0, 1.1]
LS_B = [20000, 10000, 9000]
COEF_TEMP = 100
COEF_HUMI = 50
THRED = 1.2

# sources: https://whatcomfamilyfarmers.org/breeds-of-dairy-cows/
# Holstein:
# Origin: Netherlands
# Weight: 1,200-1,500 lbs.
# Production: 22,000 lbs. per year
# Guernsey:
# Origin: Isle of Guernsey
# Weight: 1,100 lbs.
# Production: 16,500 lbs. per year
# Jersey:
# Origin: Jersey Island
# Weight: 1,000 lbs.
# Production: 16,500 lbs. per year

# ----------------------------


def sim_product(weight, w, b, lwer, uper):
    # farm condition
    weight = weight + random.uniform(lwer, uper)
    # production
    production = (
        w * weight
        + b
        + (temperature - 20) * COEF_TEMP
        + (humidity - 50) * COEF_HUMI
        + random.uniform(-1000, 1000)
    )
    # return
    return weight, production


def sample_breed():
    rdm_idx = random.randint(0, 2)
    breed = LS_BREEDS[rdm_idx]
    weight = LS_WEIGHTS[rdm_idx]
    w = LS_W[rdm_idx]
    b = LS_B[rdm_idx]
    return breed, weight, w, b


# farm_alpha: 2 records per day
records = []
for cow_id in range(1, N_COWS + 1):
    breed, weight, w, b = sample_breed()
    for day in range(N_DAYS):
        # Random temperature between 15 and 25 degrees Celsius
        temperature = round(random.uniform(15, 25), 1)
        # Random humidity between 30 and 80 percent
        humidity = round(random.uniform(30, 80), 1)
        for _ in range(2):
            weight, production = sim_product(weight, w, b, lwer=-5, uper=100)
            # health
            health = "productive" if production > b * THRED else "unproductive"
            # output
            record = {
                "ID": cow_id,
                "breed": breed,
                "farm_id": "farm_alpha",
                "day": day,
                "weight": round(weight, 3),
                "temperature": temperature,
                "humidity": humidity,
                "production": round(production, 3),
                "health": health,
            }
            records.append(record)
pd.DataFrame(records).to_csv(os.path.join("data_farm", "farm_alpha.csv"), index=False)

# farm_beta: 1 record per day
records = []
for cow_id in range(1, N_COWS + 1):
    breed, weight, w, b = sample_breed()
    for day in range(N_DAYS):
        # Random temperature between 15 and 25 degrees Celsius
        temperature = round(random.uniform(15, 25), 1)
        # Random humidity between 30 and 80 percent
        humidity = round(random.uniform(30, 80), 1)
        # sim data
        weight, production_A = sim_product(weight, w, b, lwer=-20, uper=10)
        weight, production_B = sim_product(weight, w, b, lwer=-20, uper=10)
        # health
        health = "good" if production > b * THRED else "bad"
        # output
        record = {
            "cow_id": cow_id,
            "BD": breed,
            "name": "farm_beta",
            "d": day,
            "weight": round(weight, 3),
            "temp": temperature,
            "humidity": humidity,
            "pA": round(production_A, 3),
            "pB": round(production_B, 3),
            "health": health,
        }
        records.append(record)
pd.DataFrame(records).to_csv(os.path.join("data_farm", "farm_beta.csv"), index=False)
