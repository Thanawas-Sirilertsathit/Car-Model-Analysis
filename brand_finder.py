import pandas as pd

def find_brand(brand):
    df = pd.read_csv("Cars.csv")
    brand1 = brand.lower()
    carname = df["CarName"].str.lower()
    filtered = df[carname.str.startswith(brand1)]
    return filtered
    
if __name__ == '__main__':
    test_df = find_brand("BMW")
    