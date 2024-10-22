![10991330 (1)](https://github.com/user-attachments/assets/1e444620-05d4-4b1c-a5a3-30b7c573f0b3)

# Como configurar uma instância de banco de dados no Portal Azure
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

> A computação em nuvem refere-se ao fornecimento de serviços de computação via internet, permitindo inovações rápidas, flexibilidade e economias de escala. 
  
1. **Acessar o Portal Azure**: 
   - Entre no **portal.azure.com** com sua conta.
2. **Criar um Recurso**:
   - No menu lateral, clique em **“Criar um recurso”**.
   - Na barra de pesquisa, procure por **Banco de Dados** (ex.: SQL Database, MySQL, PostgreSQL) e selecione o tipo desejado.
3. **Configurar a Instância**:
   - **Assinatura e Grupo de Recursos**: Selecione sua assinatura e crie/seleciona um **Grupo de Recursos** para organizar o projeto.
   - **Nome do Banco de Dados**: Insira um nome exclusivo para a instância de banco de dados.
   - **Servidor**: Crie um novo servidor ou selecione um existente. Especifique o nome do servidor, a região, login administrativo e senha.
4. **Definir Especificações de Desempenho**:
   - Escolha o **Plano de Serviço** (camadas de desempenho como Básico, Standard, Premium), que determina a capacidade de armazenamento e processamento.
   - Configure o **tamanho do banco de dados** e a capacidade de processamento (DTUs ou vCores).
5. **Configurações Adicionais**:
   - **Backups e Redundância**: Escolha a opção de backup (locais, georredundantes) conforme suas necessidades de recuperação de desastres.
   - **Rede e Segurança**: Configure o acesso ao banco de dados, definindo IPs permitidos ou integrando a instância a uma Rede Virtual (VNet).
6. **Revisar e Criar**:
   - Revise as configurações e clique em **“Criar”**. O Azure levará alguns minutos para provisionar a instância.
7. **Conectar ao Banco de Dados**:
   - Após a criação, obtenha o **String de Conexão** para conectar aplicativos ao banco de dados usando ferramentas como SQL Server Management Studio (para SQL) ou pgAdmin (para PostgreSQL).
