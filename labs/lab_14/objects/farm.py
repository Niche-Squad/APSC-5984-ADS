from abc import ABC, abstractmethod
import pandas as pd


class Farm(ABC):
    def __init__(self):
        self.data = pd.DataFrame()
        self.cows = []

    def load_data(self, filename):
        self.data = pd.read_csv(filename)

    @abstractmethod
    def preprocess(self):
        pass


class FarmAlpha(Farm):
    def __init__(self):
        super().__init__()

    def preprocess(self):
        data_new = (
            self.data.groupby(
                ["ID", "breed", "farm_id", "day", "temperature", "humidity"]
            )
            .aggregate(
                weight=("weight", "mean"),
                production=("production", "mean"),
                health=("health", "max"),  # ASCII: U > P
            )
            .reset_index()
        )
        # replace health column values-> productive->1, unproductive->0
        data_new["health"] = data_new["health"].replace(
            {"productive": 1, "unproductive": 0}
        )
        # assign the preprocessed data to the object attribute
        self.data = data_new


class FarmBeta(Farm):
    def __init__(self):
        super().__init__()

    def preprocess(self):  # rename the column names
        self.data.columns = [
            "ID",
            "breed",
            "farm_id",
            "day",
            "weight",
            "temperature",
            "humidity",
            "production_A",
            "production_B",
            "health",
        ]
        # tidy the data, turn pA and pB to one single column
        data_new = self.data.melt(
            id_vars=[
                "ID",
                "breed",
                "farm_id",
                "day",
                "weight",
                "temperature",
                "humidity",
                "health",
            ],
            value_vars=["production_A", "production_B"],
            var_name="production_type",
            value_name="production",
        )
        data_new = (
            data_new.groupby(
                ["ID", "breed", "farm_id", "day", "temperature", "humidity"]
            )
            .aggregate(
                weight=("weight", "mean"),
                production=("production", "mean"),
                health=("health", "max"),  # choose unproductive over productive
            )
            .reset_index()
        )
        # replace health column values-> good->1, bad->0
        data_new["health"] = data_new["health"].replace({"good": 1, "bad": 0})
        # assign the value to the attribute
        self.data = data_new
