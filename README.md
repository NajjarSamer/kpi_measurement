# KPI Measurement Dashboard

This is an interactive dashboard built with [Streamlit](https://streamlit.io) for analyzing network KPIs such as:

- 📉 Packet Loss
- ⏱️ Round Trip Time (RTT)
- 🔁 Jitter

## Live Features

- Upload CSV logs
- Visualize trends over time
- View packet loss, delay, and jitter all in one place

---

## Project Files

|         File               |                 Description                      |
|----------------------------|--------------------------------------------------|
| `packet_loss_dashboard.py` | Main Streamlit app                               |
| `packet_loss_log.csv`      | Sample KPI data (timestamp, sent, received, RTT) |

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/NajjarSamer/kpi_measurement.git
cd kpi_measurement

# 2. Install requirements
pip install -r requirements.txt

# 3. Run the app
streamlit run packet_loss_dashboard.py
