# Explicação das funções .get() e .join()
# O método .get() é uma ferramenta poderosa para manipular dicionários em Python, especialmente útil em tarefas de contagem ou frequências
# O método .get(chave, valor_padrao) tenta encontrar a chave dentro do dicionário.
# Temos 2 situações, se a chave existir ele retorna o valor guardado dentro dela, se não em vez de travar o programa com um erro (o temido KeyError), ele retorna o valor_padrao que você definiu.
# EX:
#contagem_generos = {}
#for filme in catalogo:
#    genero = filme["genero"]
#    contagem_generos[genero] = contagem_generos.get(genero, 0) + 1
    
# USADO EM OUTRO CODIGO *****

# .join(): O método .join() é uma ferramenta de manipulação de strings em Python, ele une vários elementos de um iterável (como uma lista ou tupla) em uma única string, utilizando um separador específico.
# EX: Isso transforma uma lista como ['001', 'França', 'Médico'] na string "001,França,Médico" apenas usando o ",".join(el)

ble =[" *", " * *", " * *", " * *", "*** ***"," * *", " * *", " *****"]
print("\n".join(ble))
# Entre aspas a gente escolhe o separador e dps define aonde vai ser feito o .join

# .strip(): O método .strip() é uma função nativa do Python utilizada para manipular strings, com o objetivo principal de remover caracteres indesejados do início e do fim de um texto
# Basicamente deixa o dado puro, sem espaços, tabulação ou quebra de linha, você tambem pode escolher exatamente o que tirar
# Por exemplo, ao processar dados estatísticos que contêm o símbolo de porcentagem, você pode usar x.strip('%')
# Evita que o programa falhe se o usuario apertar a barra de espaço por acidente antes ou depois de escrever o nome de um filme.

# .items():  É um método exclusivo do tipo de dado Dicionário (dict) Ele serve para "desempacotar" o conteúdo do dicionário, permitindo que você acesse a Chave e o Valor simultaneamente em um laço de repetição (for)
# Sintaxe: 

#meu_dicionario = {"Chave": "Valor"}

#for k, v in meu_dicionario.items():
    #print(f"Etiqueta: {k} | Dado: {v}")