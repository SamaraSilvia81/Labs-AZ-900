# Introdução à computação em nuvem AZURE
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

> A computação em nuvem refere-se ao fornecimento de serviços de computação via internet, permitindo inovações rápidas, flexibilidade e economias de escala.

Para configurar arquiteturas no **Azure Portal** e criar recursos como máquinas virtuais, bancos de dados ou redes, há uma série de etapas e recursos a serem considerados. Aqui está um resumo de como configurar uma arquitetura no Azure Portal, com ênfase na criação de recursos e marcações (tags):

### 1. **Planejamento da Arquitetura**
   - **Definir os requisitos**: Antes de iniciar, é importante planejar a arquitetura que melhor atenda às suas necessidades, seja pública, privada ou híbrida.
   - **Escolher os recursos principais**: Decida quais recursos serão implementados, como máquinas virtuais (VMs), banco de dados SQL, redes virtuais e serviços de armazenamento.

### 2. **Criação de Grupos de Recursos**
   - Um **grupo de recursos** no Azure é o primeiro passo para organizar e gerenciar os recursos associados. 
     - Acesse o **Azure Portal** e vá até a aba “Grupos de Recursos”.
     - Clique em “+ Criar” para configurar um grupo, definindo o nome e a região.
     - Escolha a **região** onde seus recursos serão hospedados.

### 3. **Criação de Recursos**
   - Após criar o grupo, você pode adicionar recursos como VMs, bancos de dados ou redes:
     - Vá ao grupo de recursos criado e selecione “+ Adicionar”.
     - Escolha o tipo de recurso que deseja, como uma **Máquina Virtual (VM)**, **Banco de Dados SQL** ou **Rede Virtual**.
     - Preencha as configurações, como **tamanho da VM**, **imagem** (por exemplo, Windows ou Linux), **CPU**, **RAM** e **armazenamento** para máquinas virtuais.
     - Para bancos de dados, configure os parâmetros como **tipo de banco** (SQL, PostgreSQL), **preço** e **tamanho de armazenamento**.
     - Para redes, configure **sub-redes**, **endereço IP** e políticas de segurança de rede.

### 4. **Uso de Modelos ARM (Azure Resource Manager)**
   - O **Azure Resource Manager (ARM)** permite a implementação automatizada e replicável de recursos usando templates (modelos) JSON.
     - Você pode acessar templates prontos ou criar o seu próprio para definir a arquitetura completa com todos os recursos necessários, como VMs, redes e regras de segurança.
     - Isso é útil para implementar arquiteturas complexas de forma consistente em várias regiões ou projetos.

### 5. **Configuração de Redes e Segurança**
   - Ao configurar uma arquitetura, a criação de **Redes Virtuais (VNets)** é essencial para interconectar seus recursos:
     - Acesse **Rede Virtual** no portal, crie uma nova rede e defina o intervalo de IP.
     - Crie **Sub-redes** para diferentes camadas de aplicação (web, banco de dados) e configure **regras de segurança de rede (NSG)** para controlar o tráfego.
     - Adicione **Balanceadores de Carga** e **Gateways de Aplicação** para distribuição de tráfego e escalabilidade.

### 6. **Marcação de Recursos (Tags)**
   - As **tags** no Azure ajudam a organizar, rastrear e gerenciar recursos com mais facilidade, especialmente em grandes ambientes:
     - Durante a criação ou após a implementação de um recurso, vá até a seção “Tags”.
     - Adicione **chaves** e **valores** para identificar recursos por projetos, departamentos, custos ou outras categorias relevantes. Exemplo: `Projeto: Ecommerce`, `Ambiente: Produção`.
     - Isso facilita a gestão de custos e conformidade, permitindo relatórios detalhados por grupos de tags.

### 7. **Gerenciamento e Monitoramento**
   - Depois de configurados os recursos, o Azure oferece ferramentas integradas para gerenciar e monitorar a infraestrutura:
     - Utilize o **Azure Monitor** para acompanhar o desempenho dos recursos em tempo real.
     - Configure **alertas** e **métricas** personalizadas para detectar anomalias e tomar ações corretivas.
     - Implemente **Azure Policies** para garantir que seus recursos estejam em conformidade com as melhores práticas de governança e segurança.

### 8. **Automação e Escalabilidade**
   - Use **Azure Autoscale** para ajustar automaticamente a capacidade dos recursos de acordo com a demanda.
     - Configure regras de escalabilidade que aumentam ou diminuem a quantidade de VMs ou outros serviços conforme a carga de trabalho.
     - Adicione **Azure Automation** para automatizar tarefas repetitivas, como backups e atualizações de segurança.

A **implementação** no **Azure Portal** é uma etapa crítica após o planejamento e configuração da arquitetura. Ela envolve a disponibilização e operacionalização dos recursos criados, garantindo que eles estejam prontos para uso e integração com outros serviços. A seguir, está o resumo do processo de **implementação** no Azure:

