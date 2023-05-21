# RecMovies

## Rodar projeto
~~~
git clone https://github.com/marcelo-mascarenhas/TP-Eng-Soft2.git
cd TP-Eng-Soft2/
~~~
Para rodar aplicação abra os diretórios do front (client) e do back (backend) em terminais separados.

### No terminal do frontend (client):

1) Execute o comando `npm i`  para instalar todas as dependências necessárias.

2) Em seguida, inicie o aplicativo:
    ~~~
    npm run dev
    ~~~
    
### No terminal do backend:

1) Instale o Pipenv usando pip (pode ser necessário usar pip3 em vez de pip):   
  
    ~~~
    pip install pipenv 
    ~~~

2) Ative um novo ambiente virtual:

    ~~~
    pipenv shell
    ~~~

3) Execute o comando para baixar as dependências:

    ~~~
    pipenv install -r requirements.txt
    ~~~

4) Execute o django:

    ~~~
    python manage.py runserver
    ~~~
    
### Testes

 1) Para executar os testes de unidade do backend, entre na pasta 'backend' e execute o seguinte comando: 

    ~~~
    pytest -m 'unit'
    ~~~

 2) Para executar os testes de unidade, entre na pasta 'client' e execute o seguinte comando:
    
    ~~~
    npm test
    ~~~

## Equipe

  Asafe Clemente Gadelha de Medeiros - 2019006434
  
  Helio Victor Flexa dos Santos - 2019006680
  
  Henrique Magalhães de Oliveira Carvalho - 2019006698
   
  Marcelo Mascarenhas Ribeiro de Araújo - 2019110053

  Matheus Prado Miranda - 2019007023

  
**Objetivo do Sistema:** Plataforma de recomendação que implementa uma interface de avaliação, recomendação e visualização, no domínio de filmes.

## Principais Features

<ol>
  <li>Buscar filmes, fornecendo um conjunto de filtros para o usuário, e.g filtrar por gênero, por nota, etc..</li>
  <li>Listar filmes recomendados com base nos indicados pelo usuário.</li>
  <li>Sistema de cadastro para salvar informações e filmes.</li>
  <li>Mostrar informações de filmes selecionados.</li>
</ol>

## Possíveis Tecnologias

<ol>
  <li>Database: SQL</li>
  <li>Back-end: Django</li>
  <li>Front-end: React</li>
</ol>

## Backlog do Produto e do Sprint

### SPRINT 1

- Tarefas Técnicas
    - Preparar ambiente de desenvolvimento ( VSCode, Dependências ) \[ Asafe, Helio, Marcelo, Matheus ]
    - Projetar e implementar o banco de dados \[ Helio ]
    - Projetar o Crawler e popular o banco de dados \[ Helio ]

- História: Como usuário do sistema, eu quero buscar filmes e acessar suas informações.
- Tarefas:
    - Projetar e implementar a interface web \[ Asafe ]
    - Criar rotas entre banco de dados e interface web \[ Matheus / Marcelo ]

- História: Como usuário do sistema, eu quero receber recomendações de filmes similares ao filme buscado.
- Tarefas: 
    - Implementar a interface web \[ Asafe ]
    - Projetar e treinar o recomendador \[ Marcelo / Matheus]
    - Salvar o modelo de recomendação \[ Marcelo / Matheus]
    - Implementar o modelo no servidor \[ Marcelo / Matheus]

- História: Como usuário do sistema, eu quero salvar um filme para visualização posterior.
- Tarefas: 
    - Implementar a interface web \[ Asafe ]
    - Criar sistema de armazenamento no cache do navegador \[ Matheus / Marcelo]

- História: Como usuário do sistema, eu quero visualizar os filmes mais populares.
- Tarefas: 
    - Implementar a interface web \[ Asafe ]
    - Criar rotas entre banco de dados e interface web \[ Matheus / Marcelo]
    
    
### SPRINT 2


- Tarefas Técnicas
    - Rodar a ferramenta Lizard para obter o relatório do sistema \[ Asafe, Helio, Marcelo, Matheus ]
    - Refatorar funções mais complexas do sistema \[ Asafe, Helio, Marcelo, Matheus ]
    
### SPRINT 3

- Tarefas Técnicas
    - Desenvolver testes de unidade para o back-end \[Henrique, Marcelo, Matheus ]
    - Desenvolver testes de unidade para o front-end \[ Asafe, Helio ]   

