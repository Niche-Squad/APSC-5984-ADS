import os
import pandas as pd

# import customized objects from farm.py
from farm import FarmAlpha, FarmBeta


class Analyzer:
    def __init__(self):
        self.farm_alpha = FarmAlpha()
        self.farm_beta = FarmBeta()
        # to keep the merged dataframe
        self.data = pd.DataFrame()

    def load_data(self, folder_path):
        # load data into farm alpha
        file_a = os.path.join(folder_path, "farm_alpha.csv")
        self.farm_alpha.load_data(file_a)
        # laod data into farm beta
        file_b = os.path.join(folder_path, "farm_beta.csv")
        self.farm_beta.load_data(file_b)

    def preprocess(self):
        """
        remove any conflict due to data format (columns, tidy format)
        """
        self.farm_alpha.preprocess()
        self.farm_beta.preprocess()

    def merge(self):
        self.data = pd.concat([self.farm_alpha.data, self.farm_beta.data])
