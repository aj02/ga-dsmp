# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
file = open(path, 'r')
data = np.genfromtxt(file, delimiter=',', skip_header=1)
print(data)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census = np.concatenate((data, new_record))
print(census)


# --------------
#Code starts here
age = census[:,0]

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

print('old')


# --------------
#Code starts here

race_0 = census[census[:, 2] == 0]
race_1 = census[census[:, 2] == 1]
race_2 = census[census[:, 2] == 2]
race_3 = census[census[:, 2] == 3]
race_4 = census[census[:, 2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 3
print(minority_race)





# --------------
#Code starts here

# find all senior citizens
senior_citizens = census[census[:, 0] > 60]

# calculate sum of senior citizens working hours
working_hours_sum = np.sum(senior_citizens[:, 6])

# claculate no of senior citizens
senior_citizens_len = len(senior_citizens)

# avg senior citizen working hours
avg_working_hours = working_hours_sum / senior_citizens_len

# display
print(avg_working_hours)


# --------------
#Code starts here

low = census[census[:, 1] <= 10]
high = census[census[:, 1] > 10]

avg_pay_high = np.mean(high[:, 7])

avg_pay_low = np.mean(low[:, 7])

print(avg_pay_low)
print(avg_pay_high)







