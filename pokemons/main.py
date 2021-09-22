import pandas as pd

# 1. load data
df = pd.read_csv('pokemon_data.csv')

# take first and last 5 records
df_head = pd.read_csv('pokemon_data.csv').head(5)
df_tail = pd.read_csv('pokemon_data.csv').tail(5)

# read txt files
df_text = pd.read_csv('pokemon_data.txt', delimiter='\t')

"""

READING DATA IN PANDAS

"""
def read_data():
    # Read Headers - column
    print(df.columns)
    # Read each Column
    print(df['Name'])
    # Read multiple Column - indexing
    print(df[['Name', 'Type 1', 'HP']])
    # Read Each Row - iloc
    print(df.iloc[0:4])
    # Iterrows Row - iterrows
    for index, row in df.iterrows():
        print(index, row['Name'])
    # Read a specific Location(R,C) iloc + row and column
    print(df.iloc[2,1])
    # Read wor with loc based on text
    print(df.loc[df['Type 1'] == "Fire"])
    # look at - count, mean, std, min, max
    print(df.describe())
    # sort
    print(df.sort_values('Name', ascending=False))
    print(df.sort_values(['Type 1','HP'], ascending=[1,0]))

"""

CHANGES DATA

"""