### 1. **Escolha dos Recursos a Implementar**
   - Durante a fase de planejamento, você decide quais serviços ou recursos vão compor sua arquitetura.
   - Alguns exemplos comuns de recursos implementados no Azure incluem:
     - **Máquinas Virtuais (VMs)**
     - **Bancos de Dados (SQL, MySQL, PostgreSQL)**
     - **Serviços de Armazenamento (Blob Storage, Discos Gerenciados)**
     - **Redes Virtuais (VNet) e Sub-redes**
     - **Gateways de Aplicação** e **Balanceadores de Carga**

### 2. **Implantação de Recursos Usando ARM Templates**
   - Uma maneira eficiente de implementar vários recursos de uma só vez é usando **Azure Resource Manager (ARM) Templates**.
     - **Criação de um template**: Um arquivo JSON define todos os recursos e suas configurações.
     - **Implementação automatizada**: Ao executar o template, o Azure provisiona todos os serviços especificados de forma consistente e replicável.
     - Ideal para arquiteturas complexas ou para implementar em vários ambientes (desenvolvimento, produção).

### 3. **Implementação Manual via Azure Portal**
   - Para implantações menores ou mais simples, você pode criar e implantar recursos diretamente pelo **Azure Portal**:
     - **Máquinas Virtuais (VMs)**:
       - Defina o sistema operacional, CPU, memória e configurações de armazenamento.
       - Após a criação, a VM é automaticamente inicializada e fica disponível para uso.
     - **Bancos de Dados**:
       - Configure instâncias de banco de dados (SQL, PostgreSQL) escolhendo a versão, escalabilidade e tamanho.
       - Após a implementação, você pode acessar o banco por meio de conexões seguras, configurar usuários e permissões.

### 4. **Gerenciamento de Infraestrutura**
   - Uma parte importante da implementação é garantir que os recursos estejam devidamente gerenciados e integrados:
     - **Balanceadores de Carga**: Após implementar várias VMs, configure um balanceador de carga para distribuir tráfego entre elas, garantindo alta disponibilidade.
     - **Rede Virtual e NSG (Network Security Groups)**: Durante a implementação, defina regras de segurança para controlar o acesso entre as diferentes camadas da arquitetura.
     - **Storage Accounts**: Implante contas de armazenamento para dados de logs, backups ou arquivos, integrando-as com as máquinas virtuais e bancos de dados.

### 5. **Automação e Pipelines de Implementação**
   - Após a configuração inicial, você pode usar o **Azure DevOps** ou **GitHub Actions** para automatizar a implementação contínua:
     - Crie **pipelines CI/CD** para automatizar a implementação de atualizações ou novos recursos.
     - Utilize **Scripts PowerShell ou CLI** para implantar recursos em massa ou fazer modificações rápidas.

### 6. **Implementação de Aplicações e Integrações**
   - Além de infraestrutura, você pode implementar **aplicações** diretamente no Azure:
     - **Azure App Services** para hospedar aplicativos web, APIs e microsserviços.
     - **Contêineres com Azure Kubernetes Service (AKS)** para implantar e gerenciar aplicações em contêineres de forma escalável.
     - Após a implementação, configure as conexões e integrações com bancos de dados, filas de mensagens ou outros serviços.

### 7. **Governança e Compliance Durante a Implementação**
   - Durante o processo de implementação, aplicar **políticas de governança** é essencial para garantir que os recursos estejam em conformidade:
     - Utilize **Azure Policy** para definir restrições e regras que os recursos devem seguir (por exemplo, definir uma política que impeça a criação de VMs fora de uma determinada região).
     - **Auditoria**: Monitore e audite a implementação para garantir que todas as práticas de segurança e conformidade sejam seguidas.

### 8. **Marcação (Tagging) e Gerenciamento de Custos**
   - Durante a implementação de recursos, é importante utilizar **marcações (tags)** para facilitar o gerenciamento:
     - Aplique **tags** em recursos durante ou após a implementação para categorizar e organizar por departamento, projeto ou ambiente (produção/desenvolvimento).
     - Isso ajuda no controle de **custos** e permite a geração de relatórios detalhados sobre como os recursos estão sendo utilizados.

### 9. **Implementação de SLAs**
   - Durante a implementação, também é essencial garantir que os recursos cumpram os **Acordos de Nível de Serviço (SLA)**:
     - Azure oferece SLAs para alta disponibilidade e desempenho, como VMs com SLA de 99,9% de disponibilidade.
     - Configure redundância e backup adequados para garantir que a implementação de seus recursos atenda a esses SLAs.

### 10. **Monitoramento e Ajustes Pós-Implementação**
   - Após a implementação, use **Azure Monitor** e **Application Insights** para monitorar o desempenho e a disponibilidade dos recursos.
   - Configure alertas para eventuais problemas de desempenho ou disponibilidade e automatize o ajuste de escala ou a criação de novos recursos conforme necessário.

Essas etapas de **implementação** garantem que seus recursos estejam totalmente funcionais, integrados e monitorados no ambiente do Azure, oferecendo flexibilidade, controle e suporte à governança de TI.
