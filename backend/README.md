# Dockerで起動する
- docker-compose up -d

# Docker使用せずに起動する
- pip env install
- pip env shell
- python manage.py migrate
- python manage.py runserver
- python manage.py createsuperuser

<!-- # コンテナで直接コマンド実行する場合
- docker-compose run web ./manage.py makemigrations
- docker-compose run web ./manage.py migrate
- docker-compose run web ./manage.py createsuperuser
- docker-compose run web ./manage.py collectstatic --no-input -->

# 開発環境でDocker起動（MySQL）
- docker-compose down -v
- docker-compose up -d
<!-- 自動実行
- docker-compose exec web python manage.py migrate --noinput --settings=restapi.settings.local -->
- docker-compose exec web python manage.py createsuperuser
- docker-compose exec web python manage.py loaddata fixtures/all.json
- アクセスURL: localhost:8000

# 開発環境（SQLite3）
- pip env install
- pip env shell
- python manage.py runserver --settings=restapi.settings.test

# 本番環境でDocker起動(MySQL)
- docker-compose -f docker-compose.prod.yml down -v
- docker-compose -f docker-compose.prod.yml up -d --build
- docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput --settings=restapi.settings.production
- docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput --clear
- アクセスURL: localhost:1337

## 初期データ投入
- python manage.py dumpdata > fixtures/all.json
- python manage.py loaddata fixtures/all.json

# アクセス
- URL: http://127.0.0.1:8000/api/

# 注意
本番環境でmanage.pyコマンドを実行する場合は、あらかじめ環境変数DJANGO_SETTINGS_MODULEにconfig.settings.productionを設定するか、manage.pyの起動オプションに--settings config.settings.productionを指定する必要がある。