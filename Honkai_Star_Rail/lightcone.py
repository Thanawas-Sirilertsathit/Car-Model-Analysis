from dict_finder import dict_finder
import pandas as pd
class Lightcone:
    def __init__(self):
        self.df = pd.read_csv("lightcone.csv")
        self.__name = list(self.df["Name"])
    
    @property
    def name(self):
        return self.__name
    
    def path_index(self, path):
        path_df = self.df[self.df["Path"] == path]
        return path_df
    
if __name__ == '__main__':
    l = Lightcone()
    print(l.name)
    print(l.path_index("Harmony"))