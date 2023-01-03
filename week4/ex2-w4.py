import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#one
df = pd.read_csv('california_housing_train.csv')

xpoints = np.array(df['total_rooms'])
ypoints1 = np.array(df['median_house_value'])
ypoints2 = np.array(df['population'])

plt.plot(xpoints,ypoints1)
plt.plot(xpoints,ypoints2)

plt.show()



