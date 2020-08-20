# API Navedex

## API em funcionamento
A api está em funcionamento no seguinte endereço:

http://35.169.59.206:8000

A documentação feita em swagger está em:

http://35.169.59.206:8000/swagger/

## Git
clone o repositório em https://github.com/cyberby/navedex: 

`git clone git@github.com:cyberby/navedex.git`
## Instalação

### 1. Venv
Para instalar a venv do python rode o comando
```bash
python3 -m venv /path_do_projeto/venv
```
Se windows, na pasta Scripts rode o comando
```bash
cd /path_do_projeto/venv/Scripts
activate
```
Se linux, na pasta bin rode o comando
```bash
cd /path_do_projeto/venv/bin
source activate
```

### 2. Instalar dependências
```bash
cd /path_do_projeto
pip install -r requirements.txt
```

### 3. Migrations
Para criar as migrations e instalar o banco entre na api dentro sistema
```bash
cd /path_do_projeto/api
```
Depois rode os seguintes comandos para migração com
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Fixtures (popular o banco)
Para popular o banco com as fixtures, entre na pasta api se não estiver nela
```bash
cd /path_do_projeto/api
```
Depois rode os seguintes comandos para popular o banco:
```bash
python manage.py loaddata User
python manage.py loaddata Project
python manage.py loaddata Naver
```

### 5. Rodar o servidor
Para iniciar o servidor
```bash
cd /path_do_projeto/api
python manage.py runserver
```

## Api Swagger
A api swagger encontra-se em http://localhost:8000/swagger/

Você pode criar um usuário em users/post enviando o username e a senha

Para login, após criar o usuário, http://localhost:8000/swagger/ accounts/post e envie o username e senha no corpo, conforme api
O sistema fornecerá um token

Copie o token e na parte superior da página, clique em Authorize e em value coloque "JWT token_copiado" e clique em authorize para poder usar os outros endpoints da api

Um exemplo do que deve ficar em value no JWT é "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InJvb3QiLCJleHAiOjE1OTc4ODQwNDIsImVtYWlsIjoicmFmYWVsZGVjcnV6ZWlyb0BnbWFpbC5jb20ifQ.y4TGm-77e9av9PDvYEXbDkUxFWxxReeeCjmhSiEFLQY"

Caso rode as fixtures com loaddata já criei um usuário padrão root com senha 123456

Assim, o corpo de accounts/login deve ficar como
```bash
{
  "username": "root",
  "password": "123456"
}
```


## Tests
Os testes estão em `/path_do_projeto/api/tests`

Para rodar os testes, execute o seguinte comando na pasta api:
```bash
python manage.py test
```
