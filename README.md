# Gestão Financeira
Essa API é uma aplicação para gestão financeira, contendo débitos, créditos, cadastro de contas, cálculo de balanço, gráficos, etc.

# Funcionalidades
1. Criar de Conta
2. Excluir conta
3. Calcular o balanço individual de cada conta
4. Cadastrar débitos às contas
5. Cadastrar créditos às contas
6. Visualizar relação entre as contas por gráfico geral

# Endpoints
1. Accounts
"/accounts/" (POST, GET) - Visualização das contas, recebe uma lista com todas as contas para criação do gráfico e/ou de novas contas
"/accounts/{account_id}/" (GET/DELETE) - Manipulação das contas, recebe contas individualmente e/ou exclui
Todas as funcionalidades da aba Contas

2. Credits
"/credits/" (POST, GET) - Visualização dos créditos, recebe uma lista com todos os créditos para criação de novos.
"/credits/{credit_id}/" (GET/DELETE) -  Manipulação dos créditos,  recebe créditos individualmente e/ou exclui
Todas as funcionalidades da aba Créditos

4. Debits
"/debits/" (POST, GET) - Visualização dos débitos, recebe uma lista com todos os débitos para criação de novos.
"/debits/{debit_id}/" (GET/DELETE) -  Manipulação dos débitos,  recebe débitos individualmente e/ou exclui
Todas as funcionalidades da aba Débitos

# Instalação
1. pip install -r requirements.txt ou (pip install uvicorn fastapi sqlalchemy motor pymongo jinja2 pydantic alembic)
2. python -m uvicorn app.main:app --reload
