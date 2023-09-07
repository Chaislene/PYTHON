import sqlite3 

conexao = sqlite3.connect('coonexao_dados.py')
cursor =  conexao.cursor()

cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

conexao.commit()
conexao.close



