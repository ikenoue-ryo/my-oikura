# 起動1
- docker-compose up -d

# 起動2
- pip env install
- pip env shell
- python manage.py migrate
- python manage.py runserver
- python manage.py createsuperuser

## 初期データ投入
- python manage.py dumpdata > fixtures/all.json
- python manage.py loaddata fixtures/all.json

# アクセス
- URL: http://127.0.0.1:8000/api/