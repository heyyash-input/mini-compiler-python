# Mini Compiler for Arithmetic Expressions

A simple web-based mini compiler built using **Python Flask** that performs lexical analysis and generates **Three Address Code (TAC)** for basic arithmetic expressions.

This project demonstrates basic compiler design concepts such as tokenization, operator precedence handling, and intermediate code generation through a simple web interface.

---

## Features

- Lexical analysis / tokenization
- Supports identifiers, numbers, operators, and assignment expressions
- Handles arithmetic operators:
  - Addition `+`
  - Subtraction `-`
  - Multiplication `*`
  - Division `/`
- Generates Three Address Code
- Simple Flask-based web interface
- Beginner-friendly compiler design project

---

## Tech Stack

- Python
- Flask
- HTML
- Jinja2 Template Engine

---

## Project Structure

```text
mini-compiler-python/
│
├── app.py
├── README.md
└── templates/
    └── index.html
```

## How It Works

The project works in two main phases:

### 1. Lexical Analysis

The input expression is broken into tokens.

Example input:
```
a = b + c * d
```
Generated tokens:
```
[('ID', 'a'), ('OP', '='), ('ID', 'b'), ('OP', '+'), ('ID', 'c'), ('OP', '*'), ('ID', 'd')]
```
### 2. Three Address Code Generation

The expression is converted into intermediate code using temporary variables.

Example output:
```
t1 = c * d
t2 = b + t1
a = t2
```

### Example
Input
```
a = b + c * d
```
Output
```
t1 = c * d
t2 = b + t1
a = t2
```

### Installation and Setup
1. Clone the repository
```
git clone https://github.com/rujularaut/mini-compiler-python.git
```
2. Move into the project folder
```
cd mini-compiler-python
```
3. Install Flask
```
pip install flask
```
4. Run the project
```
python app.py
```
5. Open in browser

After running the project, open:
```
http://127.0.0.1:5000/
```

## Usage
Enter an arithmetic expression in the input box.
Click on the compile button.
View the generated tokens.
View the generated Three Address Code.

Example expression:
```
x = a + b * c
```
Expected output:
```
t1 = b * c
t2 = a + t1
x = t2
```

Supported Input Format

The project currently supports simple assignment expressions like:
```
a = b + c
x = a + b * c
result = x / y + z
```

### Limitations
Parentheses are not currently supported.
Only basic arithmetic operators are supported.
Error handling for invalid expressions is limited.
Variables are expected to be alphabetic identifiers.
The project is intended for learning basic compiler design concepts.

### Future Enhancements
Add support for parentheses
Improve syntax error handling
Add support for floating-point numbers
Add a better styled user interface
Add syntax tree generation
Add support for more complex expressions

### Author

Originally developed by heyyash-input
.

Documentation update contributed by rujularaut
.