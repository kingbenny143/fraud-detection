import streamlit as st
# This line imports the Streamlit library, which is used for building interactive web applications in Python. Streamlit allows you to 
# create and share data applications easily, making it a popular choice for data scientists and developers to visualize and interact with
#  their data and models.
import pandas as pd
# Load the dataset
import joblib
# Load the trained model

model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection prediction App")
st.markdown("this enter the transaction details use the predict button")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT","TRANSFER", "CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount", min_value = 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance(sender)", min_value = 0.0, value = 10000.0)
newbalanceOrg = st.number_input("New Balance(sender)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance(receiver)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance(receiver)", min_value = 0.0, value = 0.0)

if st.button("Predict"):

    balanceDiffOrig = oldbalanceOrg - newbalanceOrg
    blanceDiffDest = newbalanceDest - oldbalanceDest

    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,

        # IMPORTANT:
        "newbalanceOrig": newbalanceOrg,

        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,

        # Engineered features
        "balanceDiffOrig": balanceDiffOrig,
        "blanceDiffDest": blanceDiffDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("The transaction can be fraud.")
    else:
        st.success("The transaction looks like it is not a fraud.")
