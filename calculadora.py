a = float(input('Entre com o primeiro número: '))
b = float(input('Entre com o segundo número: '))
soma = b + a
subtracao = a - b
<<<<<<< HEAD
multiplicacao = b*a
divisao = b/a
=======
multiplicacao = a*b
divisao = a/b
potencia = a**b
>>>>>>> e88844fc0c99be483848007f4e75640f73da0d1c
print(f'A soma é {soma}.')
print(f'A diferença é {subtracao}.')
print(f'A multiplicação é {multiplicacao}.')
print(f'A divisão é {divisao}.')
<<<<<<< HEAD
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
    
=======
print(f'A potência é {potencia}.')
>>>>>>> e88844fc0c99be483848007f4e75640f73da0d1c
