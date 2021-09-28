# Basic commands

1. Read data or create df from scratch
    - import pandas as pd
    - df = DataFrame(my_dict)
      - or
    - df = pd.read_csv('path_to_csv_file')

2. General commands    
    - df.info()
    - df.describe()
    - df.head()
    - df.teil()
    - df['column'].max()
    - df['column'].min()
    - df['column'].sum()
    - df['column'].sum()/len(def['column'])
    - df['column'].mean()
    - df['column'].median()
    - df.dtypes
    - df.size
    - df.shape

3. Column
    - df.column
    - df['column_name']
    - df[['col1,col2']]
    - df['column1'].value_counts()
    - df.columns = [x.upper() for x in df.columns]
   
4. Rows
    - df.index
    - df.set_index('column_name')
    - df.loc['row_name']
    - df.loc['row_name1':'row_name2']
    - df.iloc['row_index']
    - df.iloc['row_index1 :'row_index2']
    - df.iloc['row_index1 :'row_index2','column1 : column2]
    
5. Conditions - FILTER
    - df['column_name1'] > 70
    - df['column_name1'] < 70
    - df['column_name1'] = 70
    - df['column_name1'] != 70
    - df.loc[df['column_name1'] > 70, 'column_name1]
    - df.loc[df['column_name1'] > 70, ['column_name1, column_name2']]
    
    - filter_str = df['column'].str.contains('WORD', na=False)
      result = df.loc[filter_str]

    - filt_first_cond = df['column'] == "word"
        filt_second_cond = df['column1'].str.contains('word').sum()
        return df.loc[filt_word][filt_second_cond]

6. Dropping stuff
    - df.drop('row_name')
    - df.drop(['row_name1', 'row_name2'])
    - df.drop(columns=['column1', 'column2'])
    - df.drop(['column1', 'column2'], axis=1)
    - df.drop(['column1', 'column2'], axis='columns')

7. Adding, rename new column 
    - df['new_column_name] = df['column1'] + df['column2']
    - df.rename(columns={
        'old_name1':'new_name1',
        'old_name2':'new_name2'
        },index ={'old_row1':'new_row1'})
    
8. Cleaning data
    
    - df['column'] = df['column'].astype(float)
    - df['column'].replace('string', number, inplace=True)
    - nan_df = df[all_data.isna().any(axis=1)]
    - df = df.dropna(how="all")
    - df.fillna(0)
   
9. SORT
    - df = df.sort_values(by='column1')
    - df.sort_values(by=['col1',"col2"], ascending=[False,True], inplace=True)
   
10. group by

    - column_grp = df.groupby(['column'])
    - column_grp.get_group('row')
    - column_grp['column1'].value_counts().loc['row']
    - column_grp['column1'].median()
    - column_grp['column1'].agg(['median', 'mean'])
    
11. Time

    - df['column'] = pd.to_datetime(df['column']).dt.month
   
12. Join/ concat
    - result = pd.concat([df1, df2], axis=1) -> column
    - result = pd.concat([df1, df2], axis=0) -> rows

13. Apply
    
    def get_city(address):
        return address.split(",")[1].strip(" ")
    
    df['City'] = df['Purchase Address'].apply(lambda x: f"{get_city(x)}")