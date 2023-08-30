# Exercício 01 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo: 
# Dólar Americano: R$4,91 
# Peso Argentino: R$0,02
# Dólar Australiano: R$3,18
# Dólar Canadense: R$3,64
# Franco Suiço: R$0,42
# Euro: R$5,36 
# Libra esterlina: R$6,21
"""n = float(input("Quanto dinheiro você tem? \nR$"))
dolar_americano = 4.91
conversao = n / dolar_americano
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))"""

# Simples (sempre trocando o valor da moeda)
"""valor = input("Digite o valor em reais: ")
print(f"Dolar Americano: {float(valor)/4.91}")"""

# Com dicionário
"""valor = input("Digite o valor em reais: ")
moedas = {
    "Dólar Americano": 4.91, 
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}
for moeda, valor_moeda in moedas.items():
    print(f"{moeda}: {float(valor)/valor_moeda}")"""

# Exercício 02 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado.
"""km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = float(input("Digite a quantidade de dias alugados: "))

custo_km = 0.20
custo_dia = 80.00
print(f"O valor a ser pago é: {(km_percorridos * custo_km) + (dias_alugados * custo_dia)}")"""


# Exercício 03 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Se o salário for até R$1000,00 o funcionário terá 20% de aumento. Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento. Acima de R$2801,00 o funcionário terá 5% de aumento.
"""salario = float(input("Digite o salário: "))
if salario <= 1000:
    print(f"O novo salário é: {salario*1.2}")
elif salario <= 2800:
    print(f"O novo salário é: {salario*1.1}")
else:
    print(f"O novo salário é: {salario*1.05}")"""
# 1.2 já é a somatória equivalente a 120%

# Exercício 04 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico. 
# Ex: n = leiaInt(‘Digite um n’)
"""def leiaInt():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Valor inválido!")

numero = leiaInt()
print(f"O número digitado foi: {numero}")"""
