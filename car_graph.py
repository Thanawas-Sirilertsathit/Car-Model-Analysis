from car import Car, car_subcategory
import matplotlib.pyplot as plt
import seaborn as sns


class CarGraph:

    def __init__(self):
        """Initialize data which inherit from car data"""
        self.car = Car()
        self.c_df = self.car.current_df
        self.brand = ""

    def car_category(self, brand, asp, num_door, fueltype, carbody):
        """Find car in giving categories"""
        if brand == "":
            self.brand = ""
        else:
            self.brand = brand
        self.c_df = car_subcategory(brand, asp, num_door, fueltype, carbody)

    def clear_previous_plot(self):
        """Clear the previous graph"""
        if self.ax:
            plt.close(self.ax.figure)

    def city_mpg_graph(self):
        """Create cityway and stroke correlation"""
        ax = sns.relplot(data=self.c_df, x="stroke", y="citympg", sizes=80)
        ax.set(xlabel='Stroke (Litre)', ylabel='City mpg')
        plt.title(f'City mpg and stroke correlation of {self.brand} car')
        return ax.fig

    def highway_mpg_graph(self):
        """Create highway and stroke correlation"""
        ax = sns.relplot(data=self.c_df, x="stroke", y="highwaympg", sizes=80)
        ax.set(xlabel='Stroke (Litre)', ylabel='Highway mpg')
        plt.title(f'Highway mpg and stroke correlation of {self.brand} car')
        return ax.fig

    def price_hist(self):
        """Create histogram for price"""
        fig, ax = plt.subplots()  # Create a new figure
        ax.hist(self.c_df["price"])
        ax.set(xlabel='Price ($)', ylabel='Frequency')
        ax.set_title(f'Histogram of {self.brand} car price')
        return fig

    def price_box(self):
        """Create boxplot for price"""
        fig, ax = plt.subplots()  # Create a new figure
        sns.boxplot(x='price', data=self.c_df, ax=ax)
        ax.set_title(f'Distribution of {self.brand} car price')
        return fig

    def pie_rpm(self):
        """Create peak rpm pie chart"""
        color_arr = ['r', 'b', 'c', 'm', 'springgreen', 'g', 'orange', 'navy']
        peakrpm = self.c_df["peakrpm"].unique()
        x = self.c_df.groupby(["peakrpm"]).count()
        fig, ax = plt.subplots()
        ax.pie(x["price"], labels=peakrpm, colors=color_arr,
               startangle=90, counterclock=False,
               autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(f'Percentage of peak rpm for {self.brand} cars')
        return fig

    def bar_horsepower(self):
        """Create bar chart for horsepower"""
        fig, ax = plt.subplots()
        y = self.c_df["horsepower"]
        x = self.c_df["CarName"]
        ax.bar(x, y, color="orange")
        ax.set_xlabel('Car models')
        ax.set_ylabel('Horsepower')
        ax.set_title(f'Horsepower bar chart for {self.brand} cars')
        ax.set_ylim(bottom=0)
        return fig

    def stackbar_dimensions(self):
        """Create stack bar chart for dimensions"""
        dimensions_agg = self.c_df.groupby(["CarName"]).agg(carwidth=(
            "carwidth", "mean"), carlength=("carlength", "mean"), carheight=("carheight", "mean"))
        fig, ax = plt.subplots()
        color_arr = ["orange", "c", "m"]
        dimensions_agg.plot(kind='bar', stacked=True, color=color_arr, ax=ax)
        ax.set_xlabel('CarName')
        ax.set_ylabel('Length (inch)')
        ax.set_title(f'Stack bar chart of {self.brand} car dimensions')
        ax.legend(title='Car dimensions')
        ax.set_ylim(bottom=0)
        return fig


if __name__ == '__main__':
    cg = CarGraph()
    cg.car_category("Honda", "Standard", "4 doors", "Gas", "Sedan")
    cg.city_mpg_graph()
    cg.car_category("Toyota", "Standard", "Default", "Gas", "Default")
    cg.stackbar_dimensions()
