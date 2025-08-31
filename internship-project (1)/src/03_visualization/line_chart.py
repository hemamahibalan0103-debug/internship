import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sample_data.csv")

plt.plot(df['Experience'], df['Salary'], marker='o')
plt.title("Experience vs Salary - Line Chart")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()
