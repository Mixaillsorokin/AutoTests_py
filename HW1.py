# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.
#
# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string


def check_command_output(command, text, mode='Text'):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if mode == 'Text':
        if text in out and result.returncode == 0:
            return True
    elif mode == 'Word':
        words = out.split()
        clean_words = ''.join(char for char in words if char not in string.punctuation)
        if text in clean_words and result.returncode == 0:
            return True
        return False


if __name__ == '__main__':
    if check_command_output( 'Команда', 'Текст', mode='Text или Word'):
        print("SUCCESS")
    else:
        print("FAIL")
