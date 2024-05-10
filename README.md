# Car Model Analysis
Car Model Analysis which analyzes car models for customers in car showroom and motor show.
This program will provide the users with insight into private fuel cars to compare the capabilities.
Users can create graphs in this program to find out the distribution of each attribute for each car model.

# Main features
- Has a default graph when the program starts.
- Allow users to select categories before submitting.
- After submitting categories, display graphs according to selections.
- To submit categories and display graphs or statistics, press one of seven buttons at the bottom of the menu bar.
- Contain a page for storytelling.


# Description
  The program will let users select the categories. After that, the program will present the graph of the selected attribute. One of these is city mpg, highway mpg and stroke for showing correlation (This correlation will show the optimization of the car engine).

  Mainly, this program will let users select the car body, number of doors, fuel type, brand and aspiration to create the graph. This program will let users select attributes to create the graph. First one is the dimensions of the car. Second one is price. Third one is horsepower. Fourth one is mpg scores and km/l scores compared to stroke. Last one is the peak round per minute.

# More information
- [Wiki page]()

# Screenshots and Diagrams
- [Document for screenshots and diagrams](https://docs.google.com/document/d/156f1vVpa-ThG6n808GfuVLRIFvJYINe_oeZpa_gHZdg/edit?usp=sharing)

# Reference of data
- [Reference](https://www.kaggle.com/datasets/goyalshalini93/car-data)

# Installation
Run these commands respectively
1. Clone github repository
- **git clone https://github.com/Thanawas-Sirilertsathit/Car-Model-Analysis.git**
2. Change directory to Car-Model-Analysis
- **cd Car-Model-Analysis**
3. Look for preview tag
- **git checkout preview**
4. Create new virtual environment
- **python -m venv env**
5. Activate virtual environment
- env\Scripts\activate (For window)
- source env/bin/activate (For mac and linux)
6. Install required modules
- **pip install -r requirements.txt**
7. Run car_main file
- **python car_main.py**

# How to run the program
- Make sure you have installed the required modules
- Run the file car_main.py
- The program will show up with the default graph which is price boxplot.
- This page is called Exploratory page.
- After the program shows up, user can interact with the program by selecting categories and pressing buttons.

Storytelling page
- The story button will lead the user to another UI called Storytelling page.  

