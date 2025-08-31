import pandas as pd

df = pd.read_csv("../../data/sample_data.csv")
print("Before Cleaning:")
print(df.isnull().sum())

df.fillna(0, inplace=True)

print("After Cleaning:")
print(df.isnull().sum())
