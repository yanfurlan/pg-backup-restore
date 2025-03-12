import subprocess
import datetime
import os
import logging

# =======================
# Configurações do Banco de Dados
# =======================
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'seu_banco'
DB_USER = 'seu_usuario'
DB_PASSWORD = 'sua_senha'  

# Diretório para armazenar os backups
BACKUP_DIR = '/caminho/para/backups'
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# =======================
# Configuração do Logging
# =======================
logging.basicConfig(
    filename='backup_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =======================
# Funções Principais
# =======================
def backup_database():
    """
    Realiza o backup do banco de dados utilizando o pg_dump.
    Gera um arquivo de backup com timestamp no nome.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")
    
    # Comando pg_dump com formato custom (-F c). Pode ser ajustado conforme a necessidade.
    cmd = [
        'pg_dump',
        '-h', DB_HOST,
        '-p', DB_PORT,
        '-U', DB_USER,
        '-F', 'c',  # formato custom
        '-f', backup_file,
        DB_NAME
    ]
    
    # Configurando a variável de ambiente para a senha
    env = os.environ.copy()
    env['PGPASSWORD'] = DB_PASSWORD

    try:
        subprocess.run(cmd, env=env, check=True)
        logging.info(f"Backup realizado com sucesso: {backup_file}")
        print(f"Backup realizado com sucesso: {backup_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao realizar backup: {e}")
        print(f"Erro ao realizar backup: {e}")

def restore_database(backup_file):
    """
    Restaura o banco de dados utilizando o pg_restore a partir de um arquivo de backup.
    A opção -c remove objetos existentes antes da restauração.
    """
    cmd = [
        'pg_restore',
        '-h', DB_HOST,
        '-p', DB_PORT,
        '-U', DB_USER,
        '-d', DB_NAME,
        '-c',  # limpa os objetos existentes antes de restaurar
        backup_file
    ]
    
    env = os.environ.copy()
    env['PGPASSWORD'] = DB_PASSWORD

    try:
        subprocess.run(cmd, env=env, check=True)
        logging.info(f"Restauração realizada com sucesso a partir do arquivo: {backup_file}")
        print(f"Restauração realizada com sucesso a partir do arquivo: {backup_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao restaurar o banco de dados: {e}")
        print(f"Erro ao restaurar o banco de dados: {e}")

# =======================
# Execução do Script
# =======================
if __name__ == '__main__':
    print("Escolha uma opção:")
    print("1. Realizar Backup")
    print("2. Restaurar Backup")
    opcao = input("Opção (1 ou 2): ")

    if opcao == '1':
        backup_database()
    elif opcao == '2':
        backup_file = input("Informe o caminho completo do arquivo de backup para restaurar: ")
        if os.path.exists(backup_file):
            restore_database(backup_file)
        else:
            print("Arquivo de backup não encontrado.")
    else:
        print("Opção inválida. Finalizando.")
