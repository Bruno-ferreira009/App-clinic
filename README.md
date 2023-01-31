# Medicar backend API
This repo contains a project api.

## Como rodar o projeto

steps:

Create a VirtualEnvironment

Install requirements:
```
$ pip install -r requirements.txt
```

Create a .env and set database configuration or set a default in settings.py

Run migrates in database:
```
$ python manager.py migrate
```

Create a superuser to access /admin:
```
$ python manager.py createsuperuser
```

Run application:
```
$ python manage.py runserver
```

1° Usuário (com DRF)
```
GET /aplicativo => vem todos aplicativos
GET /aplicativo/descricao => vem o detalhamento do que se trata o aplicativo

GET /especialidade => vem a especialidade *ex "Fisioterapia pelvica", "Fisioterapia/pilates".

GET /cliente => Vem todos os clientes;
GET /cliente/:clienteID => Vem o cliente com o id passado na url;

GET /agenda => vem todos os agendamentos.
GET /agenda/agenda:ID => vem cliente com id relacionado ao agendamento.

POST / => Um dict contendo os parâmetros do corpo de uma requisição POST. request. : Caso seja uma página de upload, contém os arquivos que foram enviados.

PATH / =>  atualiza um recurso

DELETE / => remove um recurso 
```

