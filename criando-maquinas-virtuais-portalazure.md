![post_thumbnail-0fb93e0cf06d246f91f5f9fb2651e91d](https://github.com/user-attachments/assets/f1781532-be6b-4e07-9720-f9f5fc523867)

# Configurando Recursos e Dimensionamentos em Máquinas Virtuais na Azure
![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=23232e&style=for-the-badge)

### Configurando Recursos e Dimensionamentos em Máquinas Virtuais no Azure

#### 1. **Criar uma Máquina Virtual**

- **Acesso ao Portal**: Entre no [Azure Portal](https://portal.azure.com/).
- **Criar um Recurso**: Clique em "**Criar um recurso**" e selecione "**Máquina Virtual**".
- **Configurações Básicas**:
  - **Assinatura**: Selecione a assinatura que será usada.
  - **Grupo de Recursos**: Escolha um grupo de recursos existente ou crie um novo.
  - **Nome da VM**: Dê um nome à sua máquina virtual.
  - **Região**: Escolha a região onde a VM será hospedada.
  - **Imagem**: Selecione o sistema operacional que deseja usar (Windows, Linux, etc.).
  - **Tamanho**: Escolha a SKU (tamanho da VM) que determina os recursos como CPU e memória.

#### 2. **Configuração de Recursos**

- **Tamanho da VM**:
  - O Azure oferece diferentes tamanhos de VM, permitindo que você selecione a combinação ideal de CPU, memória e armazenamento. O portal fornece informações sobre as capacidades e preços de cada tamanho.
  
- **Armazenamento**:
  - **Discos**: Configure o disco do sistema operacional e discos adicionais, se necessário. Você pode escolher entre discos SSD e HDD, além de definir opções de redundância.
  
- **Rede**:
  - Defina as configurações de rede, como grupos de segurança de rede (NSGs) e IPs públicos ou privados.
  
- **Gerenciamento**:
  - Configure as opções de monitoramento, como o **Azure Monitor**, que fornece insights sobre o desempenho da VM.

#### 3. **Dimensionamento de Máquinas Virtuais**

- **Dimensionamento Vertical**:
  - Você pode alterar o tamanho da VM no portal a qualquer momento. Para isso, vá até a seção "**Configurações**" da sua VM, clique em "**Tamanho**" e escolha um novo tamanho.
  
- **Dimensionamento Horizontal**:
  - Em vez de aumentar o tamanho da VM, você pode criar várias VMs do mesmo tipo (escala horizontal) para atender a cargas de trabalho maiores. Isso é especialmente útil em aplicativos distribuídos.

#### 4. **Automação de Dimensionamento**

- **Azure Scale Sets**:
  - Utilize os **Azure Virtual Machine Scale Sets** para gerenciar um grupo de VMs idênticas que podem ser dimensionadas automaticamente com base na demanda.

- **Regras de Escalonamento Automático**:
  - Configure regras para aumentar ou diminuir automaticamente o número de VMs com base em métricas de desempenho (como uso de CPU ou tráfego de rede).

### Considerações Finais

- O Azure oferece uma interface amigável para gerenciar e dimensionar suas VMs, além de opções de automação para escalabilidade eficiente.
- Sempre monitore o desempenho e os custos associados às VMs para otimizar o uso de recursos e evitar surpresas na fatura.
