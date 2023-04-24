import random
import pandas as pd

# Constants
NUM_COWS = 50
NUM_FARMS = 4
NUM_DAYS = 30
NUM_HOURS = 24

# Generate walking_activity_data
ls_walking = []
for cow_id in range(1, NUM_COWS + 1):
    farm_id = random.randint(1, NUM_FARMS)
    for day in range(NUM_DAYS):
        for hour in range(NUM_HOURS):
            # Random steps per hour between 50 and 200
            steps = random.randint(50, 200)
            # Random temperature between 15 and 25 degrees Celsius
            temperature = round(random.uniform(15, 25), 1)
            # Random humidity between 30 and 80 percent
            humidity = round(random.uniform(30, 80), 1)

            hourly_record = {
                "cow_id": cow_id,
                "farm_id": farm_id,
                "day": day,
                "hour": hour,
                "steps": steps,
                "temperature": temperature,
                "humidity": humidity,
            }

            ls_walking.append(hourly_record)

data_walk = pd.DataFrame(ls_walking)
data_milk = (
    data_walk.groupby(["cow_id", "farm_id"])
    .aggregate(
        temperature=("temperature", "mean"),
        humidity=("humidity", "mean"),
        steps=("steps", "sum"),
    )
    .reset_index()
)

data_milk["yield"] = (
    2000
    - (data_milk["temperature"] * 0.3)
    + (data_milk["humidity"] * 0.5)
    + (data_milk["steps"] * 0.1)
) / 10
data_milk = data_milk.loc[:, ["cow_id", "farm_id", "yield"]]

data_milk.to_csv("data_milk.csv", index=False)
data_walk.to_csv("data_walk.csv", index=False)
