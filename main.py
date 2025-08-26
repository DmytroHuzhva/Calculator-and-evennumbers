from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'dmytrohuzhva123'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/even', methods=['GET', 'POST'])
def even():
    if request.method == 'POST':
        even_value = request.form.get('even')
        if even_value and even_value.isdigit():
            even = int(even_value)
            if even % 2 == 0:
                message = f"Yes, number: {even} is even"
            else:
                message = f"No, number: {even} is odd"
            flash(message, "info")
        else:
            flash("Please enter a valid number", "error")
    return render_template('even.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        inp_calculator = request.form.get('inp_calculator')
        try:
            result = eval(inp_calculator, {"__builtins__": None}, {})
            flash(f"Result: {result}", "info")
        except Exception:
            flash("Invalid expression! Use only numbers and + - * /", "error")
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)
