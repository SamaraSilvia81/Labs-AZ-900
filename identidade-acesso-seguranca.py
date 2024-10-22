# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um serviço ou ferramenta e retornar sua respectiva descrição.
def associar_recurso(recurso):
    if recurso == "Microsoft Entra ID":
        return "Serviço de gerenciamento de identidades e acessos"
    
    elif recurso == "Multi-Factor Authentication":
        return "Proporciona uma camada adicional de segurança"
    
    elif recurso == "Azure Role-Based Access Control":
        return "Possibilita um gerenciamento de acesso refinado dos recursos"
    
    elif recurso == "Azure Security Center":
        return "Oferece visibilidade e controle sobre a segurança dos recursos"
    
    elif recurso == "Azure Key Vault":
        return "Permite armazenar e acessar segredos de maneira segura"
    
    else:
        return "Recurso desconhecido"

# Chama a função e imprime a descrição correspondente
print(associar_recurso(entrada))
