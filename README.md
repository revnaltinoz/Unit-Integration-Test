# 🛠️ MLOps Testing Demo: Insurance Premium Calculator

This repository contains a simple Python application used for demonstrating **Unit Testing** and **Integration Testing** within an MLOps context.

The application simulates a pricing pipeline that combines **business logic** (age/accident rules) and a **Machine Learning score adjustment** (driving score discount).

## 🚀 Repository Structure

| File | Purpose | Test Type Demonstrated |
| :--- | :--- | :--- |
| `insurance_calculator.py` | Contains the core business logic (`calculate_premium`) and the full pipeline logic (`calculate_final_quote`). | Component under Test |
| `test_unit.py` | Contains tests to check the **internal logic** of `calculate_premium` in isolation. | **Unit Tests** |
| `test_integration.py` | Contains tests to check the **full flow** and **communication** between data fetching and the final quote calculation. | **Integration Tests** |
| `README.md` | This file. | Instructions |

## ✅ How to Run the Tests

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are strictly required as we use the built-in `unittest` module.

### Step 1: Clone the Repository

Open your terminal or command prompt and clone this repository:

```bash
git clone [YOUR_REPOSITORY_URL_HERE]

### Step 2: Navigate to the Project

```bash
cd mlops-testing-demo

### Step 3: Run Unit Tests

```bash
pytest test_unit.py

### Step 4: Run Integration Tests

```bash
pytest test_integration.py

