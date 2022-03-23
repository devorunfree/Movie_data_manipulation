import pandas as pd
import numpy as np

df = pd.read_csv("IMDb_movies.csv") 
#                 parse_dates=["date_published"],
#                 date_parser = lambda x : pd.to_datetime(x, format='%Y-%m-%d'))


df = df.rename(columns={"worlwide_gross_income": "worldwide_gross_income"})

df["imdb_title_id"] = df["imdb_title_id"].str[2:]
df["budget"] = df["budget"].str.replace("$", "")
df["budget"] = df["budget"].replace(',','', regex=True)
df["budget"] = df["budget"].str.extract(r'(\d+)', expand=False)
pd.to_numeric(df["budget"])

df["usa_gross_income"] = df["usa_gross_income"].str.replace("$", "")
df["usa_gross_income"] = df["usa_gross_income"].replace(',','', regex=True)
df["usa_gross_income"] = df["usa_gross_income"].str.extract(r'(\d+)', expand=False)
df["usa_gross_income"] = pd.to_numeric(df["usa_gross_income"])

df["worldwide_gross_income"] = df["worldwide_gross_income"].str.replace("$", "")
df["worldwide_gross_income"] = df["worldwide_gross_income"].replace(',','', regex=True)
df["worldwide_gross_income"] = df["worldwide_gross_income"].str.extract(r'(\d+)', expand=False)
pd.to_numeric(df["worldwide_gross_income"])

df["date_published"] = pd.to_datetime(df["date_published"]).dt.strftime('%Y-%m-%d')
pd.to_datetime(df["date_published"])

df["year"] = pd.to_numeric(df["year"])

df


df[["original_title","usa_gross_income", "date_published"]].loc[df['year']==2018].sort_values(by="usa_gross_income", ascending=False, ignore_index = True)[0:10]

df[["original_title","genre", "avg_vote"]].sort_values(by="avg_vote", ascending=False, ignore_index = True)[0:1]



#prompt for user input to search dataframe for specific actor
user_inp = input("Enter the name of an actor:")

result = df[df["actors"].str.contains(user_inp, regex = True, na=False)]
result[["original_title","actors", "year"]]
# print(result)


df[["original_title","duration"]].sort_values(by="duration", ascending=True, ignore_index = True)[0:1]
