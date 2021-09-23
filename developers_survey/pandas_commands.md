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


filt_one_critiria = df['last'] == 'Doe'
df[filt_one_critiria]
    - give all rows with TRUE value of column last name == Doe
or

df.loc(filt_one_critiria , 'email')
    - same but only emails

filt_two_critiria = df['last'] == 'Doe' & df['first] == 'John'
    df[filt_two_critiria]
    - first condition and second condtion = TRUE


filt_two_critiria = df['last'] == 'Doe' | df['first] == 'John'
    - first condition OR second condtion = TRUE

filt_two_critiria = df['last'] == 'Doe' & df['first] == 'John'
    df[~filt_two_critiria]
    - give the oposite result of the filter = False

countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries)
df.loc[filt, 'Country']
    - filter based on list with countries, check if the field is in the list. 

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
    - return df based on existing of Python in the string

    [] change title of the column in upper case

df.columns = [x.upper() for x in df.columns]
    - make all labels upper case

df.columns = df.columns.str.replace(' ', '_')
    - remove spaces from labels replacing them with _

df.rename(columns={'old_name1':'new_name1', 'old_name':'new_name'}, inplace=True)
    - rename specific column giving a dict we must use inplace=True to save the changes in the df


     [] change title of the row in upper case

df.loc[2] = ['new_name', 'new_lastname', 'new_email']
    - change the value of a row 2 

df.loc[2 , 'new_lastname'] = "Smith"
    or
df.at[2 , 'new_lastname'] = "Smith"
    
    - change singe sell in df

    [] modify data with - (apply, map, applymap, replace)

df.['email'] = df['email].apply(lambda x: x.upper())
    - return all email with uppercase

df.applymap(len)
    - return len of each individual value in df

df.applymap(str.lower)
    - return all values in lower case

df['first'].map({'old_name':"new_name"})
    - will change the name and the other names will be NAN

df['first'].replace({"old_name":"new_name"})
    - will change the name and will keep the others as they are


    [] Add/Remove Rows and Columns From DataFrames

df['combine_column] = df['first_column] + ' ' + df['second_column'] 
    - combine column two columns

df.drop(columns=['first_c', 'second_c'], inplace=True)
    - remove two columns

df['full_name'].str.split(' ', expand=True)
    - splite one column to two 

df[['first_c', 'last']] = df['full_name'].str.split(' ', expand=True)
    - giving names to the new columns

df.append({'first': 'Tony'}, ignore_index=True)
    - add row to the end, other column will be NAN

df = df.append(df2, ignore_index=True, sort=False)
    - add one df to another

df.drop(index=4)
    -  remove rows

filt = df['last']=='Doe'
df.drop(index=df[filt].index)
    - remove with condition    

    [] SORT

df.sort_values(by='name_column')
    - sort based on column  

df.sort_values(by='name_column', ascending=False)
    - sort based on column - desc

df.sort_values(by=['first_column_condition',"second_c_condition"], ascending=[False,True], inplace=True)
    - sort based on two column - desc, desc

df['salary'].nlargest(10)
    - gives you 10 largest salaries only that column

df.nlargest(10, 'salary')
    - all df

df.nsmallest(10, 'salary')
    - all df

    [] Grouping and Aggregating

df['column_name'].median()
    - return average of the columns


df.describe()
    -return stats for count, mean, std min, max and more    

df['column_name'].count()
    - return all count answers

df['column_name'].value_count()
    - return counts per answers

df['column_name'].value_count(normalize=True)
    -  returns the relative frequency by dividing all values by the sum of values.

* Grouping the object - Split, Apply Function, Combine Results

df['Country'].value_counts()
    - return answers per Country

country_grp = df.groupby(['Country'])
    - return group OBJECT

country_grp.get_group('USA')
    - return all use answers

counter_grp['socialmedia].value_counts()
    - return socialmedias break douwn by countries

counter_grp['socialmedia].value_counts().loc['USA']
    - return socialmedias only for USA

country_grp['Salary].median()
    - return median per contry

country_grp['Salary].median().loc['Bulgaria']
    - return median per contry

country_grp['salary].agg(['median','mean'])
    - return median and mean by country

filt = df['Country'] == 'India'
df.loc[filt]['Languages'].str.contains('Python').sum()
    return sum of True value for this particular country 

country_grp["Salary"].apply(lambda x: x.str.contains('Python).sum())

country_grp = df.groupby(['country'])
country_uses_python = country_grp['languageworkedwith'].apply(lambda x: x.str.contains('Python').sum())

python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)

    [] REMOVE NAN DATAFRAME

df.dropna()
    - remove NAN rows

df.dropna(axis="index", how="any") 
    - same as df.dropna() 'any' - means one of the cell to be NAN will remove all row

df.dropna(axis="index", how="all") 
    - same as df.dropna() 'all' - all cells have to be missing values to remove it. 
    "index" can be coulmn

df.dropna(axis="index", how="any", subset=["email"])
    remove row if email coulmn is with missing value

import numpy as np
df.replace('NA', np.nan, inplace=True)
    - replase custum no data valeu with NAN

df.fillna('MISSING')
    - replase NAN with wat we want to fill in


    [] CASTING DATA TYPES

df.dtypes
    - give types of the cells - objects are like str


df['age'] = df['age'].astype(float)
    - convert NAN to float if we try with int throw an error 


na_vals = ['NA', 'Missing']
df = pd.read_csv('path to file', na_values = na_vals)
    -replase all NA and MIssing with NAN

df['column'].unique()
    - gives unique vlues