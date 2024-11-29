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

# Criar a tabela core_aluno
cur.execute('''
    CREATE TABLE IF NOT EXISTS core_aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT NOT NULL UNIQUE,
        turma INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE,
        FOREIGN KEY (turma) REFERENCES turma(id)
    )
''')

# Inserir dados na tabela turma (valores entre 3 e 23)
turmas = [(i, f'Turma {i}') for i in range(3, 24)]
cur.executemany('''
    INSERT OR IGNORE INTO turma (id, nome) VALUES (?, ?)
''', turmas)

# Função para gerar uma matrícula de 10 dígitos
def gerar_matricula():
    return ''.join(random.choices(string.digits, k=10))

# Lista de nomes fictícios para os alunos
nomes = [
    'Alice', 'Bruno', 'Carla', 'Diego', 'Eduarda', 'Felipe', 
    'Gabriela', 'Henrique', 'Isabela', 'João', 'Karen', 'Leonardo'
]

# Gerar alunos
alunos = []
for i in range(500):  # Criar 50 alunos
    nome = random.choice(nomes) + f' {random.choice(string.ascii_uppercase)}.'
    matricula = gerar_matricula()
    turma = random.randint(3, 23)
    email = f"{nome.replace(' ', '').lower()}@escola.com"
    alunos.append((nome, matricula, turma, email))

# Inserir alunos na tabela core_aluno
cur.executemany('''
    INSERT INTO core_aluno (nome, matricula, turma_id, email)
    VALUES (?, ?, ?, ?)
''', alunos)

# Confirmar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Tabela 'core_aluno' populada com sucesso!")
