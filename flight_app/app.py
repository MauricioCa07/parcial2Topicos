from flask import Flask

app = Flask(__name__)

def factorial(n):
    if n < 0:
        return None  
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@app.route('/factorial_main/<int:num>')
def factorial_main(num):
    resultado = factorial(num)
    if resultado is None:
        return "El factorial no está definido para números negativos", 400
    else:
        return f"El factorial de {num} es {resultado}"


if __name__ == '__main__':
    app.run(debug=True)
