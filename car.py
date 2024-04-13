from cardata import CarData
import pandas as pd

class Car:
    def __init__(self):
        """Initialize the car data"""
        self.cardata = CarData()
        self.df = self.cardata.df
        self.current_df = self.df.copy()
        self.brand_list = []
        self.brand_list_init()

    def __new__(cls):
        """Make this class become a singleton class"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Car, cls).__new__(cls)
        return cls.instance
    
    def reset_df(self):
        """Reset the current dataframe to the original one"""
        self.current_df = self.df.copy()

    def find_brand(self, brand):
        """Filter the dataframe by using brand and output as current dataframe"""
        brand1 = brand.lower()
        if brand1 in self.brand_list:
            carname = self.df["CarName"].str.lower()
            filtered = self.df[carname.str.startswith(brand1)]
            if filtered is None:
                self.reset_df()
                return self.current_df
            self.current_df = filtered
            return self.current_df
        else:
            raise ValueError("Unexpected brand!")
    
    def brand_list_init(self):
        """Initialize brand list"""
        self.brand_list.clear()
        c_list = []
        for i in self.df["CarName"]:
            c = i.split(" ")
            c_list.append(c)
        for i in c_list:
            if i[0] in self.brand_list:
                continue
            else:
                self.brand_list.append(i[0])
        self.brand_list.append("")

    def aspiration_filter(self, asp):
        """Filter current dataframe using aspiration and output the current dataframe"""        
        if asp == "Default":
            return self.current_df
        elif asp == "Standard":
            self.current_df = self.current_df[self.current_df["aspiration"] == "std"]
            return self.current_df
        elif asp == "Turbo":
            self.current_df = self.current_df[self.current_df["aspiration"] == "turbo"]
            return self.current_df
        else:
            raise ValueError("Aspiration is not Default, Standard or Turbo")
        
    def door_filter(self, asp):
        """Filter current dataframe using door number and output the current dataframe"""
        if asp == "Default":
            return self.current_df
        elif asp == "2 doors" or asp == 2:
            self.current_df = self.current_df[self.current_df["doornumber"] == "two"]
            return self.current_df
        elif asp == "4 doors" or asp == 4:
            self.current_df = self.current_df[self.current_df["doornumber"] == "four"]
            return self.current_df
        else:
            raise ValueError("Door number is not Default, 2 doors or 4 doors")
        
    def fuel_filter(self, asp):
        """Filter current dataframe using fuel type and output the current dataframe"""
        if asp == "Default":
            return self.current_df
        elif asp == "Gas" or asp == "gas":
            self.current_df = self.current_df[self.current_df["fueltype"] == "gas"]
            return self.current_df
        elif asp == "Diesel" or asp == "diesel":
            self.current_df = self.current_df[self.current_df["fueltype"] == "diesel"]
            return self.current_df
        else:
            raise ValueError("Fuel type is not Default, gas or diesel")
    
    def car_body_filter(self, carbody):
        """Filter current dataframe using car body and output the current dataframe"""
        carbody = carbody.lower()
        carbody_list = self.df["carbody"].unique()
        if carbody in carbody_list:
            self.current_df = self.current_df[self.current_df["carbody"] == carbody]
            return self.current_df
        elif carbody == "" or carbody == "default":
            return self.current_df
        else:
            raise ValueError("Car body is not valid")

def car_subcategory(brand, aspiration, door_num, fueltype, car_body):
    """Function to filter multiple options of car
    param : brand (brand)
    param : aspiration (Default / Standard / Turbo)
    param : door_num (Default / 2 doors / 4 doors)
    param : fueltype (Default / Gas / Diesel)
    param : car_body (Car body style)
    return : carbody (last filter option)
    """
    car = Car()
    car_brand = car.find_brand(brand)
    car_aspiration = car.aspiration_filter(aspiration)
    car_door = car.door_filter(door_num)
    car_fuel = car.fuel_filter(fueltype)
    carbody = car.car_body_filter(car_body)
    return carbody

if __name__ == '__main__':
    toyota = car_subcategory("Toyota", "Standard", "2 doors", "Gas", "Default")
    print(toyota)
    honda = car_subcategory("Honda", "Standard", "4 doors", "Gas", "Sedan")
    print(honda)
    