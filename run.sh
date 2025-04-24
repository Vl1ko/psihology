#!/bin/bash

# Активация виртуального окружения
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Виртуальное окружение не найдено. Создаем новое..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# Запуск приложения
python3 app.py 