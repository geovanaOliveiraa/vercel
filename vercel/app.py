from flask import Flask, render_template, request, redirect
lista= []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Home.html', Titulo= 'Bem vindo ao site de Viagens')

@app.route('/viagem')
def viagem():
    return  render_template('Viagem.html', Titulo= 'Melhores Viagens')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Titulo= 'Sobre o nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo= 'Cadastro de Viagens')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo='Viagens Cadastradas', lista= lista)

@app.route('/criar', methods=['POST'])
def criar():
    local= request.form['local']
    nome= request.form['nome']
    estação= request.form['estação']
    transporte= request.form['transporte']
    data= request.form['peso']
    viagem= [local, nome, estação,transporte,data]
    lista.append(viagem)
    return redirect('/exibir')

if __name__ == '__main__':
    app.run()
