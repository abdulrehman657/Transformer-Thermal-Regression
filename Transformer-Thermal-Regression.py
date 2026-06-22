import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel("D:\\Programs\\Transformer_Telemetry_Report.xlsx")

X = df[['Core Temperature C']].values
Y = df['Breakdown Voltage kV'] 


Model = linear_model.LinearRegression()
Model.fit(X, Y)


print("Accuracy:", f"{Model.score(X, Y)*100:.4f}%")
print("--------------------------------------------")

print("Intercept (Base Capacity):", f"{Model.intercept_:.2f} kV")
print("--------------------------------------------")

print("Slope Coefficient (Drop Rate):", f"{Model.coef_[0]:.4f} kV Per 1°C")
print("--------------------------------------------")

test_temp = 60

prediction = Model.predict([[test_temp]])

print(f"Prediction for {test_temp}°C Core Temp: {prediction[0]:.2f} kV Breakdown Threshold")


plt.figure(figsize=(9, 6))
plt.scatter(X, Y, color='royalblue', alpha=0.6, label='Sensor Data')

plt.plot(X, Model.predict(X), color='red', linewidth=2.5, label='Regression Line')

plt.title("Core Temperature vs Breakdown Voltage")
plt.xlabel("Core Temperature (C)")
plt.ylabel("Breakdown Voltage (kV)")
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend()

plt.show()