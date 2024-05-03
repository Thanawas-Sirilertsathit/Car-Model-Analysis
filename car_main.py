from cargui import CarGUI, CarController
from car import Car
from car_graph import CarGraph

if __name__ == '__main__':
    car = Car()
    cargraph = CarGraph()
    carcontrol = CarController()
    gui = CarGUI(car, carcontrol, cargraph)
    gui.title("Car Model Analysis")
    gui.run()
