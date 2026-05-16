# Função para limpar o terminal
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

class JogoDaVelha:
    def __init__(self, jogador1, jogador2, tabuleiro, ultimo_valor):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro = tabuleiro
        self.ultimo_valor = ultimo_valor
        self.vitoria = False
    
    # Ver tabuleiro
    def ver_tabuleiro(self):
        for linha in self.tabuleiro:
            for valor in linha:
                print(f"[{valor}]", end="")
            print()
            print("-"*9)

    # Jogar!
    def jogar(self):
        while self.vitoria != True:
            for i in range(2):
                self.verificar_vitoria()
                if self.vitoria == True:
                    break
                self.ver_tabuleiro()
                print(f"Jogador {i+1} aonde deseja jogar?(linha/coluna...)\n")
                linha = int(input("Qual linha deseja jogar?"))
                linha -= 1
                coluna = int(input("Qual coluna deseja jogar?"))
                coluna -= 1

                if i == 0:
                    if self.tabuleiro[linha][coluna] == " ":
                        self.tabuleiro[linha][coluna] = self.jogador1
                        self.ultimo_valor = "X"
                    else:
                        print(f"Posição ja ocupada, tente novamente...")
                        break
                    if self.vitoria == True:
                        break
                else:
                    if self.tabuleiro[linha][coluna] == " ":
                        self.tabuleiro[linha][coluna] = self.jogador2
                        self.ultimo_valor = "O"
                    else:
                        print(f"Posição ja ocupada, tente novamente...")
                        break
                    if self.vitoria == True:
                        break
                limpar_tela()


    # Função para verificar a vitoria
    def verificar_vitoria(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                self.vitoria = True

        for i in range(3):
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                self.vitoria = True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            self.vitoria = True

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            self.vitoria = True

    # Finalização do jogo
    def fim(self):
        print("=== {TABELA DO JOGO} ===")
        print("-"*24)
        self.ver_tabuleiro()
        if self.ultimo_valor == "X":
            print(f"Jogador 1({self.jogador1}) ganhou!!!\nJogador 2({self.jogador2}) perdeu...")
        else:
            print(f"Jogador 2({self.jogador2}) ganhou!!!\nJogador 1({self.jogador1}) perdeu...")
        try_again = int(input("Digite 1 para jogar novamente, ou 2 caso queira encerrar: "))
        limpar_tela()
        if try_again == 1:
            self.limpar_tabuleiro()
            self.jogar()
        else:
            print("Obrigado pelo jogo.")

    # Função para limpar o tabuleiro e não dar erro na hora de reiniciar
    def limpar_tabuleiro(self):
        self.tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
        self.vitoria = False



tabuleiro_inicial = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]
jogo_teste = JogoDaVelha("X", "O", tabuleiro_inicial, " ")
jogo_teste.jogar()
jogo_teste.fim()