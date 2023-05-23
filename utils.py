def valida_cadastro(nome, email, senha, confsenha):
    if nome == '':
        return 'O campo nome é obrigatório'
    elif len(nome) < 3:
        return 'O nome deve ter pelo menos 3 caracteres'
    elif email == '':
        return 'O campo e-mail é obrigatório'
    elif senha == '':
        return 'O campo senha é obrigatório'
    elif senha != confsenha:
        return 'As senhas não conferem'
    else:
        return None