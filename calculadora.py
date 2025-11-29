a = float(input('Entre com o primeiro número: '))
b = float(input('Entre com o segundo número: '))
soma = a + b
subtracao = a - b
multiplicacao = a*b
divisao = a/b
print(f'A soma é {soma}.')
print(f'A diferença é {subtracao}.')
print(f'A multiplicação é {multiplicacao}.')
print(f'A divisão é {divisao}.')
print(f'A porcentagem é {porcentagem}')
from flask import Flask, render_template, request

app = Flask(__name__)

# Rota inicial -> carrega a página HTML
@app.route("/")
def index():
    return render_template("index.html")

# Rota que processa dados do frontend
@app.route("/somar", methods=["POST"])
def somar():
    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])
    resultado = n1 + n2
    return f"O resultado da soma é: {resultado}"

if __name__ == "__main__":
    app.run(debug=True)
    