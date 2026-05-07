nome = str(input("Digite o nome do Aluno: "))
idade = int(input("Digite a idade do Aluno: "))

somaNotas = 0.0
for i in range(1, 5):
    nota = float(input(f"Digite a {i}. nota: "))
    somaNotas += nota

mediaNotas = somaNotas / 4

if mediaNotas >= 7:
    print("="*30)
    print(f" Aluno: {nome} - Idade: {idade}")
    print(f" Parabéns pela aprovação com média {mediaNotas}!")
    print("-"*30)
elif mediaNotas < 7 and mediaNotas > 5:
    print("="*30)
    print(f" Aluno: {nome} - Idade: {idade}")
    print(f" Ficou de recuperação com média {mediaNotas}!")
    print("-"*30)
else:
    print("="*30)
    print(f" Aluno: {nome} - Idade: {idade}")
    print(f" Reprovado com média {mediaNotas}!")
    print("-"*30)