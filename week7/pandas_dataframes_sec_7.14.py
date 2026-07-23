"""
Intro to Data Science: Pandas DataFrames
"""

# import pandas
import pandas as pd




print("df:", df)

# index
print(df["Age"])
print(df["Age"].mean())

print(sum(df["Age"]) / len(df["Age"]))

# new column
df["Score_Percent"] = df["Score"]/100
print(df)

# summary information
print(df.describe())