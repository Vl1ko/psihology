@echo off
REM Активация виртуального окружения
IF EXIST venv (
    call venv\Scripts\activate
) ELSE (
    echo Виртуальное окружение не найдено. Создаем новое...
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
)

REM Запуск приложения
python app.py 