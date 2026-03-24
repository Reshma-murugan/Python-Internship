# 🏦 Loan Approval Prediction

This project predicts whether a loan application will be **approved or rejected** using Machine Learning models.

---

## 📁 Project Structure

```
loan_approval/
│
├── loan_approval_dataset.csv
├── logistic_regression.ipynb
├── random_forest.ipynb
└── README.md
```

---

## 📊 Dataset

* Source: Kaggle
* Contains **4269 records** with financial and personal details
* Target variable: `loan_status` (Approved / Rejected)

---

## 🔧 Data Preprocessing

* Removed unwanted columns (`loan_id`)
* Handled invalid values (e.g., negative asset values)
* Filled missing values using **median**
* Encoded categorical variables:

  * education
  * self_employed
  * loan_status
* Checked for duplicates and cleaned data

---

## 🤖 Models Used

### 1. Logistic Regression

* Simple baseline model
* Accuracy: **~79.5%**

---

### 2. Random Forest Classifier

* Ensemble learning method
* Captures complex patterns
* Accuracy: **~97.8%**

---

## 📈 Model Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report (Precision, Recall, F1-score)

---

## 🔍 Key Insights

* **CIBIL score**, **income**, and **loan amount** are major factors
* Random Forest significantly outperformed Logistic Regression
* Slight overfitting observed but acceptable

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Open notebooks:

   * Logistic Regression → baseline model
   * Random Forest → improved model

---

## 💼 Project Highlights

* End-to-end ML pipeline
* Real-world financial dataset
* Model comparison and evaluation
* Ready for portfolio and interviews

---

## 📌 Future Improvements

* Feature engineering (loan-income ratio)
* Hyperparameter tuning
* Deployment using Streamlit

---

## 👨‍💻 Author

* Loan Approval ML Project by Reshma M

---
