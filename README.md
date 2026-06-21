# 📊 Smart Forecast AI

## 🚀 Overview
Smart Forecast AI is a lightweight predictive analytics tool that transforms historical time-series data into actionable future insights. It enables users to forecast future values, detect anomalies, and simulate different scenarios with clear explanations.  

The project solves the limitation of relying only on historical data by allowing users to predict future trends, understand uncertainty, and make informed decisions. It is designed for analysts, students, and decision-makers who need fast, reliable, and interpretable forecasts without deep technical expertise.

---

## ✨ Features

- 📈 Time Series Forecasting using Prophet  
- 📊 Forecast range with lower and upper bounds (uncertainty visualization)  
- ⚖️ Baseline comparison using rolling average  
- ⚠️ Anomaly detection (detects spikes/dips outside expected range)  
- 🔮 Scenario simulation:
  - Growth scenario  
  - Conservative scenario  
  - Shock scenario (volatility-based)  
- 🧠 AI-generated explanations for non-technical users  
- 📊 Interactive dashboard using Chart.js  
- ✅ Model validation using MAPE (accuracy score)  
- 🧹 Robust data validation (handles missing values, sorting, duplicates)  

---

## 🛠️ Tech Stack

### Backend
- Python → core programming and data processing  
- Flask → lightweight web framework for handling requests and rendering UI  

### Data & Machine Learning
- Pandas → data cleaning and preprocessing  
- NumPy → numerical computations  
- Prophet → time-series forecasting with trend and seasonality  
- Scikit-learn → model validation using MAPE  

### Frontend
- HTML/CSS → UI design  
- Chart.js → interactive data visualization  

### Tools & Environment
- python-dotenv → environment variable management  
- cmdstanpy → backend engine for Prophet  

---

## 🧠 Technical Approach & Design Decisions

### Forecasting Model (Prophet)
Prophet is used because it handles trend and seasonality automatically, works well on small datasets, and requires minimal tuning.  
👉 Solves: complex parameter tuning and unstable predictions.

### Baseline Model (Rolling Average)
A rolling average provides a simple benchmark.  
👉 Solves: ensures the ML model adds value and avoids overfitting.

### Model Validation (MAPE)
MAPE gives error in percentage form, making it easy to interpret.  
👉 Solves: lack of clarity in prediction accuracy.

### Anomaly Detection
Detects values outside forecast confidence intervals.  
👉 Solves: identifies unusual spikes and drops.

### Scenario Simulation
- Growth → increases forecast  
- Conservative → smoothens trend  
- Shock → adds volatility  

👉 Solves: real-world uncertainty instead of single prediction.

### Explanation Engine
Generates human-readable insights using trend, anomalies, and accuracy.  
👉 Solves: improves usability for non-technical users.

---

## 📂 Project Structure

Smart-Forecast-AI/  
│  
├── app.py  
├── forecast.py  
├── baseline.py  
├── anomaly.py  
├── scenario.py  
├── explanation.py  
├── validation.py  
│  
├── data/  
│   └── sample_data.csv  
│  
├── templates/  
│   ├── index.html  
│   └── result.html  
│  
├── static/  
│   └── style.css  
│  
├── tests/  
│   └── test_forecast.py  
│  
├── .env.example  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation & Run Instructions

### 1. Clone the Repository
git clone https://github.com/bhavukm007/Smart-Forecast-AI.git  
cd Smart-Forecast-AI  

### 2. Create Virtual Environment
python -m venv venv  

Activate:  
Windows → venv\Scripts\activate  
Mac/Linux → source venv/bin/activate  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Setup Environment Variables
Create `.env` file:

FLASK_ENV=development  
FORECAST_PERIODS=30  

### 5. Run Application
python app.py  

### 6. Open in Browser
http://127.0.0.1:5000  

---

## 📊 Usage Examples

### Sample Input CSV
date,value  
2023-01-01,100  
2023-01-02,120  

### User Steps
1. Upload CSV file  
2. Select scenario (Growth / Conservative / Shock)  
3. Enter percentage (e.g., 10)  
4. Click Predict  

### Example Output (Simplified)
{
  "forecast": 150.2,
  "baseline": 140.0,
  "accuracy": 8.5,
  "anomalies": 2
}

### Internal Flow
POST /predict → Upload CSV → Process → Forecast → Dashboard  

---

## 📸 Dashboard Preview
<img width="1919" height="1031" alt="Screenshot 2026-04-12 080403" src="https://github.com/user-attachments/assets/f1e99f77-8036-41a4-b37c-88a1ea0949da" />


## 📸 Output Example
<img width="1918" height="1031" alt="Screenshot 2026-04-12 080429" src="https://github.com/user-attachments/assets/05a3073a-3d4a-4de8-98e8-680a1e2d2a52" />


---

## 📊 Output Includes

- Forecast values  
- Confidence intervals (upper/lower bounds)  
- Scenario-adjusted predictions  
- Detected anomalies  
- Accuracy score (MAPE)  
- AI-generated explanation  

---

## 🧠 System Architecture

User Input (CSV)  
        ↓  
Data Validation & Cleaning  
        ↓  
Forecast Model (Prophet)  
        ↓  
Baseline + Validation  
        ↓  
Anomaly Detection  
        ↓  
Scenario Simulation  
        ↓  
Explanation Engine  
        ↓  
Frontend Dashboard (Chart.js)  

👉 Modular pipeline ensures scalability and reliability.

---

## 🧹 Data Validation

- Checks required columns (date, value)  
- Converts date formats  
- Removes duplicates  
- Sorts data  
- Rejects missing values  
- Ensures minimum 10 rows  

---

## 🧪 Testing

Run tests:  
pytest  

Covers:  
- Baseline logic  
- Scenario logic  
- Anomaly detection  
- Model validation  

---

## ⚠️ Limitations

- Requires minimum 10 rows  
- Only supports time-series format  
- Prophet may be slow on large datasets  
- Scenario simulation is rule-based  
- No real-time streaming  

---

## 🚀 Future Improvements

- Real-time forecasting  
- API endpoints  
- Advanced ML models (LSTM, XGBoost)  
- Better anomaly explanations  
- Cloud deployment  

---

## 🔐 Security

- No hardcoded secrets  
- Uses environment variables  
- `.env.example` provided  

---

## 📚 Learning Outcomes

- Time-series forecasting  
- Model validation  
- Handling uncertainty  
- Data pre-processing  
- Communicating insights  

---

## 👨‍💻 Author

Bhavuk Mahajan  
Thapar Institute of Engineering and Technology  

---

## 📄 License

Open-source and compatible with Apache 2.0 and DCO requirements.
