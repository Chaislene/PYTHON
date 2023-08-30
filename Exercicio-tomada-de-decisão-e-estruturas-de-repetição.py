# Exercício 01 - Faça um Programa que peça dois números e imprima o maior deles.
"""numero1 = int(input('Primeiro número: '))

numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)"""


# Exercício 02 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""turno = input(
    "Digite seu turno, M - matutino, V - vespertino, N - noturno: "
).upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")"""


# Exercício 03 - Faça um Programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""nota = -1

while nota < 0 or nota > 10:
    nota = int(input("Informe a nota: "))

    if nota < 0 or nota > 10:
        print("Valor inválido")"""
