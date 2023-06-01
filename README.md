# hice_messenger


для создания БД нужно добавить в env строку
database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
либо заливать на гит с готовой базой


Alembic умеет работать с переменными окружения и может прочесть значение DATABASE_URL из .env. Для этого нужно добавить несколько строк в файл alembic/env.py.
 внесите изменения в свой файл alembic/env.py:

 # Загрузим файл .env в переменные окружения.
# Библиотека python-dotenv умеет находить файл в «вышестоящих» каталогах,
# поэтому полный путь указывать не обязательно.
load_dotenv('.env')

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Установим для переменной sqlalchemy.url значение из нашего .env файла.
config.set_main_option('sqlalchemy.url', os.environ['DATABASE_URL'])