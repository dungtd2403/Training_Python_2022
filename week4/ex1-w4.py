import pandas as pd

#one
df = pd.read_csv('california_housing_train.csv')
data = df[['total_rooms', 'total_bedrooms', 'population', 'median_house_value']]
DataTotalRooms = df['total_rooms']

#two
maxMHV = 0
sumMHV = 0
for x in df.index:
    sumMHV += df.loc[x, 'median_house_value']
    if df.loc[x, 'median_house_value'] > maxMHV:
       maxMHV = df.loc[x, 'median_house_value']


#three
a = df.loc[1, 'median_house_value']
data2 = [a]
for x in df.index:
    if x == 0:
        data2[0] = df.loc[1, 'median_house_value']
    else:
        i = data2[x-1] + df.loc[x, 'median_house_value']
        data2.append(i)
#print(pd.Series(data2))



#print(data, DataTotalRooms, maxMHV, sumMHV)