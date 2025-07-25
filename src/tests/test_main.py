import pytest
from src.main import main
from unittest.mock import patch


def test_main_invalid_report():
    test_args = [
        "main.py",
        "--file", "tests/test_data/example2.log",
        "--report", "invalid"
    ]
    
    with patch('sys.argv', test_args):
        with pytest.raises(ValueError, match="Неизвестный тип отчета"):
            main()


def test_main_invalid_file():
    test_args = [
        "main.py",
        "--file", "tests/test_data/example",
        "--report", "average"
    ]
    
    with patch('sys.argv', test_args):
        with pytest.raises(ValueError, match=f"Файл {test_args[2]} не существует"):
            main()