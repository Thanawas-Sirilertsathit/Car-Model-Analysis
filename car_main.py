from cargui import CarGUI, CarController
from car import Car

if __name__ == '__main__':
    car = Car()
    carcontrol = CarController()
    gui = CarGUI(car, carcontrol)
    gui.title("Car Model Analysis")
    gui.run()
