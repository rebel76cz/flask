from flask import Flask, render_template, request

app = Flask(__name__)

# Your calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

# Global variables for storing results and pairs
results_list = []
pairs_dict = {}

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        operation = request.form['operation']
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])

            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)

            pairs_dict[f'{num1} {operation} {num2}'] = result

            with open('results.txt', 'a') as f:
                f.write(f'{num1} {operation} {num2} = {result}\n')

        except ValueError as e:
            result = f"Error: {str(e)}"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)