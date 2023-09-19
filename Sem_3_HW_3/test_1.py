"""

"""
from pip._internal.utils import datetime

from checkout import checkout_positive, getout
import random
import string

import yaml
import pytest as pytest
import pytest
with open('config.yaml', encoding='utf-8') as fy:
    # читаем документ YAML
    data = yaml.safe_load(fy)

# folder_in = "/home/user/tst"
# folder_out = "/home/user/out"
# folder_ext = "/home/user/folder1"


@pytest.fixture()
def make_folders():
    return checkout_positive(f'mkdir {data["folder_in"]} {data["folder_out"]} {data["folder_ext"]} {data["folder_ext2"]}', "")

@pytest.fixture()
def clear_folders():
    return checkout_positive(f'rm -rf {data["folder_in"]}/* {data["folder_out"]}/* {data["folder_ext"]}/* {data["folder_ext2"]}/*', "")
@pytest.fixture()
def make_files():
    list_off_files = [ ]
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(f'cd {data["folder_in"]}; dd if=/dev/urandom of={filename} bs={data["bs"]} count={data["bs"]} iflag=fullblock', ""):
            list_off_files.append(filename)
    return list_off_files

@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive(f'cd {data["folder_in"]}; mkdir {subfoldername}', ""):
        return None, None
    if not checkout_positive(f'cd {data["folder_in"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs={data["bs"]} count={data["bs"]} iflag=fullblock', ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename









@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

@pytest.fixture()
def make_bad_arx():
    checkout_positive(f'cd {data["folder_out"]}; 7z a {data["type"]}/arxbad -t', "Everything is Ok")
    checkout_positive(f'truncate -s 1 {data["folder_out"]}/arxbad.{data["type"]}', "Everything is Ok")
    yield "arxbad"
    checkout_positive("rm -f {}/arxbad.{}".format(data["folder_out"], data["type"]), "")

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout_positive("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")








#
# @pytest.fixture()
# def test_step1():
#      #test1 проверяет, что команда архивации содержит текст «Everything is OK» и завершается с кодом 0.
#     assert checkout_positive(f"cd {foder_in}; 7z a {foder_out}/arx2", "Everything is Ok"), "test1 FAIL"
#
# @pytest.fixture()
# def test_step2():
#     # test2 проверяет, что команда разархивации содержит текст «Everything is OK» и завершается с кодом 0.
#     assert checkout_positive(f"cd {foder_out}; 7z e arx2.7z -o{foder_ext} -y", "Everything is Ok"), \
#         "test2 FAIL"
#
# @pytest.fixture()
# def test_step3():
#     # test3 проверяет, что команда тестирования файлов в архиве содержит текст «Everything is OK»
#     # и завершается с кодом 0.
#     assert checkout_positive(f"cd {foder_out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
#
# @pytest.fixture()
# def test_step4():
#     # test4 удаление из архива
#     assert checkout_positive(f"cd {foder_out}; 7z d arx2.7z", "Everything is Ok"), "test3 FAIL"
#
# @pytest.fixture()
# def test_step5():
#     # test5 обновление архива
#     assert checkout_positive(f"cd /{foder_out}; 7z u arx2.7z", "Everything is Ok"), "test3 FAIL"
#
#
# @pytest.fixture()
# def test_step6():
#     # test6 при архивации дополнительно проверялось создание файла архива.
#     res1 = checkout_positive(f"cd {foder_in}; 7z a {foder_out}/arx2", "Everything is Ok")
#     res2 = checkout_positive(f"ls {foder_out}", "arx2.7z")
#     assert res1 and res2, "test6 FAIL"
#
# @pytest.fixture()
# def test_step7():
#     # test7 при распаковке проверялось создание файлов.
#     res1 = checkout_positive(f"cd {foder_out}; 7z e arx2.7z -o{foder_ext} -y", "Everything is Ok")
#     res2 = checkout_positive(f"ls {foder_ext}", "test1.txt")
#     res3 = checkout_positive(f"ls {foder_ext}", "test2.txt")
#     assert res1 and res2 and res3, "test7 FAIL"
#
# @pytest.fixture()
# def test_step8():
#     # test8 проверка на пустоту архива,  вывод списка файлов.
#     assert checkout_positive(f"cd {foder_out}; 7z l arx2.7z", "2 files")
#
# @pytest.fixture()
# def test_step9():
#     # test9 команда разархивирования с путями (x).
#     assert checkout_positive(f"cd {foder_out}; 7z x arx2.7z -o{foder_ext} -y", "Everything is Ok"), \
#         "test9 FAIL"
#
# @pytest.fixture()
# def test_step10():
#     # test10 тест команды расчета хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
#     assert checkout_positive(f"cd {foder_out}; 7z h arx2.7z", "6E3F7F25")
