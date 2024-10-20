import pandas as pd
import nutriscore_creator

path = 'data/food_data.csv'
data = pd.read_csv(path)

data = data.rename(columns={'Calories (kcal)':'Calories',
                     'Fat (g)':'Fat',
                     'Carbohydrates (g)':'Carbohydrates',
                     'Sugar (g)':'Sugar',
                     'Protein (g)':'Protein',
                     'Salt (g)':'Salt',
                     'Color (drink)':'Color',
                     'Price (PLN)':'Price'})

for i in ['Fat','Carbohydrates','Sugar','Protein','Salt','Price']:
    data[i] = data[i].str.replace(',','.').astype('float64')

data['Palm oil'] = data['Ingredients'].str.contains('palmowy')
data['Palm oil'] = data['Palm oil'].apply(lambda x: 1 if x == True else 0)

data['Karagen'] = data['Ingredients'].str.contains('karagen')
data['Karagen'] = data['Karagen'].apply(lambda x: 1 if x == True else 0)

print(nutriscore_creator.nutriscore_creator(data))
data = data.drop(columns=['Sugar_points','Fat_points','Protein_points',
                          'Salt_points','Carbo_points','NutriValue',
                          'Ingredients','Taste','Color'])

# print(data[['Producer','Name','NutriScore']].loc[data['NutriScore']=='B'])
# print(data[['Producer','Name','Sugar_points','Fat_points','Protein_points','Salt_points','Carbo_points','Nutriscore digit']].loc[data['Nutriscore']=='B'])
# print(data['Carbo_points'].unique())
# print(data.groupby('Nutriscore')['Price'].mean().round(2))
print(data[['Name','NutriScore']])