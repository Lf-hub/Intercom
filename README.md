# Controle de estoque
<p align="justify"> Este é o README do projeto "Controle de estoque". Descreve a estrutura e as funcionalidades do projeto, além de fornecer instruções sobre como configurar e executar o projeto localmente.</P>

## Descrição do Projeto:
Este projeto é uma aplicação web desenvolvida com Django que gerencia produtos e estoques. Os usuários podem criar, atualizar e excluir produtos, bem como registrar vendas de produtos. Além disso, os usuários podem visualizar uma lista de produtos disponíveis e obter detalhes específicos de cada produto.

### Funcionalidades
Exibição de lista de produtos
Criação de produtos
Atualização de produtos
Exclusão de produtos
Registro de vendas de produtos

### Requisitos do Sistema
<p align="justify"> Python 3.8 ou superior</p>
<p align="justify"> Django 3.2 ou superior</p>

### Configuração do Ambiente
- Clone o repositório do projeto:
    - git clone https://github.com/Lf-hub/intercom.git

- Crie e ative um ambiente virtual:
    - python3 -m venv env
    - source env/bin/activate

- Instale as dependências do projeto:
    - pip install -r requirements.txt

- Execute as migrações do banco de dados:
    - python manage.py migrate

- Crie um superusuário para acessar a área administrativa (opcional):
    - python manage.py createsuperuser

- Executando o Projeto
  <p align="justify"> Inicie o servidor de desenvolvimento do Django:</p>
     - python manage.py runserver

- Acesse a aplicação no navegador:
    - http://localhost:8000/

- Para acessar a área administrativa, adicione /admin ao final da URL:
    - http://localhost:8000/admin

### Dependências Externas
<p align="justify"> O projeto depende das seguintes bibliotecas externas:</p>

- Django: framework web utilizado para desenvolver a aplicação.
- Outras dependências listadas no arquivo requirements.txt.
<p align="justify"> Certifique-se de ter as dependências instaladas corretamente conforme mencionado nas etapas de configuração do ambiente.</p>

## Contribuição
<p align="justify"> Contribuições para este projeto são bem-vindas. Sinta-se à vontade para abrir issues relatando problemas, propor melhorias ou enviar pull requests com novos recursos ou correções de bugs.</p>

<p align="justify"> Certifique-se de seguir as diretrizes de contribuição do projeto e respeitar o código de conduta.</p>
