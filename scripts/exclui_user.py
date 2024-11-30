import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')  # Substitua pelo caminho do seu banco de dados, se necessário
cur = conn.cursor()

# Excluir todos os registros da tabela core_user
try:
    # Desabilitar restrições de chave estrangeira temporariamente (se necessário)
    cur.execute('PRAGMA foreign_keys = OFF;')

    # Excluir os dados da tabela core_user
    cur.execute('DELETE FROM core_user;')

    tabelas = ['user_group', 'turma', 'responsavel', 'groups']

    for tabela in tabelas:
        cur.execute(f'DROP TABLE IF EXISTS {tabela};')
        print(f"Tabela '{tabela}' excluída com sucesso.")

    # Confirmar as alterações
    conn.commit()
    print("Todos os registros da tabela 'core_user' foram excluídos com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar excluir os registros: {e}")
finally:
    # Habilitar restrições de chave estrangeira novamente
    cur.execute('PRAGMA foreign_keys = ON;')
    # Fechar a conexão
    conn.close()
