# Classe base Veiculo
class Veiculo:
    def __init__(self, placa, marca, modelo, ano, valor_diaria):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self.valor_diaria = valor_diaria
        # garantimos que _disponivel sempre será True
        self._disponivel = True

    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Veículo {self._modelo} alugado com sucesso!")
            dias = int(input("Quantidade de dias que o veiculo foi alugado? "))
            print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")

    def exibir_info(self):
        if self._disponivel:
            status = "Carro disponivel" 
        else:
            status = "Carro indisponivel"
        dados = {"Placa":self._placa, 
             "Marca":self._marca,
             "Modelo":self._modelo, 
             "Ano":self._ano,
             "Valor diaria":self.valor_diaria,
             "Disponibilidade": status            
            }
        
        print("\n--- Informações do Veículo ---")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

veiculo_teste = Veiculo("ABC-1234", "Toyota", "Corolla", 2024, 200)

#Veiculo disponivel pois não alugamos ainda
veiculo_teste.exibir_info()

#Alugou, veiculo indisponivel
veiculo_teste.alugar()

#Print do veiculo indisponivel
veiculo_teste.exibir_info()        
