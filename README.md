# 🌱 Crop Recommendation System

This project is a simple web application that helps users decide which crop to grow based on soil conditions.  
It combines a **machine learning model** with a **Flask backend** and a **MySQL database** to create a complete end-to-end system.

The idea is straightforward:  
you enter values like soil nutrients → the model predicts the most suitable crop.

---

## 🚀 What this project does

- Lets users **create an account and log in**
- Uses **sessions** to keep users logged in
- Takes soil input values from the user
- Runs a **machine learning model** on those inputs
- Displays the **recommended crop on the same page**

---

## 🛠️ Tech used

**Backend:**
- Flask
- MySQL
- mysql-connector-python

**Frontend:**
- HTML (with Jinja templates)

**Machine Learning:**
- scikit-learn
- NumPy
- Pickle (for saving/loading the model)

---
project/
│
├── app.py
├── model.pkl
├── templates/
│ ├── login.html
│ ├── register.html
│ └── prediction.html
│
├── static/
│ └── (optional CSS/JS)
│
└── README.md
## 📁 Project structure
        
