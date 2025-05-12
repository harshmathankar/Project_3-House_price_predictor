import streamlit as st
import joblib as jb
import numpy as np

#Loading trained model
model = jb.load('C:\\Users\\harsh\\Downloads\\minor project\\II. House price prediction\\house_price_app\\House_price_app\\house_price_model.pkl')


#App UI
st.title("House Price Prediction")

#Inputs
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
TotRmsAbvGrd = st.slider("Total Rooms Above Ground", 1, 15, 6)
GrLivArea = st.number_input("Above ground living area (sq ft)", min_value=300, max_value=5000, value=1500)

ExterQual = st.selectbox("Exterior Quality", ['Po', 'Fa', 'TA', 'Gd', 'Ex'])
KitchenQual = st.selectbox("Kitchen Quality", ['Po', 'Fa', 'TA', 'Gd', 'Ex'])
FireplaceQu = st.selectbox("Fireplace Quality", ['NA', 'Po', 'Fa', 'TA', 'Gd', 'Ex'])

GarageCars = st.slider("Garage Capacity (Cars)", 0, 5, 1)
GarageFinish = st.selectbox("Garage Finish", ['NA', 'Unf', 'RFn', 'Fin'])
GarageArea = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=400)

FirstFlrSF = st.number_input("First Floor Area (sq ft)", min_value=300, max_value=3000, value=1000)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)
BsmtQual = st.selectbox("Basement Quality", ['NA', 'Po', 'Fa', 'TA', 'Gd', 'Ex'])

FullBath = st.slider("Full Bathrooms", 0, 4, 2)

YearBuilt = st.number_input("Year Built", min_value=1900, max_value=2023, value=2000)

YearRemodAdd = st.number_input("Year of Remodel/Add", min_value=1900, max_value=2023, value=2005)

# --- Encoding for categoricals (you must match this with training-time encoding) ---
qual_mapping = {'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
garage_finish_mapping = {'NA': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}

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

# --- Prediction ---
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0] * 83.5
    st.success(f"🏷️ Estimated House Price: ₹{prediction:,.2f}")
