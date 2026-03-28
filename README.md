# 🎓 Student Management System (Python + MySQL)

A simple **Student Management System** built using **Python** and **MySQL**.
This project performs basic **CRUD operations** (Create, Read, Update, Delete) through a command-line interface.

---

## 🚀 Features

* ➕ Add new student records
* ❌ Delete existing student records
* 🔄 Update student details
* 🔍 View a single student by roll number
* 📋 Display all student records
* ⚠️ Input validation (email & marks)
* 🛡️ Exception handling (duplicate entries, invalid input)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Library:** PyMySQL

---

## 🗄️ Database Schema

**Table Name:** `Student`

| Column   | Type        | Description           |
| -------- | ----------- | --------------------- |
| st_roll  | INT (PK)    | Unique Roll Number    |
| st_name  | VARCHAR(40) | Student Name          |
| st_email | VARCHAR(50) | Student Email         |
| st_marks | INT         | Student Marks (0–100) |

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install pymysql
```

---

### 2️⃣ Setup MySQL Database

* Open MySQL
* Create database:

```sql
CREATE DATABASE school;
```

---

### 3️⃣ Update Database Credentials

In the code, update:

```python
con = sq.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="school"
)
```

---

### 4️⃣ Run the Program

```bash
python main.py
```

---

## 📌 How It Works

* The program connects to MySQL
* Creates the `Student` table (if not exists)
* Displays a menu for user operations
* Performs database operations based on user input

---

## 🧠 Concepts Used

* Python basics (loops, conditionals, functions)
* Database connectivity (PyMySQL)
* SQL queries (INSERT, SELECT, UPDATE, DELETE)
* Exception handling
* Input validation

---

## 🔮 Future Enhancements

* 🌐 Convert to **Flask Web Application**
* 🖥️ Add **GUI using Tkinter**
* 🔐 Add **Login & Authentication**
* 📊 Add **Grade System & Analytics**

---

## 📷 Sample Output

```
Enter Your Choice-->
1.Add Student
2.Delete Student
3.Update Student
4.Display Student
5.Display All
6.Exit...
```

---

## 🤝 Contribution

Feel free to fork this repository and improve it!

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Abhay Pratap Singh**

---

⭐ If you like this project, don't forget to star the repository!
