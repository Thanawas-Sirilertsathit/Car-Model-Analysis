import tkinter as tk
from tkinter import ttk
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from car import Car, car_subcategory
from car_graph import CarGraph
from pygame import mixer
from car_describe import describe


class CarGUI(tk.Tk):
    """Graphical user interface of Car model analysis"""

    def __init__(self, car: Car):
        """Initialize components and variables"""
        super().__init__()
        self.corr_coef = -999
        self.car = car
        self.car_graph = CarGraph()
        self.controller = CarController()
        self.title("Car Model Analysis")
        self.brand_var = tk.StringVar()
        self.carbody_var = tk.StringVar()
        self.optiondisplay = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "black", "foreground": "yellow"}
        self.optiondisplay1 = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "blue", "foreground": "pink"}
        self.optiondisplay2 = {"padx": 2, "pady": 2, "font": (
            "Arial", 12), "background": "orange", "foreground": "purple"}
        mixer.init()
        self.init_components()

    def play_sound_error(self):
        """Playing sound when dataset is empty or event handler receive Error return from controller"""
        mixer.music.load("Error.mp3")  # to be added
        mixer.music.play()

    def default_graph(self):
        """Create a default graph"""
        figure = self.controller.graph("Price (Box)")
        self.display_graph(figure)

    def init_components(self):
        """Create components and layout the UI."""
        self.init_brand_and_carbody()
        # setting up frames
        top_frame1 = self.combobox_category_frame()
        top_frame2 = self.category_button_frame()
        top_frame3 = self.graph_button_frame()
        canvas_frame = self.canvas_frame()
        correl_frame = self.correlation_frame()
        top_frame1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        top_frame2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        top_frame3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        canvas_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        correl_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.default_graph()

    def init_brand_and_carbody(self):
        """Initialize brand list and carbody list"""
        self.brands = list(self.car.brand_list.copy())
        self.brands.insert(0, "")
        self.brands.pop()
        self.carbody_list = list(self.car.carbody_list.copy())
        self.carbody_list.insert(0, "")

    def display_graph(self, graph):
        """Display the graph in the canvas"""
        self.clear_canvas()
        graph_canvas = FigureCanvasTkAgg(graph, master=self.canvas)
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
        frame = tk.Frame()
        self.correlation_label = tk.Label(
            frame, text="", **self.optiondisplay1)
        self.correlation_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        return frame

    def clear_canvas(self):
        """Delete previous content in the canvas"""
        for widget in self.canvas.winfo_children():
            widget.destroy()

    def combobox_category_frame(self):
        """A frame that contains comboboxes"""
        frame = tk.Frame()
        brand_l = tk.Label(frame, text="Brand : ",
                           **self.optiondisplay1)
        self.brand_c = ttk.Combobox(frame, values=self.brands, font=(
            "Arial", 12), foreground="blue", textvariable=self.brand_var)
        carbody_l = tk.Label(frame, text="Car body : ",
                             **self.optiondisplay1)
        self.carbody_c = ttk.Combobox(frame, values=self.carbody_list, font=(
            "Arial", 12), foreground="blue", textvariable=self.carbody_var)
        self.brand_c.current(newindex=0)
        self.carbody_c.current(newindex=0)
        story = tk.Button(frame, text="Story", **self.optiondisplay)
        brand_l.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.brand_c.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        carbody_l.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.carbody_c.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        story.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.carbody_c.bind("<<ComboboxSelected>>",
                            self.category_combo_handler)
        self.brand_c.bind("<<ComboboxSelected>>", self.category_combo_handler)
        story.bind("<Button>", self.story_handler)
        return frame

    def category_button_frame(self):
        """A frame that contains category choice buttons"""
        frame = tk.Frame()
        self.fueltype_b = tk.Button(
            frame, text="Default", **self.optiondisplay2)
        self.aspiration_b = tk.Button(
            frame, text="Default", **self.optiondisplay2)
        self.numdoor_b = tk.Button(
            frame, text="Default", **self.optiondisplay2)
        numdoor_l = tk.Label(
            frame, text="Number of doors : ", **self.optiondisplay1)
        aspiration_l = tk.Label(
            frame, text="Aspiration : ", **self.optiondisplay1)
        fueltype_l = tk.Label(frame, text="Fuel type : ",
                              **self.optiondisplay1)
        numdoor_l.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.numdoor_b.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        aspiration_l.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.aspiration_b.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        fueltype_l.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.fueltype_b.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.numdoor_b.bind("<Button>", self.category_button_handler)
        self.aspiration_b.bind("<Button>", self.category_button_handler)
        self.fueltype_b.bind("<Button>", self.category_button_handler)
        return frame

    def graph_button_frame(self):
        """A frame that contains graph buttons"""
        frame = tk.Frame()
        dimensions = tk.Button(frame, text="Dimensions", **self.optiondisplay)
        horsepower = tk.Button(frame, text="Horsepower", **self.optiondisplay)
        peakrpm = tk.Button(frame, text="Peak rpm", **self.optiondisplay)
        self.price = tk.Button(frame, text="Price (Box)", **self.optiondisplay)
        self.mpg_score = tk.Button(
            frame, text="Mpg scores and strokes (City)", **self.optiondisplay)
        stat = tk.Button(frame, text="Statistics", **self.optiondisplay)
        dimensions.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        horsepower.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        peakrpm.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.price.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.mpg_score.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        stat.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        dimensions.bind("<Button>", self.graph_button_handler)
        horsepower.bind("<Button>", self.graph_button_handler)
        peakrpm.bind("<Button>", self.graph_button_handler)
        self.price.bind("<Button>", self.graph_button_handler)
        self.mpg_score.bind("<Button>", self.graph_button_handler)
        stat.bind("<Button>", self.stat_button_handler)
        return frame

    def canvas_frame(self):
        frame = tk.Frame()
        self.canvas = tk.Canvas(frame, bg="white")
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        return frame

    def graph_button_handler(self, event=tk.Event):
        """Event handler for graph buttons"""
        widget = event.widget
        self.corr_coef = -999
        result_graph = self.controller.graph(widget["text"])
        if widget["text"] == "Price (Box)":
            self.price.config(text="Price (Hist)", bg="Purple")
        elif widget["text"] == "Price (Hist)":
            self.price.config(text="Price (Box)", bg="Magenta")
        elif widget["text"] == "Mpg scores and strokes (City)":
            self.corr_coef = np.corrcoef(
                self.controller.current_df["stroke"], self.controller.current_df["citympg"])[0, 1]
            self.mpg_score.config(
                text="Mpg scores and strokes (Highway)", bg="Purple")
            self.corr_coef = round(self.corr_coef, 2)
        elif widget["text"] == "Mpg scores and strokes (Highway)":
            self.corr_coef = np.corrcoef(
                self.controller.current_df["stroke"], self.controller.current_df["highwaympg"])[0, 1]
            self.mpg_score.config(
                text="Mpg scores and strokes (City)", bg="Magenta")
            self.corr_coef = round(self.corr_coef, 2)
        else:
            widget.config(bg="Green")
        self.display_graph(result_graph)

    def stat_button_handler(self, event=tk.Event):
        widget = event.widget
        widget.config(bg="Green")
        stat = self.controller.stat()
        self.clear_canvas()
        stat_str = stat.to_string()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        center_x = canvas_width / 2
        center_y = canvas_height / 2
        self.canvas.create_text(
            center_x, center_y, anchor="center", text=stat_str, font=("Arial", 15))

    def category_button_handler(self, event=tk.Event):
        """Event handler for category buttons"""
        widget = event.widget
        if widget == self.fueltype_b:
            if widget["text"] == "Default":
                self.fueltype_b.config(text="Gas")
            elif widget["text"] == "Gas":
                self.fueltype_b.config(text="Diesel")
            elif widget["text"] == "Diesel":
                self.fueltype_b.config(text="Default")
        elif widget == self.aspiration_b:
            if widget["text"] == "Default":
                self.aspiration_b.config(text="Standard")
            elif widget["text"] == "Standard":
                self.aspiration_b.config(text="Turbo")
            elif widget["text"] == "Turbo":
                self.aspiration_b.config(text="Default")
        elif widget == self.numdoor_b:
            if widget["text"] == "Default":
                self.numdoor_b.config(text="2 doors")
            elif widget["text"] == "2 doors":
                self.numdoor_b.config(text="4 doors")
            elif widget["text"] == "4 doors":
                self.numdoor_b.config(text="Default")
        cdf = self.controller.select(
            self.brand_var.get(), self.aspiration_b["text"], self.numdoor_b["text"], self.fueltype_b["text"], self.carbody_var.get())
        if cdf.empty:
            print("Dataframe contains nothing")
            # self.play_sound_error()
        else:
            print(cdf)

    def category_combo_handler(self, event=tk.Event):
        """Event handler for comboboxes"""
        widget = event.widget
        cdf = self.controller.select(
            self.brand_var.get(), self.aspiration_b["text"], self.numdoor_b["text"], self.fueltype_b["text"], self.carbody_var.get())
        if cdf.empty:
            print("Dataframe contains nothing")
            # self.play_sound_error()
        else:
            print(cdf)

    def story_handler(self, event=tk.Event):
        """Leading to another UI that is Storytelling page"""
        pass  # to be added

    def run(self):
        """Run the program"""
        self.mainloop()


