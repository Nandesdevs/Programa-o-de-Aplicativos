# Atividade facil dms fiz em 2 minutos mas foi o que ele pediu
class carro:
    def __init__(self, marca ,modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("O carro ligou!")

    def desligar(self):
        print("O carro desligou!")

corsa = carro("Sla acho que fiat", "Corsinha rebaixado manow", 2010)
corsa.ligar()
corsa.desligar()