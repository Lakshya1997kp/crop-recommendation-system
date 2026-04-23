# 🌱 Crop Recommendation System

This project is a simple web application that helps users decide which crop to grow based on soil conditions.
It combines a **machine learning model** with a **Flask backend** and a **MySQL database** to create a complete end-to-end system.

The idea is straightforward:
you enter values like soil nutrients → the model predicts the most suitable crop.

---

## 🚀 What this project does

* Lets users **create an account and log in**
* Uses **sessions** to keep users logged in
* Takes soil input values from the user
* Runs a **machine learning model** on those inputs
* Displays the **recommended crop on the same page**

---
## 📊 Monitoring & Scaling

As part of deployment experimentation, basic observability and scaling concepts were explored:

* Integrated **Prometheus** for collecting application and system metrics
* Used **Grafana** to visualize metrics through dashboards
* Configured **Horizontal Pod Autoscaler (HPA)** in Kubernetes to experiment with auto-scaling based on resource usage

This helped in understanding how real-world systems monitor performance and handle varying loads.
(currently it is not live)


## 🛠️ Tech used

**Backend:**

* Flask
* MySQL
* mysql-connector-python

**Frontend:**

* HTML (with Jinja templates)

**Machine Learning:**

* scikit-learn
* NumPy
* Pickle (for saving/loading the model)

---

## 📁 Project structure

```
project/
│
├── app.py
├── model.pkl
|── db.py
|── auth_service.py
├── user_service.py
├── model_utils.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── prediction.html
│
├── static/
│   └── (CSS and background pictures)
│
└── README.md
```

---

## ⚙️ How to run this project

### 1. Clone the repo

```bash
git clone https://github.com/Lakshya1997kp/crop-recommendation-app.git
cd crop-recommendation-app
```

---

### 2. Install dependencies

```bash
pip install flask mysql-connector-python numpy scikit-learn
```

---

### 3. Setup the database

Open MySQL and run:

```sql
CREATE DATABASE crop_recommendation_app;

USE crop_recommendation_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
```

---

### 4. Add your database credentials

In your Flask code, update:

```python
host="localhost"
user="root"
password="your_password"
database="crop_recommendation_app"
```

---

### 5. Run the app

```bash
python app.py
```

Then open your browser and go to:
http://127.0.0.1:5000

---

## 🔄 How it works (flow)

1. User signs up
2. Logs in
3. A session is created
4. User goes to prediction page
5. Enters values (like N, P, K)
6. Flask sends data to ML model
7. Model predicts crop
8. Result is shown on the same page

---

## 🧠 About the model

The model takes numerical inputs like:

* Nitrogen
* Phosphorus
* Potassium
  (and other features if included)

It was trained separately and then saved using `pickle`, which is loaded inside the Flask app.

---

## 🔐 Security stuff (basic but important)

* Passwords are **hashed** (not stored as plain text)
* SQL queries use **parameterized queries** (prevents SQL injection)
* Sessions are used to restrict access to prediction page

---

## 🧪 What I learned from this project

* How Flask handles routing and requests (GET/POST)
* How to connect Flask with MySQL
* How authentication systems work (login/signup/session)
* How to integrate an ML model into a web app
* Why backend validation and security matter

---

## 🚧 Possible improvements

* Add better UI (CSS/JS)
* Add real-time validation using JavaScript
* Store user prediction history
* Use SQLAlchemy instead of raw SQL

---

## 👨‍💻 Author

Lakshya Kumar Pandey

---

## ⭐ If you found this useful

Feel free to star the repo or use it as a base for your own projects!
 📁 Project structure
        
