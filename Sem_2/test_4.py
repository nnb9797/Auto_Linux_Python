"""
Задание 2
Добавить в проект тесты, проверяющие работу команд d (удаление из архива) и u (обновление архива). Вынести в отдельные
переменные пути к папкам с файлами, с архивом и с распакованными файлами. Выполнить тесты с ключом -v.


Задание 4
Доработать позитивные тесты таким образом, чтобы при
архивации дополнительно проверялось создание файла
архива, а при распаковке проверялось создание файлов.
test6 и test7

Домашнее задание
Задание 1. Дополнить проект тестами,
проверяющими команды вывода списка
файлов (l) и разархивирования с путями (x).
test8 и test9
"""

from checkout import checkout_positive


folder_in = "/home/user/tst"
folder_out = "/home/user/out"
folder_1 = "/home/user/folder1"


def test_step1():
    # test1 проверяет, что команда архивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_positive(f"cd {folder_in}; 7z a {folder_out}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2 проверяет, что команда разархивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok"), \
        "test2 FAIL"


def test_step3():
    # test3 проверяет, что команда тестирования файлов в архиве содержит текст «Everything is OK»
    # и завершается с кодом 0.
    assert checkout_positive(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4 удаление из архива
    assert checkout_positive(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step5():
    # test5 обновление архива
    assert checkout_positive(f"cd /{folder_out}; 7z u arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step6():
    # test6 при архивации дополнительно проверялось создание файла архива.
    res1 = checkout_positive(f"cd {folder_in}; 7z a {folder_out}/arx2", "Everything is Ok")
    res2 = checkout_positive(f"ls {folder_out}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    # test7 при распаковке проверялось создание файлов.
    res1 = checkout_positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok")
    res2 = checkout_positive(f"ls {folder_1}", "test1.txt")
    res3 = checkout_positive(f"ls {folder_1}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"

