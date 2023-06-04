# hice_messenger


### Описание:
Проект hice_messanger 


### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git@github.com:VadimVolkovsky/hice_messenger.git
```

**Установите и активируйте виртуальное окружение:**
для MacOS:
```
py -3.9 -m venv venv
```

для Windows:
```
py -3.9 -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
**Из корневой директории выполните запуск контейнеров:**
```
docker-compose up --build
```


### Отправка запросов:
Перейдите в папку с клиентом:
```
cd client_app
```

Выполните команду:
```
python client_main.py
```

**Настройка конфигурации запросов:**
Основные настройки клиента прописаны в файле client_app/config.py

### Документация приложения:
- Swagger
```
http://127.0.0.1:80/docs
```

- Redoc
```
http://127.0.0.1:80/redoc
```



### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy
- Alembic


**Автор проекта:**

Vadim Volkovsky
