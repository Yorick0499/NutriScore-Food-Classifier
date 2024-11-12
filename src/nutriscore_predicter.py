import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


path = 'data/food_data_nutriscore.csv'
data = pd.read_csv(path)

data['NutriScore'] = data['NutriScore'].apply(lambda x: 0 if x == 'A' else (1 if x == 'B' else (2 if x == 'C' else (3 if x == 'D' else 4))))

X = data[['Fat','Carbohydrates','Sugar','Protein','Salt']]
y = data['NutriScore']

pca = PCA(n_components=2)


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=124,stratify=y)
X_train = pca.fit_transform(X_train)
X_test = pca.fit_transform(X_test)

model = KNeighborsClassifier(n_neighbors=14)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,average='weighted')
recall = recall_score(y_test,y_pred,average='weighted')
F_Score = f1_score(y_test,y_pred,average='weighted')

### Model evaluation
print(f'EVALUATION\nAccuracy: {accuracy:.3f}\nPrecision: {precision:.3f}\nRecall: {recall:.3f}\nF Score: {F_Score:.3f}')
# print(confusion_matrix(y_test,y_pred))
