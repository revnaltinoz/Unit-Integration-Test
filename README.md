# 🛠️ Unit/Integration Testing 

This repository contains a simple Python application used for demonstrating **Unit Testing** and **Integration Testing**.

The application simulates a pricing pipeline that combines **business logic** (age/accident rules) and a **score adjustment** (driving score discount).

### 🧠 Why Do We Use Both Unit & Integration Tests?

- **Unit Tests** ensure each function works correctly in isolation and catches logic bugs early.
- **Integration Tests** validate that multiple components work together as expected and help catch system-level issues.

## 🚀 Repository Structure

| File | Purpose | Test Type Demonstrated |
| :--- | :--- | :--- |
| `insurance_calculator.py` | Contains the core business logic (`calculate_premium`) and the full pipeline logic (`calculate_final_quote`). 
| `test_unit.py` | Contains tests to check the **internal logic** of `calculate_premium` in isolation. | **Unit Tests** |
| `test_integration.py` | Contains tests to check the **full flow** and **communication** between data fetching and the final quote calculation. | **Integration Tests** |
| `README.md` | This file. | Instructions |

## ✅ How to Run the Tests

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are strictly required as we use the built-in `unittest` module.

### Step 1: Clone the Repository

Open your terminal or command prompt and clone this repository:

```bash
git clone https://github.com/revnaltinoz/Unit-Integration-Test.git
```

### Step 2: Navigate to the Project

```bash
cd Unit-Integration-Test
```

# Step 3: Install dependencies (

```bash
pip install -r requirements.txt
```

### Step 4: Run Unit Tests

```bash
pytest test_unit.py
```

### Step 5: Run Integration Tests

```bash
pytest test_integration.py
```

