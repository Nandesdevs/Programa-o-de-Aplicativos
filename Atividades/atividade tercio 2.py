def consulta_filmes(catalogo):
    resp = 0
    while resp != 4:
        print("-"*50)
        print("1--- Consultar lista de filmes.")
        print("2--- Marcar filme como assistido.")
        print("3--- Sair")

        try:
            resp = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite apenas números. ")
            continue

        if resp == 1:
            for filme in catalogo:
                print(filme)
                print("- "*50)
        elif resp == 2:
            i = 1
            for filme in catalogo:
                print(f"{i}- {filme["titulo"]}")
                i += 1
            
            name_filme = str(input("Qual filme foi assistido?\n"))
            encontrado = False
            for filme in catalogo:
                if name_filme.lower() == filme["titulo"].lower():
                    filme["assistido"] = True
                    print(f"Sucesso! {filme["titulo"]} marcado como assistido. ")
                    encontrado = True
                    break

            if not encontrado:
                print("filme não encontrado tente novamente!")
        elif resp == 3:
            print("Obrigado por consultar nossos serviços de filme!")
            break
        else:
            print("Opção invalida. Tente novamente!")
    print("-"*50)

def favoritar_filmes(user, catalogo):
    favoritos = user["filmes_favoritos"]
    
    resp = "s"
    while resp == "s":
        for filme in catalogo:
            if filme["titulo"] in favoritos:
                status = "[ JÁ FAVORITADO ]"
            else:
                status = ""
            print(f"- {filme['titulo']} {status}")
            print("- "* 15)
        decisao = input("\nDeseja favoritar algum destes filmes agora? [S/N]: ").lower()
        if decisao == "s":
            name_filme = input("Digite o nome do filme: ").strip()
        else: 
            if filme["titulo"] in favoritos:
                print(f"Filmes favoritados: \n{" - ".join(favoritos)}.")
            print("Obrigado por utilizar nosso programa.")
            break

        if name_filme in favoritos:
            print("Filme ja adicionado a lista de favoritos")
        else:
            encontrado = False
            for filme in catalogo:
                if name_filme.lower() in filme["titulo"].lower():  
                    favoritos.append(filme["titulo"])
                    print(f"Sucesso! '{filme['titulo']}' adicionado a lista de favoritos.")
                    encontrado = True
                    break

            if not encontrado:
                print("filme não encontrado tente novamente!")

        resp = input("\nDeseja continuar no menu de favoritos? [S/N]: ").lower()
        if resp == "n":
            if filme["titulo"] in favoritos:
                print(f"Filmes favoritados: \n{" - ".join(favoritos)}.")
            print("Obrigado por utilizar nosso programa.")

catalogo = [
    {   "titulo": "A Rede Social",
        "ano": 2010,
        "genero": "Ficção Cientifica",
        "assistido": False
    },
    {   "titulo": "O Jogo da Imitição",
        "ano": 2014,
        "genero":"Suspense",
        "assistido": False
    },
    {   "titulo": "Piratas do Vale do Silício",
        "ano": 1999,
        "genero": "Drama Historico",
        "assistido": False
    },
    {   "titulo": "O Dilema das Redes",
        "ano": 2020,
        "genero": "Documentario",
        "assistido": False
    },
]

print(catalogo)

catalogo.append(
    {
        "titulo": "Matrix",
        "ano": 1999,
        "genero": "Ficção Cientifica",
        "assistido": False
    }
)

# Alteração do genero usando busca pelo for

for filme in catalogo:
    if filme["titulo"] == "O Jogo da Imitação":
        filme["genero"] = "Drama Historico"

# Alteração do genero por indice
catalogo[1]["genero"] = "Drama Historico"

consulta_filmes(catalogo)

# UI
apenas_titulos = []
for filme in catalogo:
    apenas_titulos.append(filme["titulo"])

print(f"Lista de titulos:{apenas_titulos}")

print("Filmes classicos anos 90:")
for filme in catalogo:
    if filme["ano"] < 2000:
        print(filme["titulo"])

contagem_generos = {}
for filme in catalogo:
    genero = filme["genero"]
    contagem_generos[genero] = contagem_generos.get(genero, 0) + 1
    
print(contagem_generos)

# Desafio do chefe
usuario_premium ={
        "nome": "Hernandes",
        "plano": "Premium",
        "filmes_favoritos": []
    }
 
if usuario_premium["plano"] == "Premium":
    print(f"Olá {usuario_premium["nome"]}, aqui estão seus filmes favoritos: {usuario_premium["filmes_favoritos"]}")
    fav_resp = input("Deseja favoritar algum filme?[Y/N]: ").lower()
    if fav_resp == "y":
        favoritar_filmes(usuario_premium, catalogo)
    else:
        print("Obrigado por utilizar nosso programa.")
else: 
    "Faça o upgrade para favoritar filmes!"

if usuario_premium["plano"] == "Premium":
    print(f"Olá {usuario_premium["nome"]}, aqui estão novamente seus filmes favoritos: {" - ".join(usuario_premium["filmes_favoritos"])}.")
else:
    print("")