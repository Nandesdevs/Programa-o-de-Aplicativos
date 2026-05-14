class Tarefa:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True
        