from cargui import CarGUI
from car import Car

if __name__ == '__main__':
    car = Car()
    gui = CarGUI(car)
    gui.run()
