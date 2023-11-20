import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('flights.csv')

df['AMOUNT'] = 1
df = df.drop(['Unnamed: 0'], axis=1)

DF1 = df.groupby('CARGO').sum()['AMOUNT']
DF2 = df.groupby('CARGO').sum()['PRICE']
DF3 = df.groupby('CARGO').sum()['WEIGHT']

fig, axs = plt.subplots(1, 3, figsize=(19, 7))

plt.sca(axs[0])
DF1.plot.bar()
plt.ylabel('Amount')
plt.xlabel('')
plt.xticks(rotation=0)
plt.sca(axs[1])
DF2.plot.bar()
plt.ylabel('Price')
plt.xlabel('')
plt.xticks(rotation=0)
plt.sca(axs[2])
DF3.plot.bar()
plt.ylabel('Weight')
plt.xlabel('')
plt.xticks(rotation=0)

plt.savefig("2.png")
plt.show()