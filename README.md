# House Price Prediction App

A machine learning web application that predicts the price of a house based on features like overall quality, area, basement condition, and more. Built using **Streamlit**, trained with **Scikit-learn**, and deployed on **Streamlit Cloud**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features Used](#features-used)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [How to Run Locally](#how-to-run-locally)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

This project predicts house prices using a regression model trained on historical housing data. The model considers various physical and qualitative characteristics of a house to estimate its sale price. The project is presented as an interactive web application built with **Streamlit**.

---

## 📊 Features Used in Model

- `OverallQual` – Overall material and finish quality  
- `GrLivArea` – Above grade (ground) living area (sq ft)  
- `ExterQual` – Exterior material quality  
- `KitchenQual` – Kitchen quality  
- `GarageCars` – Size of garage (car capacity)  
- `GarageArea` – Garage area (sq ft)  
- `TotalBsmtSF` – Total basement area (sq ft)  
- `1stFlrSF` – First floor area (sq ft)  
- `BsmtQual` – Basement quality  
- `FullBath` – Number of full bathrooms  
- `GarageFinish` – Garage finish type  
- `TotRmsAbvGrd` – Total rooms above ground  
- `YearBuilt` – Year the house was built  
- `FireplaceQu` – Fireplace quality  
- `YearRemodAdd` – Year of last remodel

---

## Demo

 Click here to try the live app](https://housepricepredictorproject.streamlit.app/)

---

## Technologies Used

- Python 3.10+
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit
- Seaborn, Matplotlib (for visualizations)

---

## How to Run Locally

1. Clone the repository:

    git clone https://github.com/your-username/Project_3-House_price_predictor.git
    cd Project_3-House_price_predictor/House_price_app

2. Install dependencies:
    pip install -r requirements.txt

3. Run the app:
   streamlit run app.py

---

## Deployment
This app is deployed on Streamlit Cloud.
The model is saved as house_price_model.pkl using joblib and is loaded by the app to make predictions based on user inputs.


