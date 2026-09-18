# 💻 Laptop Price Predictor

A Machine Learning regression project that predicts laptop prices based on hardware specifications using Python, Scikit-learn, XGBoost, and Streamlit.

## 🚀 Features

- Data Cleaning and Feature Engineering
- CPU, GPU, RAM, Storage & OS Analysis
- PPI Calculation from Screen Resolution
- Multiple Regression Algorithms
- Streamlit Web Application
- Docker Containerization

## 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Docker
- Git & GitHub

## 🤖 Machine Learning Models

- Linear Regression
- Ridge & Lasso Regression
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting
- XGBoost
- Voting Regressor
- Stacking Regressor

## 📊 Model Performance

| Model | R² Score |
|---|---:|
| Random Forest | 0.8831 |
| XGBoost | 0.8964 |
| Voting Regressor | 0.8869 |
| Stacking Regressor | 0.8868 |

**Best recorded R² Score:** 0.8964 (XGBoost)

> Evaluation was performed on the log-transformed price target.

## 🖥️ Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/MohammedKaif1154/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit

```bash
streamlit run app.py
```

Open: `http://localhost:8501`

## 🐳 Run Using Docker

### Build Image

```bash
docker build -t laptop-price-predictor .
```

### Run Container

```bash
docker run -p 8501:8501 laptop-price-predictor
```

Open: `http://localhost:8501`

## 📌 Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Streamlit Application
      ↓
Docker Deployment
```

## 👤 Author

**Mohammed Kaif Shaikh**

GitHub: [MohammedKaif1154](https://github.com/MohammedKaif1154)