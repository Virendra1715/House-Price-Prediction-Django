# 🏠 House Price Prediction using Machine Learning & Django

A complete end-to-end Machine Learning web application developed using **Python, Django, Scikit-learn, Pandas, NumPy, HTML, CSS, and Bootstrap**. The application predicts house prices based on user-input property features through an intuitive web interface.

---

# 📌 Project Overview

This project demonstrates the complete Machine Learning lifecycle, from data preprocessing to web deployment. A trained Random Forest Regression model is integrated into a Django web application, allowing users to estimate house prices by entering property details.

The project also includes user authentication and prediction history, making it a complete full-stack Machine Learning application.

---

# ✨ Features

- User Registration
- User Login & Authentication
- Secure Logout
- House Price Prediction
- Prediction History
- Django Admin Panel
- Machine Learning Model Integration
- Responsive Bootstrap UI
- SQLite Database Integration

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

## Backend

- Django

## Frontend

- HTML5
- CSS3
- Bootstrap 5

## Database

- SQLite3

---

# 📂 Project Structure

```
House-Price-Prediction-Django/
│
├── house_predict/
│
├── house_price/
│   ├── ml_model/
│   │   ├── kc_house_data.csv
│   │   ├── predict.py
│   │   └── model_columns.pkl
│   │
│   ├── templates/
│   ├── static/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Virendra1715/House-Price-Prediction-Django.git
```

### Navigate into the Project

```bash
cd House-Price-Prediction-Django
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# 🤖 Machine Learning Model

The project uses a **Random Forest Regression** model trained on the **KC House Price Dataset** to predict house prices.

The trained model learns relationships between different housing features and predicts the estimated selling price for unseen data.

---

# 📁 Trained Model

The trained model file **house_price_model.pkl** is **not included** in this repository because GitHub does not allow files larger than **100 MB**.

To run this project successfully, generate the model by training it on the provided dataset.

After training, place the generated model inside:

```
house_price/ml_model/
```

Required files:

```
house_price/ml_model/
│
├── house_price_model.pkl
├── model_columns.pkl
└── kc_house_data.csv
```

---

# 📊 Dataset

Dataset Used:

**KC House Price Dataset**

The dataset contains various house features including:

- Bedrooms
- Bathrooms
- Floors
- Living Area
- Lot Area
- Year Built
- Location Features
- House Condition
- House Grade
- Waterfront
- View
- Renovation Details

---

# 📸 Application Screenshots

## Home Page

(Add Screenshot Here)

---

## Prediction Page

(Add Screenshot Here)

---

## Prediction Result

(Add Screenshot Here)

---

## Login Page

(Add Screenshot Here)

---

## Register Page

(Add Screenshot Here)

---

## Prediction History

(Add Screenshot Here)

---

# 🔮 Future Improvements

- Multiple Machine Learning Algorithms
- Model Performance Comparison
- Data Visualization Dashboard
- REST API Support
- Docker Deployment
- Cloud Deployment (AWS / Azure / Render)
- User Profile Management

---

# 📚 Libraries Used

- Django
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Bootstrap

---

# 👨‍💻 Author

**Virendra Sharma**

Artificial Intelligence & Data Science Student

GitHub:

https://github.com/Virendra1715

---

# ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---

## License

This project is intended for educational and learning purposes.
