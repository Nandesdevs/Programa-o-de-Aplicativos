# Jogo de adivinhação
from random import randint
print ("Bem vindo! Descubra um valor entre 1 e 100")
sorteado = randint(1, 100)
chute = 0
while chute != sorteado:
    chute = int(input ("Chute: "))
    if chute == sorteado:
        print ("Você venceu!")
    else:
        if chute > sorteado:
            print ("Alto")
        else:
            print ("Baixo")
print ("Fim do jogo!")