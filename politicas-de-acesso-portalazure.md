![post_thumbnail-0fb93e0cf06d246f91f5f9fb2651e91d](https://github.com/user-attachments/assets/f8c9ae80-c439-48c6-97ef-7db36c0ce50e)

# Políticas de Acesso no Azure
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

> As políticas de acesso no Azure são fundamentais para garantir a segurança e a conformidade em ambientes de nuvem. Elas definem como e quem pode acessar os recursos da Azure, além de assegurar que o acesso seja concedido de forma controlada e monitorada. Aqui estão os principais aspectos das políticas de acesso no Azure:

### 1. **Controle de Acesso Baseado em Funções (RBAC)**
   - O Azure utiliza o **RBAC** para gerenciar permissões de acesso a recursos.
   - As permissões são atribuídas a funções (como **Leitor**, **Colaborador**, **Proprietário**) que podem ser atribuídas a usuários, grupos ou identidades de serviços.

### 2. **Identidade e Acesso**
   - Utilize o **Azure Active Directory (Azure AD)** para gerenciar identidades e autenticação.
   - Permite integrar com identidades locais e fornece autenticação multifatorial (MFA) para aumentar a segurança.

### 3. **Políticas de Acesso Condicional**
   - As políticas de acesso condicional permitem definir quando e como os usuários podem acessar os recursos, com base em condições específicas, como localização, dispositivo e risco.
   - Exemplo: exigir MFA para acessar recursos críticos fora da rede corporativa.

### 4. **Listas de Controle de Acesso (ACLs)**
   - As ACLs fornecem um método para controlar o acesso a recursos específicos, como armazenamentos e bancos de dados, definindo quem pode acessar e realizar ações nesses recursos.

### 5. **Auditoria e Monitoramento**
   - O Azure fornece ferramentas de auditoria para registrar e monitorar tentativas de acesso aos recursos.
   - O uso do **Azure Monitor** e **Azure Security Center** pode ajudar a detectar atividades suspeitas.

### 6. **Privilégios Mínimos**
   - Aplique o princípio de **menor privilégio**, garantindo que os usuários tenham apenas as permissões necessárias para desempenhar suas funções, reduzindo o risco de acesso não autorizado.

## Como Configurar Políticas de Acesso no Portal Azure

1. **Acessar o Portal Azure**:
   - Faça login em [portal.azure.com](https://portal.azure.com).

2. **Gerenciar Acesso com RBAC**:
   - Navegue até o recurso desejado.
   - Selecione **"Controle de acesso (IAM)"**.
   - Adicione ou remova funções para usuários ou grupos conforme necessário.

3. **Configurar Azure AD**:
   - No painel, busque por **"Azure Active Directory"**.
   - Gerencie usuários e grupos, e configure políticas de autenticação.

4. **Criar Políticas de Acesso Condicional**:
   - Em **Azure AD**, vá até **"Segurança"** e selecione **"Acesso condicional"**.
   - Crie novas políticas definindo os usuários, condições e controles de acesso.

5. **Implementar MFA**:
   - No **Azure AD**, ative a autenticação multifatorial para aumentar a segurança nas contas.

6. **Monitorar e Auditar Acesso**:
   - Utilize o **Azure Monitor** para configurar alertas e monitorar logs de acesso.
   - Revise periodicamente os registros de auditoria para garantir conformidade.
