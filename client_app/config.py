from pathlib import Path

COROUTINE_AMOUNT = 50
REQUESTS_AMOUNT = 100

NAMES = [
    'Vadim Volkovsky',
    'Minubaev Malik',
    'Erik Matiz',
    'Mark Lutz',
    'Andrey Pronin',
    'Kate',
    'Khristina',
    'Napoleon',
    'Egor',
    'Dmitry',
]

URLS = [
    'http://backend_1:80/message/',
    'http://backend_2:81/message/'
]

BASE_DIR = Path(__file__).parent
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / 'client_app.log'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'

START_MESSAGE = 'Запуск асинхронного генератора запросов'
TOTAL_REQ_MESSAGE = 'Сумарное количество запросов:'
AV_TIME_PER_REQ_MESSAGE = 'Среднее время выполнения запроса:'
RPS_MESSAGE = 'Пропускная способность серверов:'
TOTAL_TIME_MESSAGE = 'Итоговое время выполнения всех запросов:'
END_MESSAGE = 'Завершение работы генератора запросов'
