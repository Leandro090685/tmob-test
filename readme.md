### RUN

- Setear .env con variables de entorno (cambiar nombre .env.example a .env)
- pip install -r requirements.txt
- sudo docker compose up
- python3 manage.py migrate
- python3 manage.py loaddata seed/first_user.json (crea el primer superusuario user=admin / password=admin)
- python3 manage.py runserver

## RUN TESTS

- python3 manage.py test