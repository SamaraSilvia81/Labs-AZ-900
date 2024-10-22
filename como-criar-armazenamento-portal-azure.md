![post_thumbnail-0fb93e0cf06d246f91f5f9fb2651e91d](https://github.com/user-attachments/assets/f1781532-be6b-4e07-9720-f9f5fc523867)

# Armazenamento na Azure
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

> A computação em nuvem refere-se ao fornecimento de serviços de computação via internet, permitindo inovações rápidas, flexibilidade e economias de escala.

## Como Funciona o Armazenamento na plataforma Azure ?
> O **armazenamento no Azure** é um dos pilares fundamentais da infraestrutura na nuvem, oferecendo uma ampla gama de soluções para diferentes tipos de dados e cenários. No **Azure Portal**, você pode gerenciar, configurar e monitorar diversos tipos de armazenamento que atendem a necessidades variadas de performance, custo e acessibilidade.

### 1. **Tipos de Armazenamento no Azure**
   - **Azure Blob Storage**: Serviço de armazenamento de objetos otimizado para dados não estruturados, como arquivos de mídia, backups e logs. O Blob Storage oferece:
     - **Camadas de acesso**: Hot (frequente), Cool (menos frequente) e Archive (raramente acessado), permitindo otimização de custos.
     - Suporte para grandes volumes de dados e integração com outros serviços, como **Azure Data Lake**.
   
   - **Azure Files**: Serviço de compartilhamento de arquivos em SMB (Server Message Block) ou NFS (Network File System), similar a um sistema de arquivos tradicional. Ideal para cenários de migração de arquivos corporativos e compartilhamento em rede.
     - Suporte para **montagem** em VMs e servidores on-premises.
   
   - **Azure Disk Storage**: Armazenamento persistente de alto desempenho para VMs (Managed Disks). Disponível em discos SSD (Premium, Standard) e HDD, atendendo a diferentes necessidades de performance.
   
   - **Azure Table Storage**: Armazenamento NoSQL para grandes volumes de dados estruturados em formato chave-valor. Ideal para armazenar dados não relacionais de forma rápida e escalável.
   
   - **Azure Queue Storage**: Usado para filas de mensagens em sistemas distribuídos, ajudando a desacoplar componentes e permitindo a comunicação assíncrona entre serviços.

### 2. **Configuração de Contas de Armazenamento**
   - **Criação de uma conta de armazenamento**:
     - No portal, navegue até "Armazenamento" e crie uma nova **Conta de Armazenamento**.
     - Escolha o tipo de conta (Geral v2 ou Blob Storage), a região, desempenho (Standard ou Premium) e redundância (LRS, ZRS, GRS, RA-GRS).
     - A conta serve como container principal para armazenar Blobs, arquivos, tabelas e filas.

   - **Redundância de Dados**:
     - **LRS (Local Redundant Storage)**: Mantém três cópias dos dados em um único datacenter.
     - **ZRS (Zone Redundant Storage)**: Replica dados entre várias zonas dentro de uma região.
     - **GRS (Geo-Redundant Storage)**: Replica dados para outra região geograficamente distante, garantindo alta disponibilidade em caso de falhas regionais.
     - **RA-GRS (Read-Access Geo-Redundant Storage)**: Similar ao GRS, mas com acesso de leitura à região secundária.

### 3. **Segurança e Controle de Acesso**
   - **Autenticação e Controle de Acesso**:
     - **Azure Active Directory (Azure AD)** pode ser utilizado para gerenciar permissões de acesso aos dados, definindo quem pode criar, ler, atualizar ou excluir dados.
     - Suporte para **Shared Access Signatures (SAS)**, permitindo o controle granular de acesso aos recursos por meio de tokens temporários.
     - **Criptografia**: Todos os dados são criptografados em repouso e podem ser criptografados em trânsito usando HTTPS.

   - **Firewalls e Redes Virtuais**:
     - A conta de armazenamento pode ser configurada para permitir o acesso apenas de endereços IP específicos ou redes virtuais seguras, garantindo isolamento de segurança.

### 4. **Monitoramento e Gerenciamento**
   - **Azure Monitor e Logs**: Permite monitorar o uso do armazenamento, taxa de acesso, operações realizadas e métricas de desempenho em tempo real.
   - **Azure Storage Explorer**: Ferramenta gráfica que facilita o gerenciamento de arquivos e objetos dentro da conta de armazenamento, permitindo uploads, downloads e edição de permissões.

### 5. **Escalabilidade e Desempenho**
   - O armazenamento no Azure é altamente escalável, com a capacidade de armazenar desde pequenos volumes até petabytes de dados. Você pode ajustar automaticamente entre camadas de acesso ou adicionar mais recursos de disco conforme necessário.
   - **Throttling** e limites podem ser configurados para controlar o desempenho, garantindo que cargas de trabalho mais pesadas não impactem o ambiente.

### 6. **Backup e Recuperação**
   - **Azure Backup** e **Snapshot** permitem realizar backups automáticos e manuais de discos e dados armazenados.
   - **Versionamento** e **soft delete** no Blob Storage garantem a proteção contra exclusão acidental.

### 7. **Custo**
   - O custo do armazenamento no Azure é baseado no tipo de armazenamento escolhido, volume de dados armazenados, operações de leitura e escrita, além da camada de acesso.
   - Ferramentas como o **Azure Cost Management** ajudam a controlar e prever os gastos com armazenamento, ajustando conforme o uso e demanda.

### 8. **Implementação de Armazenamento via Infraestrutura como Código**
   - Você pode usar **ARM Templates**, **Azure CLI** ou **PowerShell** para automatizar a criação e configuração de contas de armazenamento, além de serviços associados, garantindo consistência e eficiência na implantação de infraestrutura.
   - 
Esses recursos tornam o **armazenamento no Azure** flexível, seguro e escalável, oferecendo soluções tanto para dados não estruturados quanto estruturados, com opções robustas de segurança e gerenciamento para atender a diferentes necessidades de negócios.

## Como Criar o Armazenamento na plataforma Azure 

1. **Acessar o Portal**:
   - Entre no [Azure Portal](https://portal.azure.com/).
2. **Navegar até o Armazenamento**:
   - No menu lateral, clique em "**Criar um recurso**" e procure por "**Armazenamento**" ou diretamente "**Conta de Armazenamento**".
   - Selecione "**Conta de Armazenamento**" e clique em "**Criar**".
3. **Configuração Básica**:
   - **Assinatura**: Escolha a assinatura ativa que será cobrada pelo recurso.
   - **Grupo de Recursos**: Selecione um grupo de recursos existente ou crie um novo para organizar os recursos.
   - **Nome da Conta de Armazenamento**: Escolha um nome exclusivo para a conta de armazenamento.
   - **Região**: Escolha a região onde os dados serão armazenados.
   - **Performance**: Escolha entre **Standard** (discos HDD, mais baratos e para armazenamento geral) ou **Premium** (discos SSD, com maior desempenho para workloads críticos).
   - **Redundância**: Escolha a redundância (LRS, ZRS, GRS, RA-GRS) dependendo das suas necessidades de recuperação e replicação de dados.
4. **Opções Avançadas**:
   - Escolha criptografia, segurança, permissões e redes de acesso. Você pode habilitar firewalls, limitar endereços IP que podem acessar os dados e integrar com redes virtuais.
5. **Tags (Marcação)**:
   - Adicione **tags** para facilitar o gerenciamento e a categorização dos recursos (como departamento, ambiente, etc.).
6. **Revisar e Criar**:
   - Após configurar, clique em "**Revisar + Criar**" para revisar as opções escolhidas. Em seguida, clique em "**Criar**".

Após alguns minutos, a conta de armazenamento será criada e você poderá gerenciar os dados (Blobs, Arquivos, Discos) diretamente pelo portal ou ferramentas de linha de comando.

### Automação e Infraestrutura como Código:
- **Azure CLI/PowerShell**: Você pode criar contas de armazenamento diretamente da linha de comando, facilitando a automação em larga escala.
- **ARM Templates**: Você pode criar templates JSON que descrevem a infraestrutura e, assim, criar instâncias de armazenamento em massa ou como parte de soluções maiores.
### Recursos adicionais:
- Criar **Containers** no Blob Storage.
- Criar **Shares** no Azure Files para compartilhamento de arquivos.
- Configurar **Snapshots** e backups automáticos para dados críticos.
