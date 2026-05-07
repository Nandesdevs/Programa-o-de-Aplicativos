class ContaBancaria:
        #O "Saber" (Atributos): **em Python o nome é sempre __init__
        #Ele é chamado de Construtor. O nome tem dois sublinhados antes e depois (__) para indicar que é um método especial da linguagem
        def __init__(self, titular, saldo_inicial, cpf):
                self.titular = titular
                self.saldo_inicial = saldo_inicial
                self.cpf = cpf
        # O "Fazer": Método para aumentar o saldo
        def depositar(self, valor):
            if valor > 0:
                self.saldo_inicial += valor
                print(f"Depósito de R$ {valor} realizado com sucesso!")
            else:
                print("O valor do depósito deve ser positivo.")
        # Metodo para sacar dinheiro
        def sacar(self, valor_saque):
            if valor_saque <= 0 or valor_saque == self.saldo_inicial:
                print("Valor invalido, tente novamente!")
            else:
                self.saldo_inicial -= valor_saque
                print(f"Saque de R${valor_saque} realizado com sucesso!")
        
# Objeto minha_conta
minha_conta = ContaBancaria("Hernandes Santos", 1000, "XXX.XXX.XXX-XX")

# Conta antes da atualização
print(f"Conta de {minha_conta.titular}:\nCPF: {minha_conta.cpf}.\nSaldo: {minha_conta.saldo_inicial}.")

# Chamando o método (a ação)
# Ler o final do arquivo POO, explicação extra apos a parte pratica, para entender como funciona em um sistema grande para um objeto especifico fazer o metodo com os dados certos.
minha_conta.depositar(500)

# Chamando o outro método (a ação)
print("- "*15)
print(f"Conta de {minha_conta.titular}/ Saldo Total: {minha_conta.saldo_inicial}")
valor_saque = int(input("Qual valor deseja sacar?"))
minha_conta.sacar(valor_saque)

# Vendo o novo "Saber" (Atributo atualizado)
print(f"Novo saldo de {minha_conta.titular}: R$ {minha_conta.saldo_inicial}")