class CarController:
    """Controller for CarGUI (MVC design)"""

    def __init__(self):
        """Initialize car class"""
        self.car = Car()
        self.car_graph = CarGraph()
        self.current_df = self.car.current_df

    def select(self, brand, aspiration, door_num, fueltype, car_body):
        """MVC design (Delegate from View or CarGUI)"""
        self.current_df = car_subcategory(
            brand, aspiration, door_num, fueltype, car_body)
        self.car_graph.brand = brand
        if self.current_df is None:
            return None
        else:
            return self.current_df

    def graph(self, text):
        """Return graph and update canvas"""
        self.car_graph.c_df = self.current_df
        try:
            if text == "Dimensions":
                return self.car_graph.stackbar_dimensions()
            elif text == "Horsepower":
                return self.car_graph.bar_horsepower()
            elif text == "Peak rpm":
                return self.car_graph.pie_rpm()
            elif text == "Price (Hist)":
                return self.car_graph.price_hist()
            elif text == "Price (Box)":
                return self.car_graph.price_box()
            elif text == "Mpg scores and strokes (Highway)":
                return self.car_graph.highway_mpg_graph()
            elif text == "Mpg scores and strokes (City)":
                return self.car_graph.city_mpg_graph()
            elif text == "Statistics":
                pass
        except IndexError:
            self.current_df = self.car.df.copy()
            self.car_graph.c_df = self.current_df
            if text == "Dimensions":
                return self.car_graph.stackbar_dimensions()
            elif text == "Horsepower":
                return self.car_graph.bar_horsepower()
            elif text == "Peak rpm":
                return self.car_graph.pie_rpm()
            elif text == "Price (Hist)":
                return self.car_graph.price_hist()
            elif text == "Price (Box)":
                return self.car_graph.price_box()
            elif text == "Mpg scores and strokes (Highway)":
                return self.car_graph.highway_mpg_graph()
            elif text == "Mpg scores and strokes (City)":
                return self.car_graph.city_mpg_graph()
            elif text == "Statistics":
                pass

    def stat(self):
        return describe()
