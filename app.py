import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("Decision_Tree.pkl")

st.set_page_config(page_title="Flight Delay Prediction", page_icon="✈️")

st.title("✈️ Flight Delay Prediction")
st.write("Enter flight details to predict whether the flight will be delayed.")

# ======================
# User Inputs
# ======================

distance = st.number_input("Distance", min_value=0.0, value=500.0)

scheduled_departure_hour = st.slider("Scheduled Departure Hour", 0, 23, 10)
actual_departure_hour = st.slider("Actual Departure Hour", 0, 23, 10)

scheduled_arrival_hour = st.slider("Scheduled Arrival Hour", 0, 23, 12)
actual_arrival_hour = st.slider("Actual Arrival Hour", 0, 23, 12)

cancelled = st.selectbox("Cancelled", [0, 1])
diverted = st.selectbox("Diverted", [0, 1])

airline = st.selectbox(
    "Airline",
    ["American", "Delta", "Southwest", "United"]
)

origin = st.selectbox(
    "Origin",
    ["ATL", "DFW", "JFK", "LAX", "ORD"]
)

destination = st.selectbox(
    "Destination",
    ["ATL", "JFK", "MIA", "SEA", "SFO"]
)

delay_reason = st.selectbox(
    "Delay Reason",
    ["No Delay", "Maintenance", "Weather", "Air Traffic Control"]
)

aircraft = st.selectbox(
    "Aircraft Type",
    ["Airbus A320", "Boeing 737", "Boeing 777"]
)

# ======================
# Create Input Data
# ======================

data = {
    "Cancelled": cancelled,
    "Diverted": diverted,
    "Distance": distance,
    "ScheduledDepartureHour": scheduled_departure_hour,
    "ActualDepartureHour": actual_departure_hour,
    "ScheduledArrivalHour": scheduled_arrival_hour,
    "ActualArrivalHour": actual_arrival_hour,

    "Airline_Delta": 1 if airline == "Delta" else 0,
    "Airline_Southwest": 1 if airline == "Southwest" else 0,
    "Airline_United": 1 if airline == "United" else 0,

    "Origin_DFW": 1 if origin == "DFW" else 0,
    "Origin_JFK": 1 if origin == "JFK" else 0,
    "Origin_LAX": 1 if origin == "LAX" else 0,
    "Origin_ORD": 1 if origin == "ORD" else 0,

    "Destination_JFK": 1 if destination == "JFK" else 0,
    "Destination_MIA": 1 if destination == "MIA" else 0,
    "Destination_SEA": 1 if destination == "SEA" else 0,
    "Destination_SFO": 1 if destination == "SFO" else 0,

    "DelayReason_Maintenance": 1 if delay_reason == "Maintenance" else 0,
    "DelayReason_No Delay": 1 if delay_reason == "No Delay" else 0,
    "DelayReason_Weather": 1 if delay_reason == "Weather" else 0,

    "AircraftType_Boeing 737": 1 if aircraft == "Boeing 737" else 0,
    "AircraftType_Boeing 777": 1 if aircraft == "Boeing 777" else 0,
}

input_df = pd.DataFrame([data])

# ======================
# Prediction
# ======================

if st.button("Predict"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("✈️ Flight will be Delayed")
    else:
        st.success("✅ Flight will NOT be Delayed")