"""
Домашнее задание
Задание 1. Дополнить проект тестами, проверяющими команды вывода спискафайлов (l) и разархивирования с путями (x).
Установить пакет для расчёта crc32 "sudo apt install libarchive-zip-perl"
Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
"""

from checkout import checkout_positive


folder_in = "/home/user/tst"
folder_out = "/home/user/out"
folder_1 = "/home/user/folder1"


def test_step1():
    """test1 for checking archivation command to include text  «Everything is OK» and finish with code 0."""
    assert checkout_positive(f"cd {folder_in}; 7z a {folder_out}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    """test2 for checking dearchivation command to include text  «Everything is OK» and finish with code 0."""
    assert checkout_positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok"), \
        "test2 FAIL"


def test_step3():
    """test3 for checking testing command in archive to include text  «Everything is OK» and finish with code 0."""
    assert checkout_positive(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    """test4 for checking deletion from archive command to include text  «Everything is OK» and finish with code 0."""
    assert checkout_positive(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step5():
    """test5 for checking archive update command to include text  «Everything is OK» and finish with code 0."""
    assert checkout_positive(f"cd /{folder_out}; 7z u arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step6():
    """test6 for checking archive file creating while archivating"""
    res1 = checkout_positive(f"cd {folder_in}; 7z a {folder_out}/arx2", "Everything is Ok")
    res2 = checkout_positive(f"ls {folder_out}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    """test7 for checking archive file creating while dearchivating"""
    res1 = checkout_positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok")
    res2 = checkout_positive(f"ls {folder_1}", "test1.txt")
    res3 = checkout_positive(f"ls {folder_1}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"


def test_step8():
    """test8 for checking archive empty, file list output"""
    assert checkout_positive(f"cd {folder_out}; 7z l arx2.7z", "2 files")


def test_step9():
    """test9 for checking dearchivation with paths"""
    assert checkout_positive(f"cd {folder_out}; 7z x arx2.7z -o{folder_1} -y", "Everything is Ok"), \
        "test9 FAIL"


def test_step10():
    """test10 for checking hash matches crc32 command hash"""
    assert checkout_positive(f"cd {folder_out}; 7z h arx2.7z", "F2107E5F")
