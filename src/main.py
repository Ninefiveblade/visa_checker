import time
from dataclasses import dataclass

import requests
import telebot
from bs4 import BeautifulSoup

from .config import settings
from .constants import CONNECT_TRYIES, REQUEST_RIMEOUT, TIME_TO_UPDATE
from .logger import logger


@dataclass(repr=False, init=False)
class VmsParse:
    """Returns string statuses from VMS Italy"""

    __timeot: int = REQUEST_RIMEOUT
    __soup: BeautifulSoup = BeautifulSoup(
        requests.get(settings.url, timeout=__timeot).text, "lxml"
    )

    @classmethod
    def __get_html_etree_text(cls, css: str) -> str:
        """Get head message by xpath"""
        try:
            result = cls.__soup.select(css)[0].text.strip(" \n")
            logger.info(f"Succses get messsage {result}")
        except (ValueError, KeyError, IndexError):
            logger.exception(msg="get_head_message has except", stack_info=True)
            result = "Статус изменился или некорректный"
        return result

    @classmethod
    def get_status_message(self) -> str:
        return self.__get_html_etree_text(
            'td[style="font-size: 24pt; color: #FF6666;"]'
        )


if __name__ == "__main__":

    for connect_try in range(CONNECT_TRYIES):
        try:
            bot = telebot.TeleBot(settings.telegram_token)
            bot.send_message(settings.chat_id, "Ready to send statuses")
            break
        except Exception:
            logger.exception(
                f"Can't connect to telegram, try: {connect_try}", stack_info=True
            )

    while True:
        bot.send_message(
            settings.chat_id, f"Статус заявки: \n {VmsParse.get_status_message()}"
        )
        bot.send_message(
            settings.chat_id,
            f"Слудующее обновление через " f"{TIME_TO_UPDATE // 60 // 60} часов",
        )
        time.sleep(TIME_TO_UPDATE)
