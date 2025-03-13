# Sistema de Backup e Recuperação Automatizado

Este projeto automatiza o processo de backup e restauração de um banco de dados PostgreSQL por meio de um script em Python. Ele gera backups com timestamp, registra logs detalhados das operações e permite a restauração dos dados a partir de um arquivo de backup específico.

## Funcionalidades

- **Backup Automatizado:**  
  Gera um arquivo de backup utilizando o `pg_dump`, com o nome formatado com data e hora da execução.

- **Restauração:**  
  Restaura o banco de dados a partir de um arquivo de backup usando o `pg_restore`, garantindo a substituição dos dados atuais.

- **Registro de Logs:**  
  Todas as operações são registradas em um arquivo de log (`backup_log.log`) para facilitar o monitoramento e a depuração.

## Requisitos

- **Python 3:**  
  Certifique-se de que o Python 3 está instalado no seu sistema.

- **PostgreSQL:**  
  As ferramentas `pg_dump` e `pg_restore` devem estar instaladas e configuradas no PATH, pois são utilizadas pelo script.

- **Acesso ao Banco de Dados:**  
  Configure as informações de conexão (host, porta, nome do banco, usuário e senha) de acordo com seu ambiente.

## Configuração

1. **Configure o Script:**

   Edite o arquivo `backup_script.py` (ou o nome escolhido para o script) e atualize as variáveis de configuração:

   ```python
   DB_HOST = 'localhost'
   DB_PORT = '5432'
   DB_NAME = 'seu_banco'
   DB_USER = 'seu_usuario'
   DB_PASSWORD = 'sua_senha'  

   BACKUP_DIR = '/caminho/para/backups'
   ```

2. **Criação do Diretório de Backup:**

   Se o diretório definido em `BACKUP_DIR` não existir, o script criará automaticamente.

## Uso

### Executando o Script

Para executar o script e utilizar as funcionalidades de backup ou restauração, utilize o seguinte comando:

```bash
python3 backup_script.py
```

Ao executar, o script exibirá um menu:

```plaintext
Escolha uma opção:
1. Realizar Backup
2. Restaurar Backup
Opção (1 ou 2):
```

- **Opção 1:** Realiza o backup do banco de dados e gera um arquivo com timestamp no diretório definido.
- **Opção 2:** Solicita o caminho do arquivo de backup a ser restaurado e executa a restauração.

### Agendamento Automatizado

Para agendar backups diários, você pode configurar uma *cron job* (em sistemas Linux). Por exemplo, para executar o backup todos os dias às 2h da manhã, adicione a seguinte linha ao seu crontab:

```cron
0 2 * * * /usr/bin/python3 /caminho/para/backup_script.py
```

## Melhorias Futuras

- **Segurança:**  
  Utilizar variáveis de ambiente ou arquivos de configuração seguros para gerenciar a senha do banco de dados.

- **Notificações:**  
  Integrar notificações (por e-mail ou outra forma) para alertar sobre o sucesso ou falhas no backup.

- **Rotação de Backups:**  
  Implementar uma rotina para exclusão de backups antigos e otimização do espaço em disco.

- **Interface Web/Dashboard:**  
  Desenvolver uma interface web para monitoramento dos backups e execução de restaurações.

## Contribuição

Contribuições são bem-vindas! Se você deseja sugerir melhorias ou corrigir algum problema, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.
