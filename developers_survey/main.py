import pandas as pd

df = pd.read_csv('srp.csv', index_col='Respondent')


def head_csv(df):
    return df.head(10)


def tail_csv(df):
    return df.tail(10)


def shape_csv(df):
    return df.shape


def info_csv(df):
    return df.info()


# print(head_csv(df))
# print(tail_csv(df))
# print(shape_csv(df))
print(df.info())