# 🎯 Debt Collector Performance Analysis - End-to-End ML Solution

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org/) [![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/) [![LightGBM](https://img.shields.io/badge/LightGBM-ML%20Model-orange.svg)](https://lightgbm.readthedocs.io/) [![Tableau](https://img.shields.io/badge/Tableau-Dashboard-purple.svg)](https://tableau.com/)

> **An intelligent debt collector performance classification system that transforms manual evaluation processes into data-driven insights using machine learning, feature engineering, and interactive web applications.**

## 🚀 Project Overview

This comprehensive project demonstrates expertise across the entire data science pipeline - from raw data analysis to production-ready machine learning deployment. The system automatically classifies debt collector performance into **High**, **Medium**, and **Low** categories with **95.34% accuracy** using advanced feature engineering and LightGBM classification.

### 🎯 Key Achievements

- **95.34% Model Accuracy** with LightGBM classifier
- **Automated Performance Classification** replacing manual evaluation
- **Interactive Web Application** with real-time predictions
- **Advanced Feature Engineering** creating performance-relevant metrics
- **Production-Ready Pipeline** with custom transformers
- **Interactive Tableau Dashboard** for comprehensive analytics

---

## 🔧 Technical Stack & Skills Demonstrated

### 📊 **Data Science & Analytics**

- **Exploratory Data Analysis** - Pattern discovery and statistical insights
- **Feature Engineering** - Custom rate-based performance metrics
- **Machine Learning** - Classification with ensemble methods
- **Model Evaluation** - Cross-validation, ROC analysis, feature importance

### 🤖 **Machine Learning Engineering**

- **Pipeline Development** - Custom transformers and preprocessing
- **Model Selection** - LightGBM, Random Forest, Decision Tree comparison
- **Hyperparameter Tuning** - Optimized model performance
- **Class Balancing** - SMOTENC for imbalanced datasets

### 🌐 **Web Development**

- **Flask Framework** - Full-stack web application
- **Interactive UI** - Form-based prediction interface
- **Data Visualization** - Matplotlib charts and radar plots
- **Database Integration** - SQLAlchemy ORM with MySQL

### 📈 **Business Intelligence**

- **Tableau Dashboard** - Executive-level performance analytics
- **KPI Monitoring** - Success ratios, contact rates, recovery metrics
- **Stakeholder Communication** - Clear, actionable insights

---

## 🖼️ Application Screenshots

### 🏠 **Homepage - Hero Section**

_Clean, professional interface introducing the debt collector performance analysis system_

![Homepage Hero](https://github.com/najeep24/debt-collector-performance-analysis/blob/d9b02afd2efd9f7ee5e96e56f72e445c6ed08bab/data/hiro-web.png)

### 📝 **Prediction Input Form**

_User-friendly form for entering collector performance data with intuitive field validation_

![Prediction Form](https://github.com/najeep24/debt-collector-performance-analysis/blob/d9b02afd2efd9f7ee5e96e56f72e445c6ed08bab/data/input-web.png)

### 📊 **Prediction Results & Analysis**

_Comprehensive results page featuring performance classification, detailed metrics analysis, and visual explanations_

![Prediction Results](https://github.com/najeep24/debt-collector-performance-analysis/blob/d9b02afd2efd9f7ee5e96e56f72e445c6ed08bab/data/result-1.png)
![Prediction Results-2](https://github.com/najeep24/debt-collector-performance-analysis/blob/d9b02afd2efd9f7ee5e96e56f72e445c6ed08bab/data/result-2.png)

### 📈 **Interactive Dashboard Analytics**

_Advanced analytics dashboard with drill-down capabilities and performance trend analysis_

![Dashboard Analytics](https://github.com/najeep24/debt-collector-performance-analysis/blob/65576856513b20a11fc8f93d38c7429585456d48/data/Screenshot%202025-09-23%20082446.png)

---

## 📚 Documentation Structure

### 📋 **Core Analysis Reports**

Navigate through comprehensive documentation covering every aspect of the project:

|Document|Description|Key Insights|
|---|---|---|
|**[Project Overview](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/00-project-overview-report.md)**|Problem statement, solution approach, success metrics|Manual → Automated evaluation transformation|
|**[Data Overview](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/01-data-overview-report.md)**|Dataset characteristics, feature descriptions, data quality|12,000 records, 17 features, 1-year timespan|
|**[Data Cleaning](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/02-data-cleaning-report.md)**|Preprocessing steps, outlier treatment, quality assurance|92.7% data retention after quality improvements|
|**[Exploratory Analysis](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/03-exploratory-analysis-report.md)**|Pattern discovery, correlation analysis, feature engineering|Key performance drivers identification|
|**[Model Development](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/04-modelling-evaluation-report.md)**|Algorithm comparison, hyperparameter tuning, evaluation|95.34% accuracy with LightGBM|

### 🚀 **Implementation Reports**

Detailed technical implementation and deployment documentation:

|Document|Focus Area|Technical Details|
|---|---|---|
|**[Deployment Report](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/05-model-deployment-report.md)**|Model serialization, pipeline deployment, production setup|Pickle serialization, Flask integration|
|**[Website Development](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/06-web-development-report.md)**|Web application architecture, features, future roadmap|Full-stack development, interactive features|
|**[Tableau Dashboard](https://github.com/najeep24/debt-collector-performance-analysis/blob/f33ebfdab08f035a4caa5ec6320fe3a7e9e595c5/docs/07-tableau-dashboard-report.md)**|Business intelligence dashboard, KPI visualization|Executive analytics, performance monitoring|

---

## ⚡ Quick Start Guide

### 1️⃣ **Clone & Setup**

```bash
git clone https://github.com/yourusername/debt-collector-performance-analysis.git
cd debt-collector-performance-analysis
pip install -r requirements.txt
```

### 2️⃣ **Database Configuration**

```bash
# Update config.py with your MySQL credentials
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dashboard_data'
```

### 3️⃣ **Run the Application**

```bash
python app.py
# Access at http://localhost:5000
```

### 4️⃣ **Make Predictions**

1. Navigate to `/predict`
2. Fill in collector performance data
3. Get instant classification with detailed analysis
4. View performance metrics and recommendations

---

## 🔬 Model Performance Highlights

### 🎯 **Classification Results**

```
Model: LightGBM with Feature Engineering
Accuracy: 95.34%
Cross-Validation: 95.42% (±0.5%)

Class Performance:
├── Low Performance:    Precision 0.96, Recall 0.97, F1 0.97
├── Medium Performance: Precision 0.96, Recall 0.95, F1 0.95
└── High Performance:   Precision 0.95, Recall 0.95, F1 0.95
```

### 📊 **Key Feature Importance**

1. **RPC Rate** (18.2%) - Right Party Contact effectiveness
2. **Recovery Rate** (17.3%) - Debt collection efficiency
3. **PTP Rate** (16.3%) - Promise-to-Pay conversion success
4. **Total Contact** (9.9%) - Contact frequency impact
5. **Call to PTP** (8.8%) - Conversion effectiveness

---

## 🤝 Technical Architecture

### 🏗️ **System Components**

```
debt-collector-performance-analysis/
├── 📊 Data Analysis & ML
│   ├── notebooks/           # Jupyter analysis notebooks
│   ├── data/               # Raw and processed datasets
│   └── models/             # Trained model artifacts
├── 🔧 ML Pipeline
│   ├── transformers/       # Custom feature transformers
│   ├── services/          # Prediction and business logic
│   └── saved_pipeline.pkl # Production model
├── 🌐 Web Application
│   ├── templates/         # HTML templates
│   ├── static/           # CSS, JS, images
│   └── routes.py         # Flask routing logic
└── 📚 Documentation
    └── docs/             # Comprehensive project reports
```

### 🔗 **Integration Points**

- **MySQL Database** - Data storage and retrieval
- **Flask Web Framework** - User interface and API
- **Tableau Server** - Business intelligence dashboard
- **Python ML Pipeline** - Model training and inference

---

## 📈 Business Impact

### 💼 **Value Proposition**

- **⚡ 80% Faster Evaluation** - Automated vs manual assessment
- **🎯 Objective Performance Metrics** - Data-driven, consistent evaluations
- **💡 Actionable Insights** - Specific improvement recommendations
- **📊 Strategic Decision Support** - Performance trend analysis
- **🔄 Scalable Solution** - Handles growing collector teams

### 🎯 **Success Metrics Achieved**

- ✅ **Model Accuracy > 75%** (Achieved: 95.34%)
- ✅ **Precision, Recall, F1 > 80%** (Achieved: 95%+ across all classes)
- ✅ **Feature Importance Identification** (Top 5 drivers identified)
- ✅ **Production Deployment** (Web application with real-time predictions)

---

## 👨‍💻 About This Project

This end-to-end machine learning project showcases comprehensive data science capabilities from initial data exploration through production deployment. The solution demonstrates expertise in:

- **🔍 Data Analysis** - Advanced EDA and statistical insights
- **🤖 Machine Learning** - Feature engineering and model optimization
- **🏗️ MLOps** - Pipeline development and model deployment
- **🌐 Full-Stack Development** - Web application with interactive UI
- **📊 Business Intelligence** - Dashboard creation and stakeholder communication

**🎯 Demonstrating:** Data Science portfolio, Machine Learning engineering skills, End-to-end project development, Business problem-solving through analytics

---

## 📞 Contact & Collaboration

**🔗 Connect with me:**

- **LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/nazhivali/)
- **Email:** nazhiv.ash@gmail.com
- **Portfolio:** [Portfolio link](https://www.notion.so/Portfolio-26eaa97018ea80d2b4a7c435b72f5950?source=copy_link)

**💬 Let's discuss:** Machine Learning projects, Data Science collaboration, Business analytics solutions

---

_⭐ If you found this project valuable, please consider starring the repository and sharing it with others interested in data science and machine learning applications!_
