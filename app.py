
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from pathlib import Path

# -------------------------------
# Load Model and Dataset
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent

try:
    with open(BASE_DIR / "pipe.pkl", "rb") as file:
        pipe = pickle.load(file)

    st.success("Model loaded successfully!")

except Exception as e:
    st.error(f"Model Loading Error: {e}")

try:
    with open(BASE_DIR / "df.pkl", "rb") as file:
        df = pickle.load(file)

    st.success("Dataset loaded successfully!")

except Exception as e:
    st.error(f"Dataset Loading Error: {e}")

# -------------------------------
# Streamlit App
# -------------------------------

st.title("💻 Laptop Price Predictor")

# Brand
company = st.selectbox(
    "Brand",
    df["Company"].unique()
)

# Laptop Type
typename = st.selectbox(
    "Type",
    df["TypeName"].unique()
)

# RAM
ram = st.selectbox(
    "RAM (in GB)",
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)

# Weight
weight = st.number_input(
    "Weight of the Laptop (kg)",
    min_value=0.5,
    max_value=5.0,
    value=1.5,
    step=0.1
)

# Touchscreen
touchscreen = st.selectbox(
    "Touchscreen",
    ["No", "Yes"]
)

# IPS
ips = st.selectbox(
    "IPS Display",
    ["No", "Yes"]
)

# Screen Size
screen_size = st.slider(
    "Screen Size (inches)",
    10.0,
    18.0,
    13.0
)

# Screen Resolution
resolution = st.selectbox(
    "Screen Resolution",
    [
        "1920x1080",
        "1366x768",
        "1600x900",
        "3840x2160",
        "3200x1800",
        "2880x1800",
        "2560x1600",
        "2560x1440",
        "2304x1440"
    ]
)

# CPU
cpu = st.selectbox(
    "CPU",
    df["Cpu brand"].unique()
)

# HDD
hdd = st.selectbox(
    "HDD (in GB)",
    [0, 128, 256, 512, 1024, 2048]
)

# SSD
ssd = st.selectbox(
    "SSD (in GB)",
    [0, 8, 128, 256, 512, 1024]
)

# GPU
gpu = st.selectbox(
    "GPU",
    df["Gpu brand"].unique()
)

# Operating System
os = st.selectbox(
    "Operating System",
    df["os"].unique()
)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Price"):

    # Convert Yes/No to 1/0
    touchscreen_value = 1 if touchscreen == "Yes" else 0
    ips_value = 1 if ips == "Yes" else 0

    # Calculate PPI
    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])

    ppi = (
        ((x_res ** 2) + (y_res ** 2)) ** 0.5
    ) / screen_size

    # Create DataFrame
    query = pd.DataFrame({
        "Company": [company],
        "TypeName": [typename],
        "Ram": [ram],
        "Weight": [weight],
        "Touchscreen": [touchscreen_value],
        "Ips": [ips_value],
        "ppi": [ppi],
        "Cpu brand": [cpu],
        "HDD": [hdd],
        "SSD": [ssd],
        "Gpu brand": [gpu],
        "os": [os]
    })

    try:
        # Predict
        prediction = pipe.predict(query)[0]

        # Convert log price to original price
        predicted_price = np.exp(prediction)

        st.success(
            f"Predicted Laptop Price: ₹{predicted_price:,.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")