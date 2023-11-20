import pandas as pd
import os
import matplotlib.pyplot as plt

T1 = pd.read_excel(os.path.join('students', 'students_info.xlsx'))
T2 = pd.read_html(os.path.join('students', 'results_ejudge.html'))[0]
T = T1.merge(T2, left_on='login', right_on='User')
print(T)
T.groupby('group_faculty')['Solved'].mean().plot.bar()
plt.title('Mean by faculty')
plt.savefig('Mean by faculty.png')
plt.subplots()

T.groupby('group_out')['Solved'].mean().plot.bar()
plt.title('Mean by groups')
plt.savefig('Mean by groups.png')
plt.subplots()
T[(T['G'] > 10) | (T['H'] > 10)].groupby('group_faculty')['Solved'].count().plot.bar()
plt.title('Score by faculty')
plt.savefig('Score by faculty.png')
plt.subplots()
T[(T['G'] > 10) | (T['H'] > 10)].groupby('group_out')['Solved'].count().plot.bar()
plt.title('Score by group')
plt.savefig('Score by group.png')
plt.show()