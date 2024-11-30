import sqlite3
import random
import string
from hashlib import sha256


# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# ======== CRIAÇÃO DAS TABELAS ========

# Tabela core_aluno
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

# Tabela core_user
cur.execute('''
    CREATE TABLE IF NOT EXISTS core_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        last_login TEXT DEFAULT NULL,
        email TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1,
        is_staff INTEGER DEFAULT 0
    )
''')


# ======== POVOAMENTO DAS TABELAS ========

# ======== TABELA RESPONSAVEL ========
def gerar_telefone():
    ddd = random.randint(11, 99)
    numero = ''.join(random.choices(string.digits, k=8))
    return f'({ddd}) 9{numero}'

def gerar_email(nome):
    base = nome.lower().replace(' ', '.')
    return f'{base}@gmail.com'

nomes_responsaveis = [
    'Alice', 'Bruno', 'Carla', 'Diego', 'Eduarda', 'Felipe',
    'Gabriela', 'Henrique', 'Isabela', 'João', 'Karen', 'Leonardo'
]
responsaveis = []
for i in range(50):
    nome = random.choice(nomes_responsaveis) + f' {random.choice(string.ascii_uppercase)}.'
    email = gerar_email(nome)
    telefone = gerar_telefone()
    responsaveis.append((nome, email, telefone))    

cur.executemany('INSERT INTO core_responsavel (nome, email, telefone) VALUES (?, ?, ?)', responsaveis)

# ======== TABELA CORE_ALUNO ========
def gerar_matricula():
    return ''.join(random.choices(string.digits, k=10))

nomes_alunos = [
    'Alice', 'Bruno', 'Carla', 'Diego', 'Eduarda', 'Felipe',
    'Gabriela', 'Henrique', 'Isabela', 'João', 'Karen', 'Leonardo'
]

alunos = []
for i in range(100):
    nome = random.choice(nomes_alunos) + f' {random.choice(string.ascii_uppercase)}.'
    matricula = gerar_matricula()
    turma_id = random.randint(1, 21)
    responsavel_id = random.randint(1, 3)
    idade = random.randint(14, 20)
    email = f"{nome.replace(' ', '.').lower() + str(random.randint(1, 999))}@gmail.com"
    alunos.append((nome, matricula, turma_id, email, responsavel_id, idade))

cur.executemany('''
    INSERT INTO core_aluno (nome, matricula, turma_id, email, responsavel_id, idade)
    VALUES (?, ?, ?, ?, ?, ?)
''', alunos)

# ======== TABELA CORE_USER ========
def gerar_senha(senha):
    return sha256(senha.encode()).hexdigest()

nomes_usuarios = [
    'Alice Silva', 'Bruno Mendes', 'Carla Dias', 'Diego Rocha',
    'Eduarda Lima', 'Felipe Souza', 'Gabriela Martins',
    'Henrique Alves', 'Isabela Santos', 'João Pereira'
]

usuarios = []
for nome in nomes_usuarios:
    email = gerar_email(nome + '.' + str(random.randint(1, 999)))
    password = gerar_senha("123456")
    usuarios.append((password, None, 0, email, nome, 1, 0))

cur.executemany('''
    INSERT INTO core_user (password, last_login, is_superuser, email, name, is_active, is_staff)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', usuarios)

# ======== TABELA USER_GROUP ========
cur.execute('SELECT id FROM core_user')
user_ids = [row[0] for row in cur.fetchall()]

# user_group = []
# for user_id in user_ids:
#     id_user = user_id
#     id_group = random.randint(1, 3)
#     user_group.append((id_user, id_group))
# cur.executemany('INSERT INTO core_user_groups (user_id, group_id) VALUES (?, ?)', user_group)

# ======== FINALIZAÇÃO ========
conn.commit()
conn.close()

print("Todas as tabelas foram criadas e populadas com sucesso!")
