import asyncio
from datetime import datetime
import json

import aiohttp


url = 'http://127.0.0.1:8000/message/'
payload = {"username": "Vadimka", "text": "aio text"}
headers = {'content-type': 'application/json'}


async def task(task_id):
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            url=url,
            data=json.dumps(payload),
            headers=headers
        )
        response_html = await response.text()
        # print(response_html)
    print(f'Задача {task_id} выполнена.')


async def async_execute():
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, 5)]
    await asyncio.wait(tasks)


if __name__ == '__main__':

    print('Асинхронное выполнение кода:')
    start_time = datetime.now()
    
    # Одна строчка кода заменяет три.
    asyncio.run(async_execute())

    end_time = datetime.now()
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')  