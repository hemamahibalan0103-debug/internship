import pandas as pd

df = pd.read_csv("../../data/sample_data.csv")

print("Summary Statistics:")
print(df.describe())

print("\nCategory Counts:")
print(df['Category'].value_counts())
