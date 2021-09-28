# Dockerで起動する
- docker-compose up -d

# Docker使用せずに起動する
- pip env install
- pip env shell
- python manage.py migrate
- python manage.py runserver
- python manage.py createsuperuser

# コンテナで直接コマンド実行する場合
- docker-compose run web ./manage.py makemigrations
- docker-compose run web ./manage.py migrate
- docker-compose run web ./manage.py createsuperuser
- docker-compose run web ./manage.py collectstatic --no-input

## 初期データ投入
- python manage.py dumpdata > fixtures/all.json
- python manage.py loaddata fixtures/all.json

# アクセス
- URL: http://127.0.0.1:8000/api/

# 注意
本番環境でmanage.pyコマンドを実行する場合は、あらかじめ環境変数DJANGO_SETTINGS_MODULEにconfig.settings.productionを設定するか、manage.pyの起動オプションに--settings config.settings.productionを指定する必要がある。