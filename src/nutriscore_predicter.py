import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import seaborn as sns
import pickle


path = 'data/cleaned_synth_data.csv'
data = pd.read_csv(path,sep='\t')
data['NutriScore'] = data['NutriScore'].apply(lambda x: 0 if x == 'A' else (1 if x == 'B' else (2 if x == 'C' else (3 if x == 'D' else 4))))
X = data[['Fat','Carbohydrates','Sugar','Protein','Salt']]
y = data['NutriScore']


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=123,stratify=y)


scaler = StandardScaler()
X = scaler.fit_transform(X)

k_values = [i for i in range(1,9)]
scores = []
for k in k_values:
    print(f'Started: {k}')
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn,X,y,cv=5)
    scores.append(np.mean(score))
    print(f'Completed: {k}')

sns.lineplot(x = k_values, y = scores, marker = 'o')
plt.xlabel('K values')
plt.ylabel('Accuracy')
plt.show()

best_index = np.argmax(scores)
best_k = k_values[best_index]

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=best_k))
])

pipeline.fit(X_train,y_train)


y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,average='weighted')
recall = recall_score(y_test,y_pred,average='weighted')
F_Score = f1_score(y_test,y_pred,average='weighted')

print(f'EVALUATION\nAccuracy: {accuracy:.3f}\nPrecision: {precision:.3f}\nRecall: {recall:.3f}\nF Score: {F_Score:.3f}')
print(confusion_matrix(y_test,y_pred))


with open('nutriscore_predicter.pkl', 'wb') as file:
    pickle.dump(pipeline,file)





# ## Testing on other dataset
# real_data = pd.read_csv('data/cleaned_food_data.csv',header=None)
# real_data = real_data.drop(real_data.columns[[0,1,2,8,9,10,11,12,13]],axis=1)
# real_data = real_data.drop(0,axis=0)

# y_pred = pipeline.predict(real_data)

# for i in y_pred:
#     if i == 4:
#         print('E')
#     elif i == 3:
#         print('D')
#     elif i == 2:
#         print('C')
#     elif i == 1:
#         print('B')
#     else:
#         print('A')