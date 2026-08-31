# 🎓 Student Record System

A simple and practical **Student Record Management System** developed in Python.
The project is designed as a console-based application that allows users to manage
student information efficiently.

---

## 📌 Project Overview

The Student Record System helps maintain basic student information such as:

- Student ID
- Name
- Age
- Program
- Marks
- Grade

The application provides a simple menu-driven interface where users can add,
view, search, update, and delete student records.

Student data is stored locally in a **JSON file**, allowing records to remain
available even after the program is closed.

---

## ✨ Features

### 👤 Student Management
- Add new student records
- View all student records
- Search students by ID or name
- Update existing records
- Delete student records

### 📊 Academic Features
- Enter marks between 0 and 100
- Automatically calculate grades
- Calculate class average
- Display highest-scoring student
- Calculate overall pass rate

### 💾 Data Storage
- Uses JSON for local data storage
- Automatically creates the data file
- Records remain saved between program sessions

### 🛡️ Input Validation
- Prevents empty inputs
- Validates marks
- Prevents duplicate student IDs
- Handles invalid numerical input

---

## 🛠️ Technologies Used

- **Python 3**
- JSON
- File Handling
- Lists & Dictionaries
- Functions
- Exception Handling
- Object-independent modular programming

No external Python packages are required.

---

## 📂 Project Structure

```text
Task-1-Student-Record-System/
│
├── student_record_system.py
├── students.json
└── README.md# Student_Record_System
