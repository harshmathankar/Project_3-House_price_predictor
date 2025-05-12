import streamlit as st
import joblib as jb
import numpy as np
import os
st.write("Files in current folder:", os.listdir())

#Loading trained model
model = jb.load('house_price_model.pkl')


#App UI
st.title("House Price Prediction")

#Inputs
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
TotRmsAbvGrd = st.slider("Total Rooms Above Ground", 1, 15, 6)
GrLivArea = st.number_input("Above ground living area (sq ft)", min_value=300, max_value=5000, value=1500)

ExterQual = st.selectbox("Exterior Quality", ['Poor', 'Fair', 'Average', 'Good', 'Excellent'])
KitchenQual = st.selectbox("Kitchen Quality",['Poor', 'Fair', 'Average', 'Good', 'Excellent'])
FireplaceQu = st.selectbox("Fireplace Quality", ['NA','Poor', 'Fair', 'Average', 'Good', 'Excellent'])

GarageCars = st.slider("Garage Capacity (Cars)", 0, 5, 1)
GarageFinish = st.selectbox("Garage Finish", ['NA', 'Unfinished', 'RoughlyFinished', 'Finished'])
GarageArea = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=400)

FirstFlrSF = st.number_input("First Floor Area (sq ft)", min_value=300, max_value=3000, value=1000)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)
BsmtQual = st.selectbox("Basement Quality", ['NA', 'Poor', 'Fair', 'Average', 'Good', 'Excellent'])

FullBath = st.slider("Full Bathrooms", 0, 4, 2)

YearBuilt = st.number_input("Year Built", min_value=1900, max_value=2023, value=2000)

YearRemodAdd = st.number_input("Year of Remodel/Add", min_value=1900, max_value=2023, value=2005)

# Encoding for categorical data
qual_mapping = {'NA': 0, 'Poor': 1, 'Fair': 2, 'Average': 3, 'Good': 4, 'Excellent': 5}
garage_finish_mapping = {'NA': 0, 'Unfinished': 1, 'RoughlyFinished': 2, 'Finished': 3}

# Create input array
input_data = np.array([[
    OverallQual,
    GrLivArea,
    qual_mapping[ExterQual],
    qual_mapping[KitchenQual],
    GarageCars,
    GarageArea,
    TotalBsmtSF,
    FirstFlrSF,
    qual_mapping[BsmtQual],
    FullBath,
    garage_finish_mapping[GarageFinish],
    TotRmsAbvGrd,
    YearBuilt,
    qual_mapping[FireplaceQu],
    YearRemodAdd
]])

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0] * 83.5
    st.success(f"🏷️ Estimated House Price: ₹{prediction:,.2f}")
