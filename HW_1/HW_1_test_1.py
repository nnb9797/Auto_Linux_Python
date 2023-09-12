"""
Задание 1. Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess
from typing import List


def check_text_function(command: List[str], text: str) -> bool:
    search_command: str = (subprocess.run(command, stdout=subprocess.PIPE,
                                          text=True, shell=True, encoding='utf-8')).stdout

    return text in search_command


if __name__ == '__main__':
    test_command: List[str] = ["cat HW_test1.py"]
    text_search: str = "Linux"
    search_result: bool = check_text_function(test_command, text_search)
    print(f'Text for search: \n{text_search}\nSearch result:\n{search_result}')