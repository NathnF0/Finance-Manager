# 💰 Finance Manager

A simple **Personal Finance Manager** built with **Python**, allowing users to create accounts and track their financial transactions.

---

## 🚀 Features

✔ User registration
✔ User login system
✔ Add income transactions
✔ Add expense transactions
✔ View transaction history
✔ Calculate current balance
✔ Financial report by category
✔ Data stored automatically using JSON files

Each user has their **own financial history and data file**.

---

## 🔗 Repository

Project repository:

```
https://github.com/NathnF0/Finance-Manager
```

---

## 🧠 How It Works

The system generates two types of files:

* `users.json` → stores registered users
* `username_data.json` → stores financial data for each user

Example:

```
joao_data.json
maria_data.json
```

These files are **ignored by Git** and are not uploaded to the repository thanks to `.gitignore`.

---

## 📦 Technologies Used

* Python 3
* JSON
* CLI (Command Line Interface)

---

## 🖥️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/NathnF0/Finance-Manager.git
```

### 2️⃣ Enter the project folder

```
cd Finance-Manager
```

### 3️⃣ Run the program

```
python PersonalFinanceManager.py
```

---

## 📂 Project Structure

```
Finance-Manager
│
├── PersonalFinanceManager.py
├── README.md
└── .gitignore
```

---

## 🔒 Data Privacy

User data files are ignored by Git:

```
users.json
*_data.json
```

This ensures that **no user data is uploaded to the repository**.

---

## 💡 Future Improvements

* Graphical User Interface (GUI)
* Financial dashboard
* Expense charts
* Export reports (CSV / Excel)
* Web version

---

## 👨‍💻 Author

This project was developed as a **learning project** to practice and improve programming skills using Python.

Its purpose is educational, focusing on concepts such as:

* Python programming
* File handling
* JSON data storage
* Basic authentication systems
* Program structure and logic

The project is part of a personal learning journey in **software development and computer science**.
