# Mini Compiler for Arithmetic Expressions

## Features
- Lexical Analysis (Tokenization)
- Syntax Analysis
- Three Address Code Generation
- Simple Web UI using Flask

## Example
Input: a = b + c * d  
Output:
t1 = c * d  
t2 = b + t1  
a = t2  

## Run Project
pip install flask  
python app.py