# Exercício 01 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 
"""ALUNOS = 10
NOTAS = 4

medias = []
media_sete = 0

for i in range(ALUNOS):
    media = 0
    for j in range(NOTAS):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= NOTAS
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\nA média dos alunos foi:")
for i in range(ALUNOS):
    print(f"Aluno {i+1}: {medias[i]}")

print(f"\n{media_sete} alunos tiveram média maior ou igual a 7.")"""


# Exercício 02 - Programa nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. 
"""nome = str(input('Digite o seu nome: '))
print(nome[::-1].upper())"""


# Exercício 03 - Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim, imprima True. Caso contrário, imprima Falso. 
"""dicionario = {"banana": 'fruta', "casa": '', "laranja": 'fruta'}
print(dicionario)
# Verifica se todos os valores no dicionário são emitidos
valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print("True")
else:
    print("False")"""



# Exercício 04 - "Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
# ""Telefonou para a vítima?"" 
# ""Esteve no local do crime?"" 
# ""Mora perto da vítima?"" 
# ""Devia para a vítima?"" 
# ""Já trabalhou com a vítima?"" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será classificado como ""Inocente"". 
"""positivos = 0
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")"""
