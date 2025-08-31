import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../../data/sample_data.csv")

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

exp = 6
pred = model.predict([[exp]])
print(f"Predicted salary for {exp} years experience: {pred[0]}")
