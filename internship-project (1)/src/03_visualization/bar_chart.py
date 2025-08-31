import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sample_data.csv")

plt.bar(df['Category'], df['Value'])
plt.title("Category vs Value - Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
