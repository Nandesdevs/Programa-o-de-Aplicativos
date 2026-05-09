class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_info(self):
        print("--- {Informações do Produto} ---")
        print(f"{self.nome}:\nPreço: R${self.preco}\nQuantidade: {self.quantidade}\n")

    def calculo_total(self, quantidade_compra):
        quantidade_compra = int(input(f"Quanto(a)s, {self.nome}s deseja adicionar a compra?\n(Quantidade total {self.quantidade}):\n"))
        print("- "* 10)
        print(f"Preço total: {self.preco * quantidade_compra}")

pd1 = Produto("Coca-Cola", 30, 5)
pd2 = Produto("Pão", 3.50, 100)

pd1.exibir_info()
pd2.exibir_info()

pd1.calculo_total()
pd2.calculo_total()
