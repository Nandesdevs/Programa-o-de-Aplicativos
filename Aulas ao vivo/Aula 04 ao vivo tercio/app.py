# Importa o Flask
from flask import Flask

# Essa linha diz = Flask apartir daqui começe a trabalhar
app = Flask(__name__)

# Criação de uma rota
# Decorador app route diz para o flask, quando alguem executar uma pagina inicial(representada por('/') ao lado de app route) execute a função logo abaixo
@app.route('/')
def index():
    return '<h1>Olá, seja bem-vindo(a) ao meu primeiro site em Flask!</h1>''<br>''<p>Esse tal de Flask é bom mermo...</p>'

# Esse if name é o nosso "melhor amigo", se a gente precisar alterar o codigo ele reinicia o server sozinho, mostra os erros que tiver e atualiza automaticamente
if __name__ == '__main__':
    app.run(debug = True)