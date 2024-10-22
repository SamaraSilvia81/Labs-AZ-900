![post_thumbnail-0fb93e0cf06d246f91f5f9fb2651e91d](https://github.com/user-attachments/assets/f1781532-be6b-4e07-9720-f9f5fc523867)

# Entendendo sobre Segurança e Identidade na Azure
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

## Como funciona ??

### 1. **Segurança em Nuvem**

A segurança na Azure é uma prioridade, oferecendo uma série de ferramentas e práticas para proteger os dados, aplicativos e a infraestrutura. A Microsoft investe significativamente em segurança, garantindo que os dados sejam protegidos em várias camadas.

### 2. **Controle de Acesso e Identidade**

- **Azure Active Directory (Azure AD)**: 
  - É o serviço de gerenciamento de identidade e acesso da Microsoft. Permite que você gerencie usuários e grupos, além de fornecer autenticação e autorização para aplicativos.
  - Suporta autenticação multifator (MFA), proporcionando uma camada extra de segurança.

- **Controle de Acesso Baseado em Funções (RBAC)**: 
  - Permite atribuir permissões específicas a usuários ou grupos com base em funções definidas. Isso garante que os usuários tenham acesso apenas aos recursos necessários para suas funções.

### 3. **Segurança de Dados**

- **Criptografia**:
  - Os dados em trânsito e em repouso podem ser criptografados usando ferramentas como o **Azure Storage Service Encryption** e o **Azure Key Vault**, que gerencia chaves de criptografia e segredos.

- **Azure Security Center**:
  - Fornece uma visão unificada da segurança de seus recursos em nuvem. Ele oferece recomendações de segurança, alertas e a capacidade de gerenciar a conformidade.

### 4. **Proteção de Aplicativos**

- **Web Application Firewall (WAF)**:
  - Protege aplicativos web contra ameaças comuns, como ataques de injeção e negação de serviço (DDoS).

- **Azure Sentinel**:
  - É uma solução de gerenciamento de informações e eventos de segurança (SIEM) que usa inteligência artificial para detectar e responder a ameaças em tempo real.

### 5. **Conformidade e Governança**

- **Azure Policy**:
  - Permite implementar regras e efeitos em seus recursos Azure, garantindo que as configurações atendam às diretrizes e padrões de conformidade.

- **Gerenciamento de Identidade e Acesso (IAM)**:
  - Fornece ferramentas para monitorar e gerenciar as permissões de acesso dos usuários, garantindo que as políticas de segurança estejam em conformidade com as normas e regulamentos.

Aqui está um resumo sobre como configurar segurança e identidade no Azure através do portal:

## Configurando Segurança e Identidade no Portal Azure

### 1. **Configuração do Azure Active Directory (Azure AD)**

- **Acessar o Azure AD**:
  1. No portal Azure, navegue até "Azure Active Directory" no menu lateral.
  
- **Criar Usuários e Grupos**:
  1. Para adicionar um usuário, clique em **Usuários** > **Novo Usuário**.
  2. Preencha os detalhes, como nome, sobrenome e endereço de e-mail.
  3. Para criar um grupo, vá em **Grupos** > **Novo Grupo** e configure as permissões conforme necessário.

- **Ativar a Autenticação Multifator (MFA)**:
  1. No Azure AD, vá até **Usuários** > **Usuários Multi-Fator**.
  2. Selecione os usuários para os quais deseja habilitar a MFA e siga as instruções para configurar.

### 2. **Configuração de Controle de Acesso Baseado em Funções (RBAC)**

- **Atribuir Funções**:
  1. Navegue até o recurso (como uma Máquina Virtual) no portal.
  2. Clique em **Controle de Acesso (IAM)** no menu do recurso.
  3. Clique em **Adicionar** e selecione **Adicionar atribuição de função**.
  4. Escolha uma função, como "Leitor" ou "Contribuidor", e atribua-a a um usuário ou grupo específico.

### 3. **Gerenciamento de Segurança dos Dados**

- **Configurar Criptografia**:
  1. Para criptografia em Azure Storage, vá para o serviço de armazenamento desejado.
  2. Clique em **Configurações** > **Criptografia** e habilite a criptografia de dados em repouso.

- **Gerenciar Chaves no Azure Key Vault**:
  1. Crie um **Key Vault** navegando até **Todos os serviços** > **Key Vaults** > **Adicionar**.
  2. Após criar, você pode adicionar chaves, segredos e certificados que podem ser usados para criptografar dados.

### 4. **Implementação de Proteção de Aplicativos**

- **Configurar o Web Application Firewall (WAF)**:
  1. No portal, acesse **Aplicativos** e selecione seu aplicativo web.
  2. Configure o WAF através das configurações de **Firewall** e ajuste as regras conforme necessário.

- **Habilitar Azure Sentinel**:
  1. Navegue até **Azure Sentinel** no portal.
  2. Crie uma nova instância e conecte suas fontes de dados para monitoramento de segurança.

### 5. **Gerenciamento de Conformidade e Governança**

- **Criar Políticas com Azure Policy**:
  1. Acesse **Azure Policy** no portal.
  2. Clique em **Criar Política** e escolha um modelo para definir as regras de conformidade.

- **Gerenciar IAM**:
  1. Acesse **Identidade** no portal.
  2. Use as configurações de **Controle de Acesso (IAM)** para revisar e ajustar as permissões de acesso de usuários e grupos.
