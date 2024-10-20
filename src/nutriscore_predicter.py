import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


path = 'data/cleaned_food_data.csv'
data = pd.read_csv(path)

le = LabelEncoder()
le.fit(['A','B','C','D'])

y =le.transform(['A','B','C','D'])

data['NutriScore'] = data['NutriScore'].apply(lambda x: 0 if x == 'A' else (1 if x == 'B' else (2 if x == 'C' else 3)))

data_train, data_test = train_test_split(data, test_size=0.2)


# model = KNeighborsClassifier(n_neighbors=2)
# model.fit(X, y)

