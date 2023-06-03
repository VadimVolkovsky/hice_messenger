import asyncio
from datetime import datetime
import json

import aiohttp

from random import choice

COROUTINE_AMOUNT = 2
REQUESTS_AMOUNT = 5
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

url = 'http://127.0.0.1:80/message/'
payload = {"username": 'dummy_name', "text": "Hello world"}
headers = {'content-type': 'application/json'}


async def task(task_id):
    async with aiohttp.ClientSession() as session:
        name = payload['username'] = choice(NAMES)
        print(f'выбрали имя: {name}')
        response = await session.post(
            url=url,
            data=json.dumps(payload),
            headers=headers
        )
    print(f'Задача {task_id} выполнена.')
    print(f'Код ответа: {response.status}')


async def async_execute():
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, REQUESTS_AMOUNT+1)]
    await asyncio.wait(tasks)


if __name__ == '__main__':

    print('Асинхронное выполнение кода:')
    start_time = datetime.now()
    
    for _ in range(COROUTINE_AMOUNT):
        asyncio.run(async_execute())

    end_time = datetime.now()
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')