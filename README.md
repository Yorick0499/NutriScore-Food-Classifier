# NutriScore Food Classifier
![nutriscore](https://github.com/user-attachments/assets/d0718889-c7ba-40bf-a947-33ae926e7d84)
## Project description
This project aims to classify food products based on a custom NutriScore system. The main goal is to use a ML model that will assign the nutriscore label to products based on proteins, fats, etc.
## How it works
This works with the food dataset which is located in "data" folder.
"data_cleaner.py" is a script which cleaning data from food dataset and use "nutriscore_creator" function. Mentioned function is a custom NutriScore system based on fat, carbohydrates, protein, sugar and salt attributes.
Then the data_saver script exports the data to a new csv file.
Further functionalities are in the development phase
## Current model evaluation
Accuracy: 71%\
#################--------

Precision: 62%\
###############----------

Recall: 71%\
#################--------

F-score: 64%\
################---------
######  Update: 12.11.2024
