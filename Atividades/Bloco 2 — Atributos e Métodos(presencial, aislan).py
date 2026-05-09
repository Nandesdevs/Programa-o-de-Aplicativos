class ContaBancaria:
    def __init__(self, titular, saldo_inicial = 0, limite_cheque_especial = 500):
        self.titular = titular
        self._saldo_inicial = saldo_inicial
        self.historico = []
        self._limite_cheque_especial = limite_cheque_especial
    
    def ver_extrato(self):
        print("\n-- {Extrato Bancario} --")
        print(f"Titular: {self.titular}\nSaldo: R${self._saldo_inicial:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self._saldo_inicial += valor
            self.historico.append((f"Deposito de R${valor:.2f}"))
            print(f"\nValor de R${valor:.2f} adicionado a conta...\nSaldo atual: {self._saldo_inicial:.2f}")
        else:
            print("\nValor de deposito invalido!!")

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite_cheque_especial:
            self._saldo_inicial -= valor
            self.historico.append((f"Saque de R${valor:.2f}"))
            print(f"\nValor de R${valor:.2f} retirado da conta...\nSaldo atual: {self._saldo_inicial:.2f}")

    def exibir_historico(self):
        print(f"\nHistorico de transação de {self.titular}")
        i = 1
        for transacao in self.historico:
            print("-_"*15,f"\n{i}.{transacao}")
            i += 1

    def cobrar_juros(self):
        if self._saldo_inicial < 0:
            self._saldo_inicial *= 1.05 
            
dev_nic = ContaBancaria("Nicklaus", 3755.73)
dev_nandes = ContaBancaria("Nantropico", 47.22)
dev_kaua = ContaBancaria("Kauã El'Capon", 13993.69)

dev_nic.ver_extrato()
dev_nandes.ver_extrato()
dev_kaua.ver_extrato()

dev_nandes.depositar(1000)
dev_nandes.sacar(300)
dev_nandes.ver_extrato
dev_nandes.exibir_historico()
dev_nic.exibir_historico()
dev_kaua.exibir_historico()