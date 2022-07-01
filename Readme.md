# Веб-страница для управления перезагрузкой тестовых ИБ

### Предназначена для включения/отключения скриптов, загружающих бэкап рабочих ИБ в тестовые ИБ.

![](ibcntr/static/images/shot.png)

Каждую ночь у нас запускаются [задания Jenkins](https://github.com/vsuh/LOADIB) для загрузки свежих данных в тестовые информационные базы из SQL-бэкапа рабочих ИБ.
Перед выполнением загрузки, каждое задание выполняет запрос `curl http://SERVER:PORT/q/INFOBASE_NAME` по текущей тестовой ИБ и, если запрос возвращает значение "on", то загрузка выполняется.


Проект работает в виртуальном окружении `venv`. Чтобы настроить окружение и установить в нее все необходимые библиотеки, нужно выполнить команды:  

```sh
cd <repo>
$ python3 -m venv venv
$ source venv/bin/activate
(ibcntr) $ pip install -r requirements.txt
```

Данные аутентификации хранятся в базе SQLite `ibcntr/db.sqlite`
Для создания БД нужно выполнить команды:

```sh
$ python
>>> from ibcntr import db, create_app, models  
>>> db.create_all(app=create_app())
```

на продуктиве, живучестью сервиса управляет сервис linux `supervisor`  

```sh
$ sudo apt-get -y install supervisor nginx
```

[Конфигурационный файл](deployment/supervisor/cntrib.conf) `/etc/supervisor/conf.d/ibcntr.conf`:

```ini
[program:runner]
command=/opt/cntib/venv/bin/gunicorn -b localhost:8000 -w 4 runner:ibcntr
directory=/home/vsuh/Dropbox/projects/flask-ibcntr
user=vsuh
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

Настройки рабочего экземпляра проекта в файле `conf/.env`

```python
SECRET_KEY = 'a92d74111111111111111111111dbc29'
LOG_TO_STDOUT = False
REDIS_URL = 'redis://redis-hostname-or-ip/1?decode_responses=True&health_check_interval=2'
PROD_APP_NAME = 'ibcntr'
```

Данные хранятся в БД `redis`

В API добавлена команда `/initialize_db_fast`, которая заполняет подключенную базу данных набором тестовых данных.

Реализованные методы описаны на справочной странице по адресу `http://SERVER:PORT/help`


### Использованная литература:

- [Мегаучебник Flask на habr](https://habr.com/ru/post/346306/)
- [Про bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Инструкция по развертыванию](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)
- [Развертывание еще](https://flask.palletsprojects.com/en/1.1.x/deploying/)
- [Redis в примерах](https://python-scripts.com/redis#beginning-redis-examples)
- [Пример аутентификации в Flask](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-ru)
