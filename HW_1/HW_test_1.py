"""
Задание 1. Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess
from typing import List

def text_checking(command: List[str], text: str) -> bool:
    result_command: str = (subprocess.run(command, stdout=subprocess.PIPE,
                                          text=True, shell=True, encoding='utf-8')).stdout

    return text in result_command


if __name__ == '__main__':
    # command_list: List[str] = ["cat /etc/os-release"]
    command_list: List[str] = ["cat test_2.py"]
    # text_search: str = 'https://help.ubuntu.com/'
    text_search: str = '22.04.3'
    text_was_found: bool = text_checking(command_list, text_search)
    print(f'\nВывод: \n{text_search}\n{text_was_found}')