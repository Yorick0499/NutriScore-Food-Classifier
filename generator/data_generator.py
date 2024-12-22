import pandas as pd
import numpy as np


# Loading and cleaning data
real_data = pd.read_csv('data/food_data.csv')

cleaned_data = real_data.rename(columns={'Calories (kcal)':'Calories',
                     'Fat (g)':'Fat',
                     'Carbohydrates (g)':'Carbohydrates',
                     'Sugar (g)':'Sugar',
                     'Protein (g)':'Protein',
                     'Salt (g)':'Salt',
                     'Color (drink)':'Color',
                     'Price (PLN)':'Price'})

for i in ['Fat','Carbohydrates','Sugar','Protein','Salt','Price']:
    cleaned_data[i] = cleaned_data[i].str.replace(',','.').astype('float64')

cleaned_data['Palm oil'] = cleaned_data['Ingredients'].str.contains('palmowy')
cleaned_data['Palm oil'] = cleaned_data['Palm oil'].apply(lambda x: 1 if x == True else 0)

cleaned_data['Karagen'] = cleaned_data['Ingredients'].str.contains('karagen')
cleaned_data['Karagen'] = cleaned_data['Karagen'].apply(lambda x: 1 if x == True else 0)

cleaned_data = cleaned_data.drop(columns=['Palm oil', 'Karagen'], axis=1)







# Generating synthetic numerical data
def numerical_data_generator(n):
    synthetic_data = pd.DataFrame()
    for i in list(cleaned_data.select_dtypes(np.number).columns):
        m = cleaned_data[i].mean()
        s = cleaned_data[i].std()
        if i != 'Price':
            synthetic_data[i] = abs(np.random.normal(m,s,n))
        else:
            synthetic_data[i] = np.random.uniform(0.75,50,n)
        if i != 'Calories':
            synthetic_data[i] = round(synthetic_data[i],1)
        else:
            synthetic_data[i] = synthetic_data[i].astype(int)
    return synthetic_data






# # Generating synthetic text data
def text_data_generator(n):
    synthetic_data = pd.DataFrame()
    for i in list(cleaned_data.select_dtypes(object)):
        random_list = cleaned_data[i].unique()
        for j in range(n):
            if i == 'Producer':
                rand_n_1 = np.random.randint(0,50)
                synthetic_data.loc[j, i] = random_list[rand_n_1]
            elif i == 'Name':
                rand_n_2 = np.random.randint(0,76)
                synthetic_data.loc[j, i] = random_list[rand_n_2]
            elif i == 'Category':
                rand_n_3 = np.random.randint(0,1)
                synthetic_data.loc[j, i] = random_list[rand_n_3]
            elif i == 'Subcategory':
                rand_n_4 = np.random.randint(0,23)
                synthetic_data.loc[j, i] = random_list[rand_n_4]
            elif i == 'Color':   
                rand_n_5 = np.random.randint(0,2)
                synthetic_data.loc[j, i] = random_list[rand_n_5]
            elif i == 'Taste':
                rand_n_6 = np.random.randint(0,30)
                synthetic_data.loc[j, i] = random_list[rand_n_6]
            else:
                rand_n_7 = np.random.randint(0,64)
                synthetic_data.loc[j, i] = random_list[rand_n_7]
            synthetic_data = synthetic_data.fillna('Green')
    return synthetic_data


print('Generating numerical data...')
synthetic_numerical_data = numerical_data_generator(100)
print('Generating text data...')
synthetic_text_data = text_data_generator(100)

print('Merging data...')
synthetic_dataset = pd.concat([synthetic_numerical_data,synthetic_text_data],axis=1)
print('Reordering data...')
synthetic_dataset_reordered = synthetic_dataset.iloc[:, [7,8,0,1,2,3,4,5,9,10,11,12,6,13]]
print('Saving data...')
synthetic_dataset_reordered.to_csv('data/new_synth_data.csv', sep='\t', index=False, header=True)
print('Successful!')