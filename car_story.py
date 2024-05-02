import tkinter as tk
from tkinter import ttk
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from car import Car, car_subcategory
from car_graph import CarGraph


class CarStoryGUI(tk.Toplevel):
    """Graphical user interface of Car storytelling """

    def __init__(self, car: Car):
        """Initialize components and variables"""
        super().__init__()
        self.corr_coef = -999
        self.car = car
        self.car_graph = CarGraph()
        self.title("Car Storytelling Page")
        self.optiondisplay = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "black", "foreground": "yellow"}
        self.optiondisplay1 = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "blue", "foreground": "pink"}
        self.optiondisplay2 = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "orange", "foreground": "purple"}
        self.init_components()

    def init_components(self):
        """Create components and layout the UI."""
        # setting up frames
        top_frame1 = self.canvas_frame_top()
        lower_frame2 = self.canvas_frame_bottom()
        correl_frame3 = self.correlation_frame()
        text_frame = self.text_frame()
        top_frame1.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=2)
        lower_frame2.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=2)
        correl_frame3.pack(side=tk.TOP, expand=True,
                           fill=tk.BOTH, pady=2)
        text_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=2)
        self.setup_graph()

    def display_graph(self, graph, canvas):
        """Display the graph in the canvas"""
        self.clear_canvas(canvas)
        graph_canvas = FigureCanvasTkAgg(graph, master=canvas)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        if self.corr_coef != -999:
            correlation_text = f"Correlation Coefficient : {self.corr_coef:.2f}"
            if self.corr_coef == 0:
                correlation_text = correlation_text + "\n" +\
                    "Two attributes not depend on each others"
            elif self.corr_coef > 0:
                correlation_text = correlation_text + "\n" +\
                    "Two attributes increase and decrease in the same direction"
            else:
                correlation_text = correlation_text + "\n" +\
                    "Two attributes increase and decrease in the opposite direction"
            self.correlation_label.config(text=correlation_text)
        else:
            self.correlation_label.config(text="")

    def correlation_frame(self):
        """Create correlation frame"""
        frame = tk.Frame(self)
        self.correlation_label = tk.Label(
            frame, text="", **self.optiondisplay1)
        self.correlation_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        return frame

    def clear_canvas(self, canvas):
        """Delete previous content in the canvas include the text"""
        for widget in canvas.winfo_children():
            widget.destroy()

    def canvas_frame_top(self):
        """Create a canvas frame contains three canvas"""
        frame = tk.Frame(self)
        self.canvas1 = tk.Canvas(frame, bg="white")
        self.canvas2 = tk.Canvas(frame, bg="white")
        self.canvas3 = tk.Canvas(frame, bg="white")
        self.canvas1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.canvas2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.canvas3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        return frame

    def canvas_frame_bottom(self):
        """Create a canvas frame contains two canvas"""
        frame = tk.Frame(self)
        self.canvas4 = tk.Canvas(frame, bg="white")
        self.canvas5 = tk.Canvas(frame, bg="white")
        self.canvas4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.canvas5.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        return frame

    def text_frame(self):
        """Create a frame for description text and quit button"""
        frame = tk.Frame(self)
        self.quit_button = tk.Button(frame, text="Quit", **self.optiondisplay)
        description = tk.Label(
            frame, text="In motor show or in car showroom, there are some situations that customer wants to see cars before test drive or buy. \n It will be a good option if customers can see overall capabilities and designs for each car model in interested brand. \n Moreover, customers may want to specify about number of doors for hanging out with family or going with few people. \n Some customers may want to know about aspiration of the car which has turbo or not. \n For this situation, we simulate that this place is Honda car showroom. \n Customers may want to know about efficiency of Honda cars and they may want to know about length, width and height of cars.", **self.optiondisplay2)
        description.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.quit_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.quit_button.bind("<Button>", self.quit_handler)
        return frame

    def setup_graph(self):
        self.car_graph.car_category(
            "Honda", "Default", "Default", "Default", "Default")
        self.corr_coef = np.corrcoef(
            self.car_graph.c_df["stroke"], self.car_graph.c_df["citympg"])[0, 1]
        self.corr_coef = round(self.corr_coef, 2)
        self.display_graph(self.car_graph.stackbar_dimensions(), self.canvas1)
        self.display_graph(self.car_graph.price_box(), self.canvas2)
        self.display_graph(self.car_graph.price_hist(), self.canvas3)
        self.display_graph(self.car_graph.bar_horsepower(), self.canvas4)
        self.display_graph(self.car_graph.city_mpg_graph(), self.canvas5)

    def quit_handler(self, event=tk.Event):
        """Quit the program"""
        self.destroy()

    def run(self):
        """Run the program"""
        self.mainloop()
