"""
Задание 1
Написать автотест на bash, который читает содержимое файла /etc/os-release (в нем хранится информация о версии системы)
и выведет на экран “SUCCESS” если в нем содержатся версия 22.04.1, кодовое имя jammy и команда чтения файла выполнена
без ошибок. В противном случае должно выводится “FAIL”.
"""

# #!/bin/bash
# result=$(cat /etc/os-release)
# if [[ $result == *"22.04.1"* && *"jammy"* && $? == 0 ]];
# then echo "SUCCESS"
# else echo "FAIL"
# fi

import subprocess

def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(type(result))
    print(result.stdout)
    print(result.returncode)
    print(result.stderr)
    if ("jammy" in result.stdout and "22.04.3" in result.stdout and result.returncode == 0):
        print("SUCCESS")
    else:
        print("FAIL")


script_1()
