
import asyncio
import json
import logging
from datetime import datetime
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from random import choice

import aiohttp
import pandas as pd
from config import (COROUTINE_AMOUNT, LOG_DATETIME_FORMAT, LOG_FILE,
                    LOG_FORMAT, LOGS_DIR, NAMES, REQUESTS_AMOUNT, URLS)

requests_time = []
payload = {"username": 'dummy_name', "text": "Hello world"}
headers = {'content-type': 'application/json'}


async def task():
    """Функция создания задачи"""
    start_time = datetime.now()
    async with aiohttp.ClientSession() as session:
        payload['username'] = choice(NAMES)
        url = choice(URLS)
        await session.post(
            url=url,
            data=json.dumps(payload),
            headers=headers
        )
    end_time = datetime.now()
    requests_time.append(end_time - start_time)


async def async_execute():
    """Асинхронный генератор задач"""
    tasks = [asyncio.ensure_future(task()) for _ in range(REQUESTS_AMOUNT)]
    await asyncio.wait(tasks)


def calculate_average_time_of_request(requests_time):
    """Вычисляет среднее время одного запроса"""
    average_time = (pd.to_timedelta(pd.Series(
        requests_time)).mean().total_seconds())
    return average_time


def calculate_rps(average_time_of_request):
    """Вычисляет RPS - requests per second"""
    rps = int(REQUESTS_AMOUNT/average_time_of_request * COROUTINE_AMOUNT)
    return rps


def configure_logging():
    """Описание конфигурации для логирования"""
    LOGS_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10**6, backupCount=5, encoding='utf-8'
    )

    logging.basicConfig(
        datefmt=LOG_DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, StreamHandler())
    )
