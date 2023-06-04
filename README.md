# hice_messenger


### Описание:
Мессенджер для "Хайс Банк"


### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git@github.com:VadimVolkovsky/hice_messenger.git
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

**Конфигурация клиента:**
Основные настройки клиента прописаны в файле client_app/config.py

Количество клиентов (корутин):
```
COROUTINE_AMOUNT = 50
```

Количество запросов на каждого клиента
```
REQUESTS_AMOUNT = 100
```


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
