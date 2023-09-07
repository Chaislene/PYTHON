# Exercício 01 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""def soma3(a, b, c):
    s = a + b + c
    return s


print('SOMA DE TRÊS NÚMEROS')
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print('Soma = ', soma3(a, b, c))"""


# Exercício 02 - "Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127->721. 
"""def reverso(n):
    return str(n[::-1])

n = str(input('Digite um número: ')).strip()
print(f'Reverso: {reverso(n)}')"""

# Exercício 03 - Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta. 
"""def celsiusfahrenheit(grausC):
    return (grausC * 9/5) + 32

def fahrenheitCelsius(grausF):
    return (grausF - 32) * 5/9

def menu():
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    escolhido = input("Digite o número da opção desejada: ")
    return escolhido

escolhido = menu()

if escolhido == "1":
    grausC = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsiusfahrenheit(grausC)
    print(f'Valor em Fahrenheit: {fahrenheit}°F')
elif escolhido == "2":
    grausF = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheitCelsius(grausF)
    print(f'Valor em Celsius: {celsius}°C')
else:
    print("Opção inválida")"""
