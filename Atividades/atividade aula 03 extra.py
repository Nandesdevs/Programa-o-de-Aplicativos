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
        self._dias_alugados = None

    # Função para alugar carro:
    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Veículo {self._modelo} alugado com sucesso!")
            dias = int(input("Quantidade de dias que o veiculo foi alugado? "))
            self._dias_alugados = dias
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

    def devolução(self, dias = None):
        if self._disponivel == False:
            if dias is None:
                dias = self._dias_alugados
                valor_total = self.valor_diaria * dias
                self._disponivel = True
                print(f"Veículo {self._modelo} devolvido com sucesso!")
                print(f"R${valor_total:.2f}")
        else:
            print(f"Erro Veículo {self._modelo} não foi alugado...")

# Criação do veiculo para teste
veiculo_teste = Veiculo("ABC-1234", "Toyota", "Corolla", 2024, 200)

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
            self._dias_alugados = dias
            # Se o aluguel for maior que 7 dias, ganha 10% de desconto no valor total. 
            if dias > 7:
                valor_sem_desconto = self.valor_diaria * dias
                valor_com_desconto = valor_sem_desconto * 0.9
                print(f"Você alugou seu Veiculo por mais de 7 dias, o valor R${valor_sem_desconto:.2f} ganhou 10% de desconto...\n")
                print(f"O valor total a ser pago, com 10% de desconto é: R${valor_com_desconto:.2f}")
            else:
                print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")

# Criação do carro
meu_carro = Carro("ABC-0707", "Mitsubishi", "Corolla pretin", 2024, 250, 4)

# SubClasse Moto: adicional cilindradas.
class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, marca, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

    def alugar(self):
        return super().alugar()

    #  Não tem desconto, mas tem uma taxa fixa de R$ 50 para lavagem do capacete, cobrada em toda devolução.
    def devolução(self, dias = None):
        if self._disponivel == False:
            if dias is None:
                dias = self._dias_alugados
                valor_total = (self.valor_diaria * dias) + 50
                self._disponivel = True
                print(f"Valores + Cobrança de taxa obrigatoria de R$50 para lavagem do capacete...")
                print(f"R${valor_total:.2f}")
                print(f"Veículo {self._modelo} devolvido com sucesso!")
        else:
            print(f"Erro Veículo {self._modelo} não foi alugado...")

# Criação da moto
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
            self._dias_alugados = dias
            # O valor da diária aumenta em 20% se a capacidade de carga for maior que 5 toneladas (risco de desgaste). 
            if self.capacidade_carga > 5000:
                valor_sem_adicional = self.valor_diaria * dias
                valor_com_adicional = valor_sem_adicional * 1.20
                print(f"Detectamos que seu Caminhão pesa mais de 5 toneladas...\n")
                print(f"Taxa de 20% de adicional ao valor de R${valor_sem_adicional:.2f}, por risco de desgaste")
                print(f"O valor total a ser pago, com 20% de adicional é: R${valor_com_adicional:.2f}")
            else:
                print(f"O valor total a ser pago é: R${self.valor_diaria * dias}")
        else:
            print("Veiculo indisponivel para aluguel.")

# Criação do caminhão
meu_caminhao = Caminhao("LMN-9999", "Volvo", "FH 540", 2022, 600.0, 20000)

class Cliente():
    def __init__ (self, nome, cpf, telefone):
        self.nome = nome
        self._cpf = cpf
        self.telefone = telefone
        self._veiculo_alugado = None
    
    # Tenta alugar o veículo. Se der certo, guarda o objeto veículo no atributo veiculo_alugado. 
    def solicitar_aluguel(self, veiculo):
        if veiculo._disponivel:
            veiculo.alugar()
            self._veiculo_alugado = veiculo
            return True
        else:
            print(f"Veículo {veiculo._modelo} não está disponível!")
            return False
    
    # Se o cliente tiver um veículo alugado, chama o método devolver do veículo, imprime o recibo com o valor a pagar e limpa o atributo veiculo_alugado.
    def finalizar_aluguel(self, dias = None):
        if self._veiculo_alugado is not None:
            self._veiculo_alugado.devolução(dias)
            self._veiculo_alugado = None
        else:
            print(f"Cliente {self.nome} não possui veículo alugado!")

    # Metodo auxiliar para mostrar veiculo alugado
    def exibir_veiculo_alugado(self):
        if self._veiculo_alugado is not None:
             print(f"Veículo alugado: {self._veiculo_alugado._modelo}")
        else:
            print("Nenhum veículo alugado no momento")


# Teste final do codigo
# 1. Instancie pelo menos um Carro, uma Moto e um Caminhão. 
# 2. Instancie dois Clientes
# 3. Faça o Cliente 1 alugar o Carro. 
# 4. Tente fazer o Cliente 2 alugar o mesmo Carro (deve dar erro!). 
# 5. Faça o Cliente 2 alugar a Moto
# 6. Faça os dois clientes devolverem os veículos após 10 dias e verifiquem se os cálculos (descontos e taxas) foram aplicados corretamente.


# 1. Instancie pelo menos um Carro, uma Moto e um Caminhão (já feito)
veiculos_alugar = [veiculo_teste, meu_carro, meu_caminhao, minha_moto]
for veiculo in veiculos_alugar:
    print(f"\n=== Alugando {veiculo._modelo} ===")
    veiculo.alugar()
    while True:
        resposta = input("\nAperte Enter para prosseguir: ")

        if resposta == "":
            limpar_tela()
            break

    print("Prosseguindo...")

# Teste 2
cliente_nandes = Cliente("Hernandes", "XXX.XXX.XXX-XX", 759999999)
cliente_nicolas = Cliente("Nicolas", "XXX.XXX.XXX-XX", 759999999)

# Desalugando veiculos para teste
for veiculo in veiculos_alugar:
    print(f"=== Desalugando {veiculo._modelo} ===")
    veiculo.devolução()
    while True:
        resposta = input("\nAperte Enter para prosseguir: ")

        if resposta == "":
            limpar_tela()
            break

    print("Prosseguindo...")

# Teste 3 e 4, saida do teste 4 = "Véiculo Corolla pretin não está disponível!"
cliente_nandes.solicitar_aluguel(meu_carro)
cliente_nicolas.solicitar_aluguel(meu_carro)

# Teste 5
cliente_nicolas.solicitar_aluguel(minha_moto)

# Teste 6
# Carro = 10% adicionado com sucesso.
# Caminhão = peso acima de 5 toneladas 20% de adicional adicionado com sucesso.
# Moto = Cobrança de taxa de 50 reais adicionais adicionado com sucesso.