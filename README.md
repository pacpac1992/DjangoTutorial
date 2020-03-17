python manage.py django-admin startproject mysite
python manage.py runserver
python manage.py startapp polls


-- migraciones
python manage.py makemigrations
python manage.py migrate

-- Errores
python manage.py check

-- shell
python manage.py shell
from GestionPedidos.models import Articulos
art = Articulos(nombre='',seccion='',precio='')
art.save()
art = Articulos.objects.create(nombre='',seccion='',precio='')


-- admin
python manage.py createsuperuser
root
root@gmail.com
123456
n
