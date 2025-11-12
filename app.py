from flask import Flask,render_template ,request
import model

srv = Flask(__name__)

@srv.route('/')
def get_home():
    pass
@srv.post('/pesquisar')
def post_pesquisar():
    nome = request.form['nome']
    listagem_clientes = model.pesquisar_clientes(nome)
    return render_template('pesquisar.html', clientes = listagem_clientes)

@srv.get('/pesquisar')
def get_pesquisar():
    return render_template('pesquisar.html')

@srv.get('/cadastrar')
def get_cadastrar():
    listagem_clientes = model.consultar_clientes()
    return render_template('cadastrar.html' , clientes = listagem_clientes)

@srv.post('/cadastrar')
def post_cadastrar():
    nome  = request.form['nome']
    email = request.form['email']
    model.cadastrar_clientes(nome,email)
    return render_template('cadastrar.html')


if __name__ == '__main__':
    srv.run(host='localhost', port=5000, debug = True)

