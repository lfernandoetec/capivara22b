# oladjango23b

## Comandos (03/03/2023)
- criar um projeto
    - python -m django startproject itapira
- entrar na pasta do manage.py
    - cd itapira
- criar uma app
    - python manage.py startapp enquete
- iniciar o servidor
    - python manage.py runserver
- mostra as bibliotecas instaladas pelo gerenciador de pacotes pip
    - pip freeze
- cria a lista de dependencias
    - pip freeze > requirements.txt
- instala as dependencias
    - pip install -r requirements.txt
- Executar migrações iniciais
    - cd itapira
    - python manage.py migrate
- Criar super usuário
    - cd itapira
    - python manage.py createsuperuser
    - usuario admin
    - senha 123mudar
    - email luisfernando.silva@etec.sp.gov.br