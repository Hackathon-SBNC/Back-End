import sqlite3
import random
from hashlib import sha256

# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# Criar a tabela core_user
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

# Criar a tabela associativa user_group
cur.execute('''
    CREATE TABLE IF NOT EXISTS user_group (
        user_id INTEGER NOT NULL,
        group_id INTEGER NOT NULL,
        PRIMARY KEY (user_id, group_id),
        FOREIGN KEY (user_id) REFERENCES core_user(id),
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
''')

# Criar a tabela groups (caso ainda não exista)
cur.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Inserir dados na tabela groups
groups = [(1, 'Admin'), (2, 'Editor'), (3, 'Viewer')]
cur.executemany('''
    INSERT OR IGNORE INTO groups (id, name) VALUES (?, ?)
''', groups)

# Função para gerar um hash de senha
def gerar_senha(senha):
    return sha256(senha.encode()).hexdigest()

# Função para gerar e-mails fictícios
def gerar_email(nome):
    base = nome.lower().replace(' ', '.')
    return f'{base}@gmail.com'

# Lista de nomes fictícios para os usuários
nomes_usuarios = [
    'Alice Silva', 'Bruno Mendes', 'Carla Dias', 'Diego Rocha', 
    'Eduarda Lima', 'Felipe Souza', 'Gabriela Martins', 
    'Henrique Alves', 'Isabela Santos', 'João Pereira'
]

# Gerar usuários
usuarios = []
for nome in nomes_usuarios:
    email = gerar_email(nome)
    password = gerar_senha("123456")  # Senha padrão "123456"
    usuarios.append((password, None, 0, email, nome, 1, 0))

# Inserir usuários na tabela core_user
cur.executemany('''
    INSERT INTO core_user (password, last_login, is_superuser, email, name, is_active, is_staff)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', usuarios)

# Recuperar IDs dos usuários criados
cur.execute('SELECT id FROM core_user')
user_ids = [row[0] for row in cur.fetchall()]

# Gerar relações na tabela user_group (associando usuários a grupos aleatórios)
user_group = [(user_id, random.randint(1, 3)) for user_id in user_ids]

# Inserir dados na tabela user_group
cur.executemany('''
    INSERT INTO core_user_groups (user_id, group_id) VALUES (?, ?)
''', user_group)

# Confirmar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Banco de dados populadas com sucesso!")
