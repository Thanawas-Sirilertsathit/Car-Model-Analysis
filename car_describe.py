from car import Car
import pandas as pd

def describe():
    """Descriptive statistics for horsepower, stroke, city mpg and highway mpg"""
    c = Car()
    desc = c.df[["horsepower","stroke","citympg","highwaympg"]]
    print(desc.describe())

if __name__ == '__main__':
    describe()
    