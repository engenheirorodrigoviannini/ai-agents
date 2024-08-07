# ai-agents
Sistema Automatizado de Respostas sobre Gerenciamento de Projetos com ChatGPT e Crew.AI

## Visão Geral

O projeto apresenta um sistema automatizado para gerenciamento de projetos, utilizando agentes de IA para planejar, redigir e editar respostas baseadas em um arquivo de texto. Este sistema é desenvolvido em Python e usa bibliotecas como `crewai`, `crewai_tools`, `langchain_community`, e `unidecode` para manipulação de dados e interação com a API do OpenAI.

## Storytelling do Código

O notebook `agente_de_projetos.ipynb` é projetado para automatizar o processo de gerenciamento de projetos por meio de três agentes de IA distintos: Planejador, Redator e Editor. O fluxo de trabalho começa com a instalação dos pacotes necessários e a configuração das variáveis de ambiente, incluindo a chave da API do OpenAI. O arquivo de texto contendo as respostas é formatado para garantir consistência e remover caracteres indesejados.

A seguir, três agentes são configurados:

1. **Planejador**: Cria um plano de conteúdo claro sobre um tópico específico.
2. **Redator**: Escreve uma resposta baseada no plano do Planejador.
3. **Editor**: Revisa a resposta para assegurar clareza e precisão.

O código inclui funções para formatar arquivos, buscar respostas e executar a equipe de agentes. Finalmente, o resultado é apresentado no Jupyter Notebook utilizando Markdown.

## Resumo em Tópicos

### Configuração Inicial

- **Instalação de Pacotes**:
  - `crewai`
  - `crewai_tools`
  - `langchain_community==0.0.29`
  - `unidecode`
  
- **Configuração de Variáveis de Ambiente**:
  - Leitura da chave API do OpenAI do arquivo `api_keys.txt`.
  - Configuração da variável `OPENAI_API_KEY`.

### Manipulação de Arquivos

- **Função `formatar_arquivo`**:
  - Formata o arquivo de texto para remover caracteres especiais e normalizar o formato.
  - Salva o conteúdo formatado em um novo arquivo.

- **Função `obter_resposta_do_arquivo`**:
  - Busca uma resposta para um tópico específico no arquivo formatado.

### Configuração dos Agentes

- **Planejador**:
  - Define o plano de conteúdo sobre o tópico.
  
- **Redator**:
  - Escreve a resposta baseada no plano.

- **Editor**:
  - Revisa a resposta para garantir clareza e precisão.

### Execução e Resultados

- **Função `executar_equipe_com_topico`**:
  - Executa a equipe de agentes para um tópico específico e combina a resposta do arquivo com o resultado da execução da equipe.
  
- **Exibição do Resultado**:
  - O resultado é exibido no Jupyter Notebook usando Markdown.

### Utilitários

- **Arquivo `utils.py`**:
  - Funções auxiliares para carregar variáveis de ambiente e formatar resultados.
