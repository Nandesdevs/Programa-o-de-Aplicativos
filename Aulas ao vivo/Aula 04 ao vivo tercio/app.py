# Importa o Flask
from flask import Flask, render_template, request, redirect, url_for

# Importar a classe tarefas para nosso app que é o programa principal
from models import Tarefa

# Essa linha diz = Flask apartir daqui começe a trabalhar
app = Flask(__name__)

# lista para simular um mini banco de dados
tarefas = []
contador_id = 1


# Criação de uma rota
# Decorador app route diz para o flask, quando alguem executar uma pagina inicial(representada por('/') ao lado de app route) execute a função logo abaixo
@app.route('/')
def index():
    return render_template('index.html',lista_tarefas = tarefas)

@app.route('/adicionar', methods = ['POST'])
def adicionar():
    global contador_id
    descricao = request.form.get('descricao')
    nova_tarefa = Tarefa(contador_id, descricao)
    tarefas.append(nova_tarefa)
    contador_id += 1
    return redirect(url_for('index'))
# Esse if name é o nosso "melhor amigo", se a gente precisar alterar o codigo ele reinicia o server sozinho, mostra os erros que tiver e atualiza automaticamente
# Esse main é o corpo principal do programa
if __name__ == '__main__':
    app.run(debug = True)