# Простой проект проверящий статус визы в Италию

## Технологии:
telebot = "0.0.5", bs4 = "0.0.1", colorlog = "6.7.0", lxml = "4.9.3"

## Запуск
Заполните .env согласно example.env
## В докере
``` docker build -t "<имя>" .```
``` docker run --name <имя контейнера> --restart=always --env-file .env -d --net=host poetry run python -m src.main.py```
## Без докера
``` python -m src.main.py ```

## Автор
Иван Алексеев