import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sample_data.csv")

plt.hist(df['Salary'], bins=5, color='blue', alpha=0.7)
plt.title("Salary Distribution - Histogram")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
