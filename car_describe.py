from car import Car
import pandas as pd


def describe(c):
    """Descriptive statistics for horsepower, stroke, city mpg and highway mpg"""
    desc = c[["horsepower", "stroke", "citympg", "highwaympg"]]
    return desc.describe()


if __name__ == '__main__':
    describe()
