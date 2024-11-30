import sqlite3
import random

# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')  # Substitua pelo caminho do seu banco de dados, se necessário
cur = conn.cursor()

# Criar a tabela core_professor, se não existir
cur.execute('''
    CREATE TABLE IF NOT EXISTS core_professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        siap TEXT UNIQUE NOT NULL
    )
''')

# Gerar dados aleatórios para professores
def gerar_nome():
    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Fernanda', 'Carlos', 'Bianca', 'Lucas', 'Juliana', 'Gabriel']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Costa', 'Almeida', 'Martins', 'Souza', 'Ferreira', 'Lima']
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def gerar_email(nome):
    base = nome.lower().replace(' ', '.')
    return f"{base}@gmail.com"

def gerar_siap():
    return f"{random.randint(1000000, 9999999)}"

# Lista para armazenar professores
professores = []
for _ in range(20):  # Gere 20 professores
    nome = gerar_nome()
    email = gerar_email(nome)
    siap = gerar_siap()
    professores.append((nome, email, siap))

# Inserir dados na tabela core_professor
try:
    cur.executemany('''
        INSERT INTO core_professor (nome, email, siap)
        VALUES (?, ?, ?)
    ''', professores)
    conn.commit()
    print("Tabela 'core_professor' populada com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao inserir os dados: {e}")
finally:
    # Fechar a conexão
    conn.close()
