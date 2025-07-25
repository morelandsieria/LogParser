Установка зависимостей: pip install -r requirements.txt

python main.py --help

--file FILE [FILE ...] Один или несколько лог-файлов
--report REPORT Тип отчёта average
--date DATE Фильтрация по дате в формате YYYY-MM-DD

Пример запуска скрипта: python3 main.py --file tests/test_data/example1.log --report average 

Запуск тестов: pytest tests/ -v 

Запуск pytest-cov: pytest --cov=src tests/