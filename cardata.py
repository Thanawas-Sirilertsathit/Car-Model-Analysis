import pandas as pd


class CarData:
    def __init__(self):
        self.__df = pd.read_csv("Cars.csv")

    @property
    def df(self):
        return self.__df
