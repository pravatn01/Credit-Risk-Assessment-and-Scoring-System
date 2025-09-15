# Credit Risk Assessment and Scoring System

A comprehensive machine learning system that predicts borrower default probability and converts these predictions into interpretable credit scores (300-900) with risk ratings. This end-to-end solution helps lenders make data-driven credit decisions through an interactive web application.

[Live demo — Deployed site](https://credit-risk-assessment-and-scoring-system-vu9h9vavphqyrhwnlexb.streamlit.app/)

## 🚀 Features

* **Predictive Modeling**: Machine learning models to estimate default probability
* **Credit Scoring**: Conversion of probabilities to standardized credit scores (300-900)
* **Risk Rating**: Categorical risk assessment (A through D)
* **Interactive Dashboard**: Real-time evaluation via Streamlit web app
* **Automated Feature Engineering**: Calculates key metrics like:

  * Loan-to-Income (LTI) ratio
  * Delinquency ratio
  * Average Days Past Due (DPD) per delinquency
* **Comprehensive Analytics**: Model evaluation with ROC/AUC, KS statistic, and Gini coefficient

## 📊 Model Performance

The optimized Logistic Regression model achieves:

* **AUC Score**: 0.98
* **Gini Coefficient**: 0.96
* **KS Statistic**: 85.98%

> *Note: reported metrics are results from experiments on the project dataset and may vary with different data or preprocessing.*

## 🛠️ Technical Implementation

### Data Processing Pipeline

* Automated data validation and cleaning
* Outlier detection and treatment
* Missing value imputation
* Multicolinearity handling with VIF analysis

### Feature Engineering

```python
# Key engineered features
df['loan_to_income'] = df['loan_amount'] / df['income']
df['delinquency_ratio'] = (df['delinquent_months'] * 100 / df['total_loan_months'])
df['avg_dpd_per_delinquency'] = np.where(
    df['delinquent_months'] != 0,
    df['total_dpd'] / df['delinquent_months'],
    0
)
```

### Model Development

* **Algorithms**: Logistic Regression, Random Forest, XGBoost
* **Class Imbalance Handling**: SMOTE-Tomek, Random Under Sampling
* **Hyperparameter Optimization**: Optuna and RandomizedSearchCV
* **Feature Selection**: Information Value (IV) and correlation analysis

## 📁 Project Structure

```
Credit-Risk-Assessment-and-Scoring-System/
├── artifacts/
│   └── model_data.joblib          # Saved model and preprocessing objects
├── dataset/
│   ├── customers.csv              # Customer demographic data
│   ├── loans.csv                  # Loan application data
│   └── bureau_data.csv            # Credit bureau information
├── streamlit_app.py               # Streamlit application
├── prediction_helper.py           # Prediction utility functions
├── credit_risk_model.ipynb        # Complete model development notebook
└── requirements.txt               # Python dependencies
```

## 🚀 Installation & Usage

1. **Clone the repository**

```bash
git clone https://github.com/pravatn01/Credit-Risk-Assessment-and-Scoring-System.git
cd Credit-Risk-Assessment-and-Scoring-System
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run streamlit_app.py
```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8501` or use the live demo link above.

## 💻 How to Use

1. **Input Borrower Information**: Enter demographic, financial, and credit history details
2. **Get Real-time Assessment**: The system instantly calculates:

   * Default probability
   * Credit score (300-900)
   * Risk rating (A, B, C, D)
3. **Interpret Results**: Use the visualizations to understand key factors influencing the decision

## 📈 Key Features in Production

* **Real-time Scoring**: Instant credit evaluation based on borrower inputs
* **Transparent Decisions**: Feature importance visualization explains scoring factors
* **Risk Segmentation**: Clear categorization of applicants by risk level
* **Data Validation**: Automated checks for input consistency and business rules
