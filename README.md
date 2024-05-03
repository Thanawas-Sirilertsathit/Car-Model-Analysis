# Car Model Analysis
Car Model Analysis which analyzes car models for customers in car showroom and motor show.
This program will provide the users with insight into private fuel cars to compare the capabilities.
Users can create graphs in this program to find out the distribution of each attribute for each car model.

# Main features
- This program can be interacted by users via buttons and comboboxes.
- This program will create graph depends on the button that is pressed.
- The program also has data storytelling page which can be navigated by the story button.
- The program has progress bar running when creating graph and opening storytelling page.

# Description
  The program will let users select the categories. After that, the program will present the graph of the selected attribute. One of these is city mpg, highway mpg and stroke for showing correlation (This correlation will show the optimization of the car engine).

  Mainly, this program will let users select the car body, number of doors, fuel type, brand and aspiration to create the graph. This program will let users select attributes to create the graph. First one is the dimensions of the car. Second one is price. Third one is horsepower. Fourth one is mpg scores and km/l scores compared to stroke. Last one is the peak round per minute.

# Screenshots
To be added

# Reference of data
- [Reference](https://www.kaggle.com/datasets/goyalshalini93/car-data)

# Installation
Requirements (Having items below installed)
- Python version 3.9 or higher version
- Tkinter library
- Matplotlib module version 3.8.4
- Seaborn module version 0.12.3
- Pandas module version 1.5.3
- Pygame module version 2.5.2
- Numpy module version 1.24.1

# How to run the program
- Make sure you have installed the required modules
- Run the file car_main.py
- The program will show up with the default graph which is price boxplot.
- This page is called Exploratory page.
- After the program shows up, user can interact with the program by selecting categories and pressing buttons.

Storytelling page
- The story button will lead the user to another UI called Storytelling page.  

# UML class diagram
- [UML class diagram](https://media.discordapp.net/attachments/1015464234664067122/1235938870177300514/Diagrams-6.jpg?ex=66363145&is=6634dfc5&hm=1c3424bb78ac3dbb1e197fd8a7c582669afdb3c76768b09dcd200c4ec615e953&=&format=webp&width=550&height=344)

# Sequence diagram
- [Sequence diagram for quit and story button](https://media.discordapp.net/attachments/1015464234664067122/1235938868100988968/Diagrams-5.jpg?ex=66363144&is=6634dfc4&hm=d66d0b529e873e812464826cbb5dfde3551175788ae62660998029f76338c6a3&=&format=webp&width=748&height=467)
- [Sequence diagram for graph button](https://media.discordapp.net/attachments/1015464234664067122/1235938869350891520/Diagrams-3.jpg?ex=66363145&is=6634dfc5&hm=ad7a603545821fefcd68e6ffb35116a413681b529ceead04a56c239f42f7fa49&=&format=webp&width=748&height=467)
- [Sequence diagram for combobox](https://media.discordapp.net/attachments/1015464234664067122/1235938869841498172/Diagrams-2.jpg?ex=66363145&is=6634dfc5&hm=77b4233b5d70397b645446a92c3a7dbb898742b03bb2c0afeb14565aa5ecf84a&=&format=webp&width=550&height=344)
- [Sequence diagram for category button](https://media.discordapp.net/attachments/1015464234664067122/1235938869984235660/Diagrams-1.jpg?ex=66363145&is=6634dfc5&hm=f34de4e9497381bbb6f56f281ee0bac5343a882d34ed085b82fd169a7e923f21&=&format=webp&width=550&height=344)
- [Sequence diagram for statistics button](https://media.discordapp.net/attachments/1015464234664067122/1235938870323974244/Diagrams-4.jpg?ex=66363145&is=6634dfc5&hm=572fc0f3e7fd8853300e611302cc265fd73ff88a53cf1a09f041b3db1155778f&=&format=webp&width=550&height=344)
