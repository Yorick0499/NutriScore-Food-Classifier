import pandas as pd
from data_cleaner import data

data.to_csv(path_or_buf='data/food_data_nutriscore.csv',index=False)