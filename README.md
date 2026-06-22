# Transformer Thermal Degradation Analysis ⚡

This project utilizes **Simple Linear Regression** to model the relationship between transformer core temperatures and the dielectric breakdown voltage of insulating oil. By analyzing historical telemetry data, this model provides a predictive maintenance tool to forecast potential insulation failure before it occurs.

## 📊 Project Overview
- **Objective**: Determine the rate of insulation breakdown as a function of thermal stress.
- **Model**: Scikit-Learn Linear Regression.
- **Dataset**: 500+ records of industrial transformer telemetry logs.
- **Key Metrics**: 
  - **Base Capacity (Intercept)**: The theoretical maximum dielectric strength at 0°C.
  - **Degradation Rate (Slope)**: The rate of voltage loss per 1°C increase.

## 🚀 Features
* **Automated Modeling**: Quick execution pipeline using `pandas` and `scikit-learn`.
* **Professional Visualization**: Generates a clean regression plot demonstrating the degradation curve.
* **Telemetry Reporting**: Includes a script to export beautified Excel reports with conditional "Heatmap" formatting to highlight risk zones.

## 🛠️ Getting Started
1. **Clone the repository**: `git clone https://github.com/abdulrehman657/Transformer-Thermal-Regression.git`
2. **Install dependencies**: 
   ```bash
   pip install pandas numpy matplotlib scikit-learn openpyxl
3. **Content**: `The Excel File And The Python File`
