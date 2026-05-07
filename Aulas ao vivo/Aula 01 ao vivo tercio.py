# Aula 01 Programação de Aplicativos
# Introdução Python

# Variaveis
# Python não é tão tipada, não preciso declarar o tipo
# nome = "Alice" ; String
# idade = 30 ; Inteiro
# altura = 1.75 ; Float Real
# vivo = true ; Boolean (V|F)
# Format = print(f"") para por variaveis dentro das aspas

# Tipos de dados e Operadores:
# Soma = +
# Subtração = -
# Multiplicação = *
# Divisão = /
# Exponenciação = **
# Modulo/Resto da divisão = %

# Operadores relacionais:
# maior que = >
# menor que = <
# maior ou igual = >=
# menor ou igual = <=
# igualdade = ==
# diferente = !=

# Operadores Logicos:
# E = and
# OU = or
# NÃO = not

# Estruturas de controles e Fluxo
# Condicionais e Loop de repetição

# Condicional
idadeCliente = 18

if idadeCliente >= 18:
    print("Venda de bebida alcoolica liberada!")
else:
    print("Venda Bloqueada. Cliente de menor.")

#input() comando para interagir
#elif serve para continuar o if, se a gente usasse outro if ia abrir outra condicional
pesquisa = int(input("Escreva sua nota de satisfação[0/10]:"))

if pesquisa < 5:
    print(f"Nota {pesquisa},Ruim")
elif pesquisa >= 5 and pesquisa <= 7:
    print(f"Nota {pesquisa}, Moderada")
else:
    print(f"Nota {pesquisa}, Excelente")

# Laço de repetição

nomes = ["Ana", "Pitchulo", "Dodril", "Moranguete"]
# For = Para do portugol

# "nome" é o contador
for nome in nomes:
    print(f"Olá {nome}! Bem-Vindo(a) ao supermercado do seu Zé!...")

opcao = 0
while opcao != 5:
    print("="*50)
    print("1 ---- SOMA")
    print("2 ---- SUBTRAÇÃO")
    print("3 ---- MULTIPLICAÇÃO")
    print("4 ---- DIVISÃO")
    print("5 ---- SAIR")
    print("="*50)

    opcao = int(input("Digite a Opção Desejada: "))

    n1 = int(input("Digite um valor inteiro: "))
    n2 = int(input("Digite outro valor:"))

    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")

    elif opcao == 2:
        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")

    elif opcao == 3:
        multi = n1 * n2
        print(f"{n1} * {n2} = {multi}")

    elif opcao == 4:
        divisao = n1 / n2
        print(f"{n1} / {n2} = {divisao}")

    elif opcao == 5:
        print("Obrigado por usar Nosso sistema!!")
        
    else:
        print("Opção Invalida!Tente novamente...")

