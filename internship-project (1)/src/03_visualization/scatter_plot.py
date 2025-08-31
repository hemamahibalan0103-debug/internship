import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sample_data.csv")

plt.scatter(df['Experience'], df['Salary'], color='red')
plt.title("Experience vs Salary - Scatter Plot")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()
