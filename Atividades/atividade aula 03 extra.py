# Função para limpar tela
import os
def limpar_tela():
    # 'nt' identifica o sistema Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Classe base: Veiculo
class Veiculo:
    def __init__(self, placa, marca, modelo, ano, valor_diaria):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self.valor_diaria = valor_diaria
        # garantimos que _disponivel sempre será True
        self._disponivel = True

    # Função para alugar carro:
    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Veículo {self._modelo} alugado com sucesso!")
            dias = int(input("Quantidade de dias que o veiculo foi alugado? "))
            print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")

    # Função para exibir informações do carro:
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
        # Utilizei ".items() para mostrar a chave e o valor na saida, ficou + facil de mostrar as informações assim"
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    def devolução(self):
        if self._disponivel == False:
            self._disponivel = True
            print(f"Veículo {self._modelo} devolvido com sucesso!")
        else:
            print(f"Erro Veículo {self._modelo} não foi alugado...")

# Criação do veiculo para teste
veiculo_teste = Veiculo("ABC-1234", "Toyota", "Corolla", 2024, 200)

#Veiculo disponivel pois não alugamos ainda
veiculo_teste.exibir_info()

#Alugou, veiculo indisponivel
veiculo_teste.alugar()

#Print do veiculo indisponivel
veiculo_teste.exibir_info() 

limpar_tela()
# SUBCLASSES QUE VÃO HERDAR VEICULO
# SubClasse Carro: adicional de portas.
class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria, portas):
        super().__init__(placa, marca, modelo, ano, valor_diaria)
        self.portas = portas

    # Função com polimorfismo
    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Veículo {self._modelo} alugado com sucesso!")
            dias = int(input("Quantidade de dias que o veiculo foi alugado? "))
            # Se o aluguel for maior que 7 dias, ganha 10% de desconto no valor total. 
            if dias > 7:
                print(f"Parabéns, você alugou seu Veiculo por mais de 7 dias, o valor R${self.valor_diaria * dias} ganhou 10% de desconto...\n")
                print(f"O valor total a ser pago, com 10% de desconto é: R${0.10 * (self.valor_diaria * dias)}")
            else:
                print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")


meu_carro = Carro("ABC-1234", "Toyota", "Corolla pretin", 2024, 250, 4)

# SubClasse Moto: adicional cilindradas.
class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, marca, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

    def alugar(self):
        return super().alugar()

    #  Não tem desconto, mas tem uma taxa fixa de R$ 50 para lavagem do capacete, cobrada em toda devolução.
    def devolução(self):
        if self._disponivel == False:
            self._disponivel = True
            print(f"Cobrança de taxa obrigatoria de R$50 para lavagem do capacete...")
            print(f"Veículo {self._modelo} devolvido com sucesso!")
        else:
            print(f"Erro Veículo {self._modelo} não foi alugado...")

minha_moto = Moto("XYZ-5678", "Honda", "CB 500", 2023, 120.0, 500)

# SubClasse Caminhao: adicional capacidade_carga.
class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, marca, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

    # Função com polimorfismo
    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Veículo {self._modelo} alugado com sucesso!")
            dias = int(input("Quantidade de dias que o veiculo foi alugado? ")) 
            # O valor da diária aumenta em 20% se a capacidade de carga for maior que 5 toneladas (risco de desgaste). 
            if self.capacidade_carga > 5000:
                print(f"Detectamos que seu Caminhão pesa mais de 5 toneladas...\n")
                print(f"Taxa de 20% de adicional ao valor de R${self.valor_diaria * dias}, por risco de desgaste")
                print(f"O valor total a ser pago, com 20% de adicional é: R${(self.valor_diaria * 0.20) * dias}")
            else:
                print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")

meu_caminhao = Caminhao("LMN-9999", "Volvo", "FH 540", 2022, 600.0, 20000)

veiculos_aluguel = [veiculo_teste, meu_carro, minha_moto, meu_caminhao]
for veiculo in veiculos_aluguel:
    print(f"\nProcessando aluguel para: {veiculo._modelo}")
    veiculo.alugar()
