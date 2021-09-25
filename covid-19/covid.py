import pandas as pd

df = pd.read_csv('covid.csv')

df.rename(columns={'countriesAndTerritories':'country_name'},inplace=True)

def group_dead_per_country(df):
    country_grp = df.groupby(['country_name'])
    deaths_per_country = country_grp['deaths'].sum()
    cases_per_country = country_grp['cases'].sum()
    result = pd.concat([cases_per_country, deaths_per_country],axis='columns', sort=False)
    result['pct_deaths'] =(result['deaths']/result['cases']) * 100
    result.sort_values(by="pct_deaths",ascending=False, inplace=True)
    result.to_csv('deaths_per_country', index=True)
    print(result)

group_dead_per_country(df)

# filt = df['country_name'] == 'Bulgaria'
#
# sum_deaths_bg = df[filt]['deaths'].sum()
# sum_cases_bg = df[filt]['cases'].sum()
#
# sum_deaths_all = df['deaths'].sum()
# sum_cases_all = df['cases'].sum()
#
#
# percentage_all = (sum_deaths_all/sum_cases_all) * 100
#
# print(sum_deaths_all)
# print(sum_cases_all)
# print(percentage_all)
#
# percentage_bg = (sum_deaths_bg/sum_cases_bg) * 100
#
# print(sum_deaths_bg)
# print(sum_cases_bg)
# print(percentage_bg)
#
#
