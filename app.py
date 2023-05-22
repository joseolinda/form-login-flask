from flask import Flask, render_template, request, redirect, url_for
from utils import valida_cadastro

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'admin' and senha == 'admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('cadastrar.html')
        
@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    
    msg = valida_cadastro(nome, email, senha, confsenha)
    
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)   