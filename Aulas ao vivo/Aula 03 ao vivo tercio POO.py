class Pessoa:
    # __init__ = Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos!")

Professor = Pessoa("Tercio", 29)
Aluno = Pessoa("Hernandes", 19)

Professor.apresentar()
Aluno.apresentar()

# Classe exemplo Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo #privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        
    def consultar_saldo(self):
        return self._saldo # bota o _ para so poder alterar quando for depositar e deixar privado
    
conta = ContaBancaria("Hernandes", 3000)

print(f"Seu saldo atual é: {conta.consultar_saldo()}")

# Atualização de saldo com o deposito
conta.depositar(1000)
print(f"Seu saldo atual é: {conta.consultar_saldo()}")

# Classe exemplo Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Estou estudando {self.curso}.")

e1 = Estudante("Nicolas", 19, "Analise e Desenvolvimento de Sistemas")

e1.apresentar()

# Exemplo polimorfismo
class Animal:
    def falar(self):
        print("O animal emite um som...")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro Late.")

class Gato(Animal):
    def falar(self):
        print("O gato Mia.")

animais = [Animal() ,Cachorro(), Gato()]
for animal in animais:
    animal.falar()