# 🏦 AI Loan Prediction Application

An AI-powered Loan Prediction Backend built with **Flask**, **MySQL**, **SQLAlchemy**, **JWT Authentication**, and **XGBoost Machine Learning**.

The application predicts whether a loan application is **Approved** or **Rejected** based on applicant and loan details.

---

# 🚀 Features

## 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- User Profile
- Change Password
- Logout
- Password Hashing

## 👤 Applicant Management
- Create Applicant
- Get Applicant
- Get All Applicants
- Update Applicant
- Partial Update Applicant
- Delete Applicant
- Search
- Pagination
- Sorting

## 💰 Loan Management
- Create Loan Application
- Get Loan
- Get All Loans
- Update Loan
- Partial Update Loan
- Delete Loan
- Search
- Pagination
- Sorting

## 🤖 AI Prediction
- XGBoost Machine Learning Model
- Predict Loan Approval
- Prediction History
- Delete Prediction

## 📊 Dashboard
- Total Users
- Total Applicants
- Total Loan Applications
- Total Predictions
- Approval Statistics

## 🛡 Security
- JWT Authentication
- Password Hashing
- Role-Based Authorization
- Request Validation
- Exception Handling

---

# 🛠 Technology Stack

### Backend

- Python
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Marshmallow
- MySQL
- SQLAlchemy

### Machine Learning

- XGBoost
- Pandas
- NumPy
- Scikit-Learn
- Joblib

### Testing

- Pytest

### Version Control

- Git
- GitHub

---

# 📁 Project Structure

```text
LoanPredictionApplication/

├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── models/
├── routes/
├── services/
├── schemas/
├── handlers/
├── utils/
├── tests/
│
├── ml/
│   ├── dataset/
│   ├── models/
│   ├── train_model.py
│   ├── evaluate.py
│   └── predict.py
│
└── static/
```

---

# 🗄 Database

Tables

- Users
- Applicant Profile
- Loan Application
- Prediction Result
- Model Details

---

# 🔑 Authentication

JWT Token based authentication.

Protected APIs require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 🤖 Machine Learning

Algorithm Used

- XGBoost Classifier

Prediction Output

- Approved
- Rejected

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/LoanPredictionApplication.git
```

## Open Project

```bash
cd LoanPredictionApplication
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙ Configure Environment

Create a `.env` file.

Example

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=LoanPredictionDB
DB_USER=root
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

---

# 🗄 Create Database

```sql
CREATE DATABASE LoanPredictionDB;
```

Execute

```
database/schema.sql
```

Optional

```
database/seed.sql
```

---

# ▶ Run Application

```bash
python app.py
```

---

# 🧪 Run Tests

```bash
pytest -v
```

### Test Result

```
23 Passed
0 Failed
```

---

# 📌 API Modules

- Authentication
- Applicant
- Loan
- Prediction
- Dashboard

---

# 📈 Future Enhancements

- React Frontend
- Admin Dashboard
- Charts & Analytics
- Email Notifications
- Docker Support
- CI/CD Pipeline
- Cloud Deployment
- Model Retraining

---

# 👨‍💻 Author

**Mohammad Aslam**

AI & Machine Learning Developer

---

# ⭐ GitHub

If you like this project, don't forget to ⭐ the repository.