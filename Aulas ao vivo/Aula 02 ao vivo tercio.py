# Estruturas de dados em python
# Lista = forma de ordenar dados em sequencia
# Dicionario = Dados organizados por chaves

# Listas:
compras = ["Maça", "Leite", "Pão", "Ovos"]

# Em python podemos por + de um tipo de dados na lista
mistura = ["João", 25, True, 1.82]

# Indexização
# Cada tem um endereço/indice iniciando no zero
print(compras[0])
# Saida = maçã
print(compras[-1])
# Truque em python para printar o ultimo elemnto em vez de fazer print(compras[3])
# Util quando você não sabe quantos elementos tem uma lista

# Slicing = Fatiamento
# Para pegar uma parte da lista
print(compras[1:3])
# OBS* tem que por um indice a + do que vc quer mostrar, pois o fim não é incluido, exemplo acima queria mostrar leite e pão mas se eu botasse de [1:2] ia mostrar so leite.
# Forma alt para slicing
print(compras[1:])
# Vai ate o ultimo indice
print(compras[::-1])
# Forma para inverter o slicing 

# Para mudar o elemento 
compras[1] = "Suco"

# Alterar com Slicing
compras[1:3] = ["Conguitos", "Café"]

# Print da alteração que fiz
print(f"Lista Modificada = {compras}")

# Dicionarios
# valor 1: chave, valor 2: valor
aluno = {
    "Nome": "Carlos", 
    "Idade": 20,
    "Curso": "Computação"
}
print(f"Nome do aluno = {aluno["Nome"]}")

# Mudar valor pela chave
aluno["Curso"] = "Engenharia"

# Adicionar informação, cria uma chave e um valor
aluno["nota_aluno"] = 10

# Se for varios valores a serem adicionados ou alterados
aluno.update({
    "Nome": "Joãozin",
    "Turma": "2B"
})
print(aluno)

# ESTUDAR GET EM DICIONARIO