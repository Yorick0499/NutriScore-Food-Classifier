def nutriscore_creator(data):
    data['Fat_points'] = 0
    data['Carbo_points'] = 0
    data['Sugar_points'] = 0
    data['Protein_points'] = 0
    data['Salt_points'] = 0
    
    daily_sugar_limit = 50
    daily_fat_limit = 66
    daily_carbo_limit = 325
    daily_protein_limit = 70
    daily_salt_limit = 6
    sugar_ratio = data['Sugar']/daily_sugar_limit*100
    fat_ratio = data['Fat']/daily_fat_limit*100
    carbo_ratio = data['Carbohydrates']/daily_carbo_limit*100
    protein_ratio = data['Protein']/daily_protein_limit*100
    salt_ratio = data['Salt']/daily_salt_limit*100

    rows_num = len(data)

    for i in range(rows_num):
        if sugar_ratio[i] < 5:
            data.loc[i,'Sugar_points'] = 5
        elif sugar_ratio[i] >= 5 and sugar_ratio[i] < 10:
            data.loc[i,'Sugar_points'] = 4
        elif sugar_ratio[i] >= 10 and sugar_ratio[i] < 15:
            data.loc[i,'Sugar_points'] = 3
        elif sugar_ratio[i] >= 15 and sugar_ratio[i] < 20:
            data.loc[i,'Sugar_points'] = 2 
        # elif sugar_ratio[i] >= 20 and sugar_ratio[i] < 25:
        #     data.loc[i,'Sugar_points'] = 1
        else:
            data.loc[i,'Sugar_points'] = 1

    for i in range(rows_num):
        if fat_ratio[i] < 5:
            data.loc[i,'Fat_points'] = 5
        elif fat_ratio[i] >= 5 and fat_ratio[i] < 10:
            data.loc[i,'Fat_points'] = 4
        elif fat_ratio[i] >= 10 and fat_ratio[i] < 15:
            data.loc[i,'Fat_points'] = 3
        elif fat_ratio[i] >= 15 and fat_ratio[i] < 20:
            data.loc[i,'Fat_points'] = 2
        # elif fat_ratio[i] >= 20 and fat_ratio[i] < 25:
        #     data.loc[i,'Fat_points'] = 1
        else:
            data.loc[i,'Fat_points'] = 1
    
    for i in range(rows_num):
        if protein_ratio[i] >= 24:
            data.loc[i,'Protein_points'] = 5
        elif protein_ratio[i] >= 20 and protein_ratio[i] < 24:
            data.loc[i,'Protein_points'] = 4
        elif protein_ratio[i] >= 8 and protein_ratio[i] < 20:
            data.loc[i,'Protein_points'] = 3
        elif protein_ratio[i] >= 5 and protein_ratio[i] < 8:
            data.loc[i,'Protein_points'] = 2
        # elif protein_ratio[i] >= 5 and protein_ratio[i] < 10:
        #     data.loc[i,'Protein_points'] = 1
        else:
            data.loc[i,'Protein_points'] = 1

    for i in range(rows_num):
        if salt_ratio[i] < 5:
            data.loc[i,'Salt_points'] = 5
        elif salt_ratio[i] >= 5 and salt_ratio[i] <= 7:
            data.loc[i,'Salt_points'] = 4
        elif salt_ratio[i] > 7 and salt_ratio[i] <= 25:
            data.loc[i,'Salt_points'] = 3
        elif salt_ratio[i] > 25 and salt_ratio[i] <= 30:
            data.loc[i,'Salt_points'] = 2
        # elif salt_ratio[i] > 30 and salt_ratio[i] <= 35:
        #     data.loc[i,'Salt_points'] = 1
        else:
            data.loc[i,'Salt_points'] = 1

    for i in range(rows_num):
        if carbo_ratio[i] <= 8:
            data.loc[i,'Carbo_points'] = 5
        elif carbo_ratio[i] > 8 and carbo_ratio[i] <= 15:
            data.loc[i,'Carbo_points'] = 4
        elif carbo_ratio[i] > 15 and carbo_ratio[i] <= 16:
            data.loc[i,'Carbo_points'] = 3
        elif carbo_ratio[i] > 16 and carbo_ratio[i] <= 17:
            data.loc[i,'Carbo_points'] = 2
        # elif carbo_ratio[i] > 17 and carbo_ratio[i] <= 18:
        #     data.loc[i,'Carbo_points'] = 1
        else:
            data.loc[i,'Carbo_points'] = 1

    
    data['NutriValue'] = data[['Sugar_points','Fat_points','Protein_points','Salt_points','Carbo_points']].mean(axis=1)

    data['NutriScore'] = data['NutriValue'].apply(lambda x: 'A' if (x <= 5 and x >= 4.5)
                                                        else ('B' if (x < 4.5 and x >= 4)
                                                              else ('C' if (x < 4 and x >= 3.4)
                                                                    else ('D' if (x < 3.4 and x >= 2.4)
                                                                          else 'E'))))