@echo off
cls
chcp 65001
python -m venv .venv
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    echo Окружение создано в backend/.venv и зависимости установлены.
) else (
    echo Не удалось создать виртуальное окружение в backend.
)
pause

cls