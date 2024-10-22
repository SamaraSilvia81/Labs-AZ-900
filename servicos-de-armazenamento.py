# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um serviço de armazenamento e retornar sua respectiva descrição.
def identificar_servico_armazenamento(servico):
    if servico == "Blob do Azure":
        return "Armazenamento de arquivos grandes e não estruturados"
    
    elif servico == "Disco do Azure":
        return "Armazenamento de alto desempenho para máquinas virtuais"
    
    elif servico == "Fila do Azure":
        return "Armazenamento de mensagens para comunicação entre aplicações"
    
    elif servico == "Arquivos do Azure":
        return "Armazenamento de arquivos compartilhados acessíveis por meio de SMB"
    
    elif servico == "Tabelas do Azure":
        return "Armazenamento de dados estruturados não relacionais em tabelas"
    
    else:
        return "Serviço desconhecido"

# Chama a função e imprime a descrição correspondente
print(identificar_servico_armazenamento(entrada))
