import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Laptop Price Predictor")

ram = st.selectbox("RAM", [4, 8, 16])
storage = st.selectbox("Storage", [256, 512, 1024])

if st.button("Predict"):
    result = model.predict([[ram, storage]])
    st.write("Price:", int(result[0]))