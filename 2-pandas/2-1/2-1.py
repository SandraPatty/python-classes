import pandas as pd

df = pd.read_csv("transactions.csv")

print("The biggest payments are: ")
print(df[df['STATUS'] == 'OK'].sort_values(by=['SUM'], ascending=False).iloc[:3], '\n')

print("The total sum for Umbrella, Inc is: ")
print(df[(df['STATUS'] == 'OK') & (df['CONTRACTOR'] == 'Umbrella, Inc')].sum()['SUM'])