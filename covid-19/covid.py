import pandas as pd

df = pd.read_csv('covid.csv')

print(df['cases'].head(10))