import pandas as pd
import pyforest

df = pd.read_csv("5000 appids.csv")
df = df.drop(['752', '1'], axis=1)
df.to_csv("top 5000 most played.csv", index=False)
# print(df.head())