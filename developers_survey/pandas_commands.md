# PANDAS 

dataframe - multidemantional list rows and columns
series - rows of the single columns
iloc - interger location - looks for indexes
loc - look for labels

#main commands

    [] basic

pd.read_csv('path to the file + file extenstion')
    - load the file
pd.shape
    - info - num of colmn and rows
pd.info()
    - inf - column and thair types
df.columns
    - return only names of the columns
pd.head()
    - return first 5 rows
pd.tail()
    -return last 5 rows
pd.DataFrame("name_python_dict")
    - create a Data Frame from a python dict - is important the values to be a list.

    [] set index column

pr.read_csv('pat.csv', index_col='name_of_the_column')
    - read the file and remove the defoult index column

   [] columns 

df['name_column'] or df.email
    - return only one column
df[['first column', 'second c]]
    - get myltiple column

df['name_column'].value_counts()

    [] rows 

df.iloc[0]
    - returns a series first one

df.iloc[[0, 1], 2]
    -return first 2 rows of data

df.loc[[0, 1], ['email','last']]

    [] rows and columns

df.loc[:, 'Hobbyist':'Employment']
    returns all rows from column H to E(included)

df.loc[:6, 1:5]
    returns first 5 rows from column 1 to 4

    [] index

df.set_index('email')
    - will set column email as a index without changing the df

df.set_index('email', inplace=True)
    - will set column email as a index changing the DataFrame

df.loc[test@mail.bg]
    - in a result we can filter by name of the index column

df.sort_index()
    - sort index ascending, no change df

df.sort_index(ascending=False)
    - sort index descending, no chane df

df.sort_index(inplace=True)
    - sort index ascending, change df

    [] filtering

