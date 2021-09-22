import pandas as pd
from openpyxl.workbook import Workbook

# 1. load data
df = pd.read_csv('pokemon_data.csv')

# read txt files
df_text = pd.read_csv('pokemon_data.txt', delimiter='\t')

"""

READING DATA IN PANDAS

"""


def read_data():
    # take first and last 5 records
    df_head = pd.read_csv('pokemon_data.csv').head(5)
    df_tail = pd.read_csv('pokemon_data.csv').tail(5)
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
    print(df.iloc[2, 1])
    # Read wor with loc based on text
    print(df.loc[df['Type 1'] == "Fire"])
    # look at - count, mean, std, min, max
    print(df.describe())
    # sort
    print(df.sort_values('Name', ascending=False))
    print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))


"""

CHANGES DATA

"""


# Total, create new column
def total(df):
    df['Total'] = df['HP'] + df["Attack"] + df["Defense"] + df["Sp. Def"] + df["Speed"] + df["Sp. Atk"]
    df['Total'] = df.iloc[:, 4:10].sum(axis=1)  # sum vertically
    print(df.head(5))


# Drop columns
def drop(df):
    df = df.drop(columns=['Total'])


# move column Total in the middle
def move_column(df):
    df['Total'] = df.iloc[:, 4:10].sum(axis=1)
    cols = list(df.columns)
    df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

    return df.iloc[:, 1:7].head(5)


df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
"""

SAVE DATA

"""


# save to csv, excel, txt

def save_modified_file(df):
    df.to_csv('modified.csv', index=False)
    df.to_excel('modified.xlsx', index=False)
    df.to_csv('modified.txt', index=False, sep='\t')


"""

FILTERING DATA : & , |, >, <, ~, contain

"""

# one condition

# df = df.loc[df['Type 1'] == "Grass"]

# two conditions we have to use () for each condition and use & sign or | for OR
df = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == 'Poison')]

# three
df = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == 'Poison') & (df["HP"] > 70)]

# reset old index

df = df.reset_index(drop=True)

# or reset in place

df.reset_index(drop=True, inplace=True)

# string contain another string

df = df.loc[df['Name'].str.contains('Mega')]

# string do not contain another string we can pass regex expresion

df = df.loc[~df['Name'].str.contains('Mega')]

# filtering using Regex: flags re.I - for lower cases
import re
df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]