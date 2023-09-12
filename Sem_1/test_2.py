"""
Задание 2
Переписать тест на Python c использованием модуля subprocess
"""
import subprocess

def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        res = result.stdout.split("\n")
        print(res)
        if "VERSION_CODENAME=jammy" in res and 'VERSION="22.04.3 LTS (Jammy Jellyfish)"' in res:
            print("SUCCESS")
        else:
            print("FAIL")


script_1()
