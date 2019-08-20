# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie(alignment, labels=alignment.index)

plt.title('Character Alignment')

plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df['Strength'].cov(sc_df['Combat'])
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df['Intelligence'].cov(ic_df['Combat'])
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)

print(sc_pearson)
print(ic_pearson)


# --------------
#Code starts here

total_high = data['Total'].quantile(.99)
        
super_best = data[data['Total'] > total_high]

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
#print(data)
fig, (ax_1, ax_2, ax_3) = plt.subplots(3, 1)

ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')
plt.show()


