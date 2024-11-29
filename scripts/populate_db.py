import sqlite3
import random
import string

# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# Criar a tabela turma (caso ainda não exista)
cur.execute('''
    CREATE TABLE IF NOT EXISTS turma (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
''')

# Criar a tabela responsavel (caso ainda não exista)
cur.execute('''
    CREATE TABLE IF NOT EXISTS responsavel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL UNIQUE
    )
''')

# Criar a tabela core_aluno
cur.execute('''
    CREATE TABLE IF NOT EXISTS core_aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT NOT NULL UNIQUE,
        turma_id INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE,
        responsavel_id INTEGER NOT NULL,
        idade INTEGER NOT NULL,
        FOREIGN KEY (turma_id) REFERENCES turma(id),
        FOREIGN KEY (responsavel_id) REFERENCES responsavel(id)
    )
''')

# Inserir dados na tabela turma (valores entre 3 e 23)
turmas = [(i, f'Turma {i}') for i in range(1, 21)]
cur.executemany('''
    INSERT OR IGNORE INTO turma (id, nome) VALUES (?, ?)
''', turmas)

# Função para gerar telefones no formato brasileiro
def gerar_telefone():
    ddd = random.randint(11, 99)  # Gerar DDD
    numero = ''.join(random.choices(string.digits, k=8))  # 8 dígitos
    return f'({ddd}) 9{numero}'

# Função para gerar nomes fictícios
def gerar_nome(prefixo, quantidade):
    return [f'{prefixo} {i}' for i in range(1, quantidade + 1)]

# Função para gerar e-mails fictícios
def gerar_email(nome):
    base = nome.lower().replace(' ', '.')
    return f'{base}@responsavel.com'

# Inserir dados na tabela responsavel
responsaveis = []
nomes_responsaveis = gerar_nome('Responsável', 50)
for nome in nomes_responsaveis:
    email = gerar_email(nome)
    telefone = gerar_telefone()
    responsaveis.append((nome, email, telefone))

cur.executemany('''
    INSERT INTO core_responsavel (nome, email, telefone) VALUES (?, ?, ?)
''', responsaveis)

# Função para gerar uma matrícula de 10 dígitos
def gerar_matricula():
    return ''.join(random.choices(string.digits, k=10))

# Lista de nomes fictícios para os alunos
nomes_alunos = [
    'Alice', 'Bruno', 'Carla', 'Diego', 'Eduarda', 'Felipe',
    'Gabriela', 'Henrique', 'Isabela', 'João', 'Karen', 'Leonardo'
]

# Gerar alunos
alunos = []
for i in range(50):  # Criar 50 alunos
    nome = random.choice(nomes_alunos) + f' {random.choice(string.ascii_uppercase)}.'
    matricula = gerar_matricula()
    turma_id = random.randint(1, 21)
    responsavel_id = random.randint(1, 50)
    idade = random.randint(14, 20)
    email = f"{nome.replace(' ', '').lower()}@escola.com"
    alunos.append((nome, matricula, turma_id, email, responsavel_id, idade))

# Inserir alunos na tabela core_aluno
cur.executemany('''
    INSERT INTO core_aluno (nome, matricula, turma_id, email, responsavel_id, idade)
    VALUES (?, ?, ?, ?, ?, ?)
''', alunos)

# Confirmar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Banco de dados populado com sucesso!")
