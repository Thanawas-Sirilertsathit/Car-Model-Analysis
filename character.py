from dict_finder import dict_finder
import pandas as pd
import numpy as np
import random
class Character:
    def __init__(self):
        self.df = pd.read_csv("hsr.csv")
        self.__name = list(self.df["Name"])
        self.random_range = np.linspace(-5,5,num = 5000)
    
    @property
    def name(self):
        return self.__name
    
    def path_index(self, path):
        path_df = self.df[self.df["Path"] == path]
        return path_df
    
    def type_index(self, _type):
        type_df = self.df[self.df["Type"] == _type]
        return type_df
    
if __name__ == '__main__':
    c = Character()
    print(c.name)
    print(c.type_index("Imaginary"))
    print(c.path_index("Harmony"))
    print(c.random_range)
    