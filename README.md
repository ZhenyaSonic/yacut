## Описание
Программа позволяет создавать короткие ссылки для переадресации. Пользователь может предложить свой вариант короткой ссылки или сгенерировать случайный.

## Технологии
alembic==1.12.0
attrs==23.2.0
blinker==1.8.2
click==8.1.7
flake8==5.0.4
Flask==3.0.2
Flask-Migrate==4.0.5
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
greenlet==3.0.3
importlib_metadata==7.1.0
iniconfig==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.3
MarkupSafe==2.1.5
mccabe==0.7.0
packaging==24.0
pluggy==1.5.0
py==1.11.0
pycodestyle==2.9.1
pyflakes==2.5.0
pytest==7.1.3
pytest-env==0.6.2
python-dateutil==2.8.2
python-dotenv==1.0.0
six==1.16.0
SQLAlchemy==2.0.21
tomli==2.0.1
typing_extensions==4.11.0
Werkzeug==3.0.0
WTForms==3.0.1
zipp==3.18.1

## Как использовать

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:
```
flask db upgrade
```

Запустить сервер:
```
flask run
```

## Автор

Братанов Евгений https://github.com/ZhenyaSonic