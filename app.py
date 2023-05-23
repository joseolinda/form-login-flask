from flask import Flask, render_template, request, redirect, url_for
from utils import valida_cadastro

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

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

@app.route('/signup', methods=["GET", "POST"])
def signup():
    erro = request.args.get("erro")
    if erro != "":
        data = request.form
        return render_template('cadastrar.html', erro=erro, form=data)        
    
    return render_template('cadastrar.html', erro=None, form=None)        
        
@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    
    msg = valida_cadastro(nome, email, senha, confsenha)
    if msg is None:
       return redirect(url_for('login')) 
       
    return redirect(url_for('signup', erro=msg))

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)   