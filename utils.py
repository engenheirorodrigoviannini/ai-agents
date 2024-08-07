# Adicione suas utilidades ou funções auxiliares a este arquivo.

import os  # Importa o módulo 'os' para interação com o sistema operacional.
from dotenv import load_dotenv, find_dotenv  # Importa funções da biblioteca 'dotenv' para carregar variáveis de ambiente de um arquivo .env.

# Essas funções esperam encontrar um arquivo .env no diretório acima do script. 
# O formato desse arquivo é (sem o comentário):
# API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService

def load_env():
    """
    Carrega variáveis de ambiente do arquivo .env localizado no diretório acima do script.
    """
    _ = load_dotenv(find_dotenv())  # Carrega as variáveis de ambiente do arquivo .env encontrado.

def get_openai_api_key():
    """
    Obtém a chave da API do OpenAI a partir das variáveis de ambiente.
    
    Returns:
        str: A chave da API do OpenAI.
    """
    load_env()  # Carrega as variáveis de ambiente.
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Obtém o valor da variável de ambiente 'OPENAI_API_KEY'.
    return openai_api_key  # Retorna a chave da API do OpenAI.

def get_serper_api_key():
    """
    Obtém a chave da API do Serper a partir das variáveis de ambiente.
    
    Returns:
        str: A chave da API do Serper.
    """
    load_env()  # Carrega as variáveis de ambiente.
    serper_api_key = os.getenv("SERPER_API_KEY")  # Obtém o valor da variável de ambiente 'SERPER_API_KEY'.
    return serper_api_key  # Retorna a chave da API do Serper.

# # Quebra linhas com mais de 80 caracteres em várias linhas, não quebrando no meio de uma palavra.
# def pretty_print_result(result):
#     """
#     Formata o texto para que nenhuma linha tenha mais de 80 caracteres, quebrando as linhas conforme necessário.
    
#     Args:
#         result (str): O texto a ser formatado.
    
#     Returns:
#         str: O texto formatado com quebras de linha apropriadas.
#     """
#     parsed_result = []  # Lista para armazenar as linhas formatadas.
#     for line in result.split('\n'):  # Itera sobre cada linha do texto original.
#         if len(line) > 80:  # Verifica se a linha tem mais de 80 caracteres.
#             words = line.split(' ')  # Divide a linha em palavras.
#             new_line = ''  # Variável para construir a nova linha formatada.
#             for word in words:  # Itera sobre cada palavra.
#                 if len(new_line) + len(word) + 1 > 80:  # Verifica se adicionar a palavra excede o limite de 80 caracteres.
#                     parsed_result.append(new_line)  # Adiciona a linha atual à lista de resultados.
#                     new_line = word  # Inicia uma nova linha com a palavra atual.
#                 else:
#                     if new_line == '':
#                         new_line = word  # Se a linha estiver vazia, adiciona a primeira palavra.
#                     else:
#                         new_line += ' ' + word  # Caso contrário, adiciona a palavra com um espaço antes dela.
#             parsed_result.append(new_line)  # Adiciona a última linha formatada à lista de resultados.
#         else:
#             parsed_result.append(line)  # Adiciona linhas que têm 80 caracteres ou menos diretamente à lista de resultados.
#     return "\n".join(parsed_result)  # Junta as linhas formatadas em uma única string com quebras de linha.
