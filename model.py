import sqlite3

def cadastrar_clientes(nome,email):
    with sqlite3.connect('clientes.db') as conn:
        sql_insert_clientes = '''
        INSERT INTO clientes (nome,email)
        VALUES (?,?)
        '''
        conn.execute(sql_insert_clientes, (nome,email))


def consultar_clientes():
    with sqlite3.connect('clientes.db') as conn:
        sql_listar_clientes = '''
        SELECT nome, email
        FROM clientes;
        '''
        cur = conn.cursor()
        cur.execute(sql_listar_clientes)
        return cur.fetchall() # retorna uma lista de tuplas [(nome,email),(nome,email)]
    

def pesquisar_clientes(nome):
    with sqlite3.connect('clientes.db') as conn:
        sql_pesquisar_clientes = '''
        SELECT nome, email
        FROM clientes
        WHERE nome LIKE ?
        '''
        cur = conn.cursor()
        cur.execute(sql_pesquisar_clientes,(f'%{nome}%',))
        return cur.fetchall() # retorna uma lista de tuplas [(nome,email),(nome,email)]
    