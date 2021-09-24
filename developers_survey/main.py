import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 10)
df = pd.read_csv('srp.csv', index_col='Respondent')


def head_csv(df):
    return df.head(10)


def tail_csv(df):
    return df.tail(10)


def shape_csv(df):
    return df.shape


def info_csv(df):
    return df.info()


def column_csv(df):
    return df.columns


def shape_csv(df):
    return df.shape


def one_column(df):
    one_column_series = df['Hobbyist']
    one_column_series_value = df['Hobbyist'].value_counts()
    return f"{one_column_series}\n\n{one_column_series_value}"


def describe(df):
    return df.describe()


def loc(df):
    one_column_data = df.loc[:, 'Hobbyist']
    two_column_data_for_3_rows = df.loc[[1, 4], ['Hobbyist', 'Country']]
    two_column_how_row = df.loc[:, ['Hobbyist', 'Country']]
    from_to_column_how_rows = df.loc[:, 'Hobbyist': 'Country']
    return f'{one_column_data} \n ' \
           f'{two_column_data_for_3_rows} \n ' \
           f'{two_column_how_row}\n' \
           f'{from_to_column_how_rows}'


def iloc(df):
    data_rows_colmns = df.iloc[:, 1:5].head(10)
    data_row = df.iloc[[0, 1], 2]
    data_single_cell = df.iloc[0, 3]
    return f'{data_rows_colmns}\n' \
           f'{data_row}\n' \
           f'{data_single_cell}'


def high_salary(df):
    high_salary_filter = df['ConvertedComp'] > 7000
    result = df.loc[high_salary_filter, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]
    return result


def language_Python_info(df):
    filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
    result = df.loc[filt]
    return result['LanguageWorkedWith']


def change_to_upper_labels(df):
    df.columns = [x.upper() for x in df.columns]
    return df.columns


def change_to_lower_labels(df):
    df.columns = [x.lower() for x in df.columns]
    return df.columns


def change_name_column(df):
    df.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True)

    return df['SalaryUSD']


def sort_df(df):
    age = df.sort_values(by='Age')
    return f"{age}"

def sort_df_two(df):
    df.sort_values(by=['Age',"Country"], ascending=[False,True], inplace=True)
    # df['salary'].nlargest(10)
    # df.nlargest(10, 'salary')
    # df.nsmallest(10, 'salary')

    return df
# print(head_csv(df))
# print(tail_csv(df))
# print(shape_csv(df))
# print(df.info())
# print(column_csv(df))
# print(shape_csv(df))
# print(one_column(df))
# print(describe(df))
# print(loc(df))
# print(iloc(df))
# print(high_salary(df))
# print(language_Python_info(df))
# print(change_to_upper_labels(df))
# print(change_to_lower_labels(df))
# print(change_name_column(df))
# print(column_csv(df))
# print(sort_df(df))
print(sort_df_two(df))
