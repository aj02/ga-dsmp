# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
#print(data)

loan_status = data['Loan_Status'].value_counts()

loan_status.plot(kind='bar')
plt.xlabel('Loan status')
plt.ylabel('Loan status count')
plt.title('Distiribution of Loan status')
plt.show()


# --------------
#Code starts here
#print(data.columns)

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()

print(property_and_loan)

property_and_loan.plot(kind='bar', stacked=False)

plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=True)

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig , (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1)


ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')

ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income')

plt.show()


