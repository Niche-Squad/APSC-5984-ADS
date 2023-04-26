import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
from abc import ABC, abstractmethod

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols


class Analyzer:
    def __init__(self):
        self.farm_alpha = FarmAlpha()
        self.farm_beta = FarmBeta()
        self.data = pd.DataFrame()

    def load_data(self, data_path):
        # farm alpha
        self.farm_alpha.load_data(os.path.join(data_path, "farm_alpha.csv"))
        self.farm_beta.load_data(os.path.join(data_path, "farm_beta.csv"))
        # polymorphism
        for farm in [self.farm_alpha, self.farm_beta]:
            farm.load_cows()
            farm.standardize_breeds()

    def merge_farms(self):
        self.data = pd.concat([self.farm_alpha.data, self.farm_beta.data])

    def build_anova(self):
        formula = "production_std ~ C(breed) + C(farm_id) + C(breed):C(farm_id)"
        model = ols(formula, self.data).fit()
        aov_table = sm.stats.anova_lm(model, typ=2)
        print(aov_table)
        return aov_table

    def pred_ols(self):
        X_train, X_test, y_train, y_test = self.__split_data()
        # fit
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        # vis
        self.__vis_pred(y_test, y_pred)
        # return
        return model

    def pred_rf(self):
        X_train, X_test, y_train, y_test = self.__split_data()
        # fit
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        # vis
        self.__vis_pred(y_test, y_pred)
        # return
        return model

    def figure_1(self, y="production_std"):
        sns.catplot(
            data=self.data,
            x="farm_id",
            y=y,
            kind="box",
        )

    def figure_2(self):
        sns.lineplot(
            data=self.data,
            x="day",
            y="production_std",
            hue="farm_id",
            style="breed",
            errorbar=None,
        )

    def __vis_pred(self, y_test, y_pred):
        sns.scatterplot(x=y_test, y=y_pred)
        plt.annotate(
            "correlation: {:.4f}".format(np.corrcoef(y_test, y_pred)[0, 1]),
            xy=(0.1, 0.9),
            xycoords="axes fraction",
        )

    def __split_data(self, test_size=0.2):
        # split data
        X = self.data[["day", "farm_id", "breed", "temperature", "humidity"]]
        # get_dummy
        X = pd.get_dummies(X, columns=["farm_id", "breed"])
        y = self.data["production"]
        # split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        return X_train, X_test, y_train, y_test


class Farm(ABC):
    def __init__(self):
        # constants
        self.FARM_NAME = ""
        # data
        self.data = pd.DataFrame()
        self.cows = []

    def load_data(self, data_path):
        data = pd.read_csv(data_path)
        self.data = self.preprocess(data)

    def load_cows(self):
        for id in self.data["ID"].unique():
            data_sub = self.data.query("ID == @id").sort_values("day")
            breed = data_sub["breed"].values[0]
            weights = data_sub["weight"].values
            productions = data_sub["production"].values
            if breed == "Holstein":
                cow = Holstein(id, weights, productions)
            elif breed == "Jersey":
                cow = Jersey(id, weights, productions)
            elif breed == "Guernsey":
                cow = Guernsey(id, weights, productions)
            self.cows.append(cow)

    def standardize_breeds(self):
        std_weight = []
        std_production = []
        for cow in self.cows:
            cow.standardize_breed()
            std_weight.extend(cow.weights_std)
            std_production.extend(cow.productions_std)
        self.data["weight_std"] = std_weight
        self.data["production_std"] = std_production

    @abstractmethod
    def preprocess(self, data):
        pass


class FarmAlpha(Farm):
    def __init__(self):
        super().__init__()
        self.FARM_NAME = "farm_alpha"

    def preprocess(self, data):
        data_new = (
            data.groupby(["ID", "breed", "farm_id", "day", "temperature", "humidity"])
            .aggregate(
                weight=("weight", "mean"),
                production=("production", "mean"),
                health=("health", "max"),
            )
            .reset_index()
        )
        data_new["health"] = data_new["health"].replace(
            {"productive": 1, "unproductive": 0}
        )
        return data_new


class FarmBeta(Farm):
    def __init__(self):
        super().__init__()
        self.FARM_NAME = "farm_beta"

    def preprocess(self, data):
        data.columns = [
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
        data_new = data.melt(
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
                health=("health", "max"),
            )
            .reset_index()
        )
        # replace health column values-> good->1, bad->0
        data_new["health"] = data_new["health"].replace({"good": 1, "bad": 0})
        return data_new


class Cow(ABC):
    def __init__(self, id, weights, productions):
        # constants
        self.ID = id
        self.BREED = ""  # string
        self.COEF_MILK = 500
        # breed standardization
        self.INIT_WEIGHT = 0
        self.W = 0
        self.B = 0
        # data
        self.weights = weights
        self.productions = productions
        self.weights_std = []
        self.productions_std = []

    def standardize_breed(self):
        self.standardize_weights()
        self.standardize_productions()

    def standardize_weights(self):
        self.weights_std = self.weights - self.INIT_WEIGHT

    def standardize_productions(self):
        self.productions_std = ((self.productions - self.B) / self.W) - self.INIT_WEIGHT


class Holstein(Cow):
    def __init__(self, id, weights, productions):
        super().__init__(id, weights, productions)
        self.BREED = "Holstein"
        self.INIT_WEIGHT = 1200
        self.W = 1.3
        self.B = 20000


class Jersey(Cow):
    def __init__(self, id, weights, productions):
        super().__init__(id, weights, productions)
        self.BREED = "Jersey"
        self.INIT_WEIGHT = 1000
        self.W = 1.0
        self.B = 10000


class Guernsey(Cow):
    def __init__(self, id, weights, productions):
        super().__init__(id, weights, productions)
        self.BREED = "Guernsey"
        self.INIT_WEIGHT = 1100
        self.W = 1.1
        self.B = 9000


# # TEST CODE
# analyzer = Analyzer()
# analyzer.load_data("data_farm")
# analyzer.merge_farms()

# analyzer.figure_1()
# analyzer.figure_2()

# analyzer.build_anova()
# analyzer.pred_ols()
# analyzer.pred_rf()
