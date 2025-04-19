import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📡 Network Quality Dashboard: Packet Loss, RTT & Jitter")

@st.cache_data
def load_data():
    df = pd.read_csv("packet_loss_log.csv", parse_dates=["timestamp"])
    df["packet_loss_percent"] = ((df["sent"] - df["received"]) / df["sent"]) * 100
    df["jitter_ms"] = df["rtt_ms"].diff().abs().fillna(0)
    return df

df = load_data()

# 📋 Show Raw Data
st.subheader("📋 Raw Data")
st.dataframe(df)

# 📉 Packet Loss Chart
st.subheader("📉 Packet Loss Over Time")
fig_loss = px.line(df, x="timestamp", y="packet_loss_percent", title="Packet Loss (%) Over Time")
st.plotly_chart(fig_loss)

# ⏱️ RTT Chart
st.subheader("⏱️ Round Trip Delay (RTT) Over Time")
fig_rtt = px.line(df, x="timestamp", y="rtt_ms", title="Round Trip Delay (ms) Over Time", markers=True)
st.plotly_chart(fig_rtt)

# 🔁 Jitter Chart
st.subheader("🔁 Jitter Over Time (RTT Variation)")
fig_jitter = px.line(df, x="timestamp", y="jitter_ms", title="Jitter (ms) Over Time", markers=True)
st.plotly_chart(fig_jitter)

# 📊 Summary Stats
st.subheader("📊 Summary Statistics")
st.write("📦 Packet Loss %")
st.write(df["packet_loss_percent"].describe())

st.write("⏱️ RTT (ms)")
st.write(df["rtt_ms"].describe())

st.write("🔁 Jitter (ms)")
st.write(df["jitter_ms"].describe())
