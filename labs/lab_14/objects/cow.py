from abc import ABC, abstractmethod
import pandas as pd


class Cow(ABC):
    def __init__(self, id, weights, productions):
        # constants
        self.ID = id
        self.BREED = ""  # string
        self.COEF_MILK = 500
        # breed standardization
        self.INIT_WEIGHT = 0
        self.W = 0  # slope
        self.B = 0  # intercept
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
