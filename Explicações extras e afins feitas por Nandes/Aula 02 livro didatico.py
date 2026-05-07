# Para trocar um valor no print sem precisar por a variavel
d = 5.385
msg = "um dólar vale %f reais."
print(msg %d)

# o "%d" vai pro lugar do "%f", ex com 2 valores
d = 5.385
msg2 = "Um dólar vale %f reais e um real vale %f dólar."
print(msg2 % (d, 1/d))

# Soma Infinita 
print ("Digite os valores a somar seguidos de [ENTER].")
print ("Para encerrar apenas [ENTER].")
total = 0
while 1: # Esse 1 signifca verdadeiro
    try:
        n = float(input(':'))
        total = total + n
    except:
        break #Um erro irá acontecer quando algum conteúdo digitado não puder ser convertido em float, por isso o ENTER, para quebrar o loop
print ("TOTAL: ", total)

# Listas
# A primeira posição é sempre zero
L = [4, "computador", [9, 8, 7], "Python", 11.5]
print(L[1])
# Saida = Computador
print(L[2])
# Saida = [9,8,7]
print(L[2][0])
# Saida = 8, entrou na lista dentro da lista e puxou a posição 0

# Atribuição por indice
L[2] = "Programação"
print(L)
# Mudei de [9, 8, 7] para "Programação"

# Funções para lista
# len = retorna o tamanho da lista
L = [1, 2, 3, 4]
len(L)
# Saida = 4

# min = retorna o menor valor da lista
L = [10, 20, 30, 40]
min(L)
# Saida = 10
  
# max = retorna o maior valor da lista
L = [10, 20, 30, 40]
max(L)
# Saida = 40

# sum = retorna a soma dos elementos da lista
L = [10, 20, 30]
sum(L)
# Saida = 60

# append = adiciona um valor ao final da lista
L = [1, 2, 3]
L.append(50)
# Saida = [1, 2, 3, 50]

# insert = adiciona um novo valor no inicio lista ou na posição selecionada
L = [1, 2, 3]
L.insert(1,50)
# Saida = [1, 50, 2, 3]

# remove = remove pelo valor
L = ["xoriça", "macarrão", "ovos"]
L.remove("ovos")
# Saida = [xoriça, macarrão]

# pop() = remove o item 
ultimoElemento = L.pop()
# Remove o ultimo elemento  
removeItem = L.pop(0)
# Remove pelo indice

# clear() = limpa toda a lista
L.clear()

# del = remove um elemento da lista pelo indice
L = [1, 2, 3, 4]
del L(1)
# Saida = [1, 3, 4]

# sort() = ordena em ordem decrescente 
L = [3, 5, 1, 4, 0, 6, 2]
L.sort()
# Saida = [0, 1, 2, 3, 4, 5, 6]
 
# reverse inverte os elementos de uma lista
L = [3, 5, 1, 4, 0, 6, 2]
L.reverse()
# Saida = [2, 6, 0, 4, 1, 5, 3]

L = [5, 7, 2, 9, 4, 1, 3]
print("Lista = ",L)
print("O tamanho da lista é ",len(L))
print("O maior elemento da lista é ",max(L))
print("O menor elemento da lista é ",min(L))
print("A soma dos elementos da lista é ",sum(L))
L.sort()
print("Lista em ordem crescente:",L)
L.reverse()
print("Lista em ordem decrescente:",L)

# inserção automatica em lista com loop
lista = []

for i in range(10):
    lista.append(i + 1)

print(lista)

# verificação com in e not in
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
# A saida vai ser true ou false

# Funções
# Usada quando precisamos repetir uma parte do codigo muitas vezes

def suporte():
    print(f"Suporte Técnico\nVocê pode entrar em contato por:\nE-mail:xxx@y.com\nTelefone: 99999-9999\nService Desk: www.servicedesk.www.ww")

ajuda = float(input("Se você precisa de ajuda digite 1: "))
if ajuda == 1:
    suporte()
else:
    print("Obrigado pelo contato")

# Funções com parametros, ex simples
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("James", "Bond")
introduction("Clark", "Kent")
# Parametros são os valores que a gente vai passar pra função quando chamar ela
# ex 1
def soma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
soma(5, 5, 6)

# ex 2
def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)
hi_everybody(["Adam", "John", "Lucy"])

# dicionario OBS* NOVO, DAR MAIS FOCO
# funciona da mesma maneira que um dicionário bilíngue.
fones = {'Farmacia' : 5551234567, 'Pizzaria' : 22657854310, 'Trabalho' :
5314653516 }
locais = ['Farmacia', 'Mercado', 'Trabalho']

for local in locais:
    if local in fones:
        print(local, "->", fones[local] )
    else:
        print(local, "não está nos registros")
        