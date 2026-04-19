from flask import Flask, render_template, request
import re

app = Flask(__name__)

# -------- TOKENIZER --------
def tokenize(expression):
    token_specification = [
        ('NUMBER',   r'\d+'),
        ('ID',       r'[A-Za-z]+'),
        ('OP',       r'[+\-*/=]'),
        ('SKIP',     r'[ \t]'),
        ('MISMATCH', r'.'),
    ]

    tokens = []
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

    for mo in re.finditer(tok_regex, expression):
        kind = mo.lastgroup
        value = mo.group()

        if kind != 'SKIP':
            tokens.append((kind, value))

    return tokens

# -------- TAC --------
def generate_TAC(tokens):
    stack = []
    output = []
    temp_count = 1

    precedence = {'+':1, '-':1, '*':2, '/':2}
    operators = []
    postfix = []

    for token in tokens:
        if token[0] in ('ID', 'NUMBER'):
            postfix.append(token[1])
        elif token[1] == '=':
            continue
        elif token[1] in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[token[1]]):
                postfix.append(operators.pop())
            operators.append(token[1])

    while operators:
        postfix.append(operators.pop())

    for symbol in postfix:
        if symbol not in "+-*/":
            stack.append(symbol)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            temp_count += 1
            output.append(f"{temp} = {op1} {symbol} {op2}")
            stack.append(temp)

    lhs = tokens[0][1]
    output.append(f"{lhs} = {stack.pop()}")

    return output

# -------- ROUTES --------
@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    tokens = []

    if request.method == 'POST':
        expr = request.form['expression']
        tokens = tokenize(expr)
        result = generate_TAC(tokens)

    return render_template('index.html', tokens=tokens, result=result)

if __name__ == '__main__':
    app.run(debug=True)