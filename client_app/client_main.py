import asyncio
import logging
from datetime import datetime

from config import (AV_TIME_PER_REQ_MESSAGE, COROUTINE_AMOUNT, END_MESSAGE,
                    REQUESTS_AMOUNT, RPS_MESSAGE, START_MESSAGE,
                    TOTAL_REQ_MESSAGE, TOTAL_TIME_MESSAGE)
from services import (async_execute, calculate_average_time_of_request,
                      calculate_rps, configure_logging, requests_time)


def main():
    """Основная функция запуска генератора запросов"""
    logging.info(START_MESSAGE)
    start_time = datetime.now()

    for _ in range(COROUTINE_AMOUNT):
        asyncio.run(async_execute())

    end_time = datetime.now()
    total_time = end_time - start_time
    total_requests_amount = REQUESTS_AMOUNT * COROUTINE_AMOUNT
    average_time_of_request = calculate_average_time_of_request(requests_time)
    rps = calculate_rps(average_time_of_request)
    logging.info(f'{TOTAL_REQ_MESSAGE} {total_requests_amount} шт.')
    logging.info(f'{AV_TIME_PER_REQ_MESSAGE} {average_time_of_request} сек.')
    logging.info(f'{RPS_MESSAGE} {rps} RPS')
    logging.info(f'{TOTAL_TIME_MESSAGE} {total_time} сек.')
    logging.info(END_MESSAGE)


if __name__ == '__main__':
    configure_logging()
    main()
