# django_celery


cd django_celery

```
pip install requirements.txt
python manage.py migrate
celery -A django_celery worker -l INFO
```