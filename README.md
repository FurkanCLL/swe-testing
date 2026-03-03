# Quick-Calc

Quick-Calc is a simple calculator application developed for the Advanced Software Engineering course.  
The application supports basic arithmetic operations including addition, subtraction, multiplication, division, and a clear function.

The main goal of this project is not the UI complexity, but demonstrating software testing principles, version control usage, and clean project structure.


## Features

- Addition
- Subtraction
- Multiplication
- Division (with division by zero handling)
- Clear (reset)


## Project Structure

- `engine.py` → core calculation logic  
- `controller.py` → handles user input and connects GUI with logic  
- `app.py` → GUI layer  
- `tests/` → unit and integration tests  


## Setup Instructions

1. Clone the repository:
```
git clone https://github.com/FurkanCLL/swe-testing.git
cd swe-testing
```

2. Create virtual environment:
```
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
## Run Application
```
python -m src.quick_calc.app
```
## Run Tests
```
pytest
```


## Testing Framework Research

For this project, Pytest was chosen as the testing framework.

Two common Python testing frameworks are:

### 1. unittest
- Built into Python standard library  
- More verbose syntax  
- Class-based structure  
- Good for traditional structured test cases  

### 2. pytest
- Simpler and more readable syntax  
- Uses plain functions  
- Better error reporting  
- Easier to write parameterized tests  

Pytest was selected because of its simplicity and cleaner syntax, which makes writing and maintaining tests easier for small and medium-sized projects.



#### Developed by Furkan Ciloglu | 231ADB104