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

# Screenshots
| Project information and documents |
| ------------- |
| [Default page](https://media.discordapp.net/attachments/1015464234664067122/1236139411087954022/image.png?ex=6636ec09&is=66359a89&hm=cd460ceb7cd7837ed0e141f0fa7df85c74fb6fab188fcc0a8a7fbb663a21b743&=&format=webp&quality=lossless) |
| [Price histogram](https://media.discordapp.net/attachments/1015464234664067122/1236139862676078622/image.png?ex=6636ec75&is=66359af5&hm=ea511bfb8a9ae73666b4c05eded3c4c70c4c9dd7f7d83b2502894bab041aad50&=&format=webp&quality=lossless) |
| [Price boxplot](https://media.discordapp.net/attachments/1015464234664067122/1236139763212222464/image.png?ex=6636ec5d&is=66359add&hm=ad11a0a4e939ed3afd2dcb48579e8ccd0add44514191433370290e66db2288c6&=&format=webp&quality=lossless) |
| [Horsepower bar graph](https://media.discordapp.net/attachments/1015464234664067122/1236140392538443898/image.png?ex=6636ecf3&is=66359b73&hm=fd105ae17bdedaf6ad29bde7afcc899f100150a37b07257879d073871c126261&=&format=webp&quality=lossless&width=550&height=251) |
| [Stackbar chart for car dimensions](https://media.discordapp.net/attachments/1015464234664067122/1236140199596261477/image.png?ex=6636ecc5&is=66359b45&hm=e3f89f26eaa9ebbb0932c75f973a8b46dc12a8a9d122e243eb559978cfd37daf&=&format=webp&quality=lossless&width=550&height=256) |
| [Scatter plot for citympg and stroke](https://media.discordapp.net/attachments/1015464234664067122/1236140528853323787/image.png?ex=6636ed14&is=66359b94&hm=d3f24ca914202ad8d11e4bec1f986b35b189e27e7a2fb34cf3a9dac34d39bdd1&=&format=webp&quality=lossless) |
| [Statistics page](https://media.discordapp.net/attachments/1015464234664067122/1236140798114926663/image.png?ex=6636ed54&is=66359bd4&hm=9e5ffa6a1898519910940a82b3e71085eb1226282bcad562afce0719cb798388&=&format=webp&quality=lossless&width=550&height=284) |
| [Storytelling page](https://media.discordapp.net/attachments/1015464234664067122/1236140709275500615/image.png?ex=6636ed3f&is=66359bbf&hm=f3440fcc3032dad353ea134cafa6141f3faca99777904b4667698845a338662d&=&format=webp&quality=lossless&width=550&height=288) |

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
- [Sequence diagram for quit and story button](https://media.discordapp.net/attachments/1015464234664067122/1235956038205968465/Diagrams-5.jpg?ex=66364142&is=6634efc2&hm=8fca28fca49b01752a0f6454d7eb369c8dba29dc6b8572dc234a450d70e73337&=&format=webp&width=748&height=467)
- [Sequence diagram for graph button](https://media.discordapp.net/attachments/1015464234664067122/1235938869350891520/Diagrams-3.jpg?ex=66363145&is=6634dfc5&hm=ad7a603545821fefcd68e6ffb35116a413681b529ceead04a56c239f42f7fa49&=&format=webp&width=748&height=467)
- [Sequence diagram for combobox](https://media.discordapp.net/attachments/1015464234664067122/1235938869841498172/Diagrams-2.jpg?ex=66363145&is=6634dfc5&hm=77b4233b5d70397b645446a92c3a7dbb898742b03bb2c0afeb14565aa5ecf84a&=&format=webp&width=550&height=344)
- [Sequence diagram for category button](https://media.discordapp.net/attachments/1015464234664067122/1235938869984235660/Diagrams-1.jpg?ex=66363145&is=6634dfc5&hm=f34de4e9497381bbb6f56f281ee0bac5343a882d34ed085b82fd169a7e923f21&=&format=webp&width=550&height=344)
- [Sequence diagram for statistics button](https://media.discordapp.net/attachments/1015464234664067122/1235938870323974244/Diagrams-4.jpg?ex=66363145&is=6634dfc5&hm=572fc0f3e7fd8853300e611302cc265fd73ff88a53cf1a09f041b3db1155778f&=&format=webp&width=550&height=344)
