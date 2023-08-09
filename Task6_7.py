# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date() -> bool:
    str_date = input("Введите дату: ")
    day, mon, yaer = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= yaer <= 9999):
        return False

    if mon in (4, 6, 9, 11) and day > 30:
        return False

    if mon == 2 and day > 29:
        return False

    if mon == 2 and if_leap(yaer) and day > 29:
        return False

    if mon == 2 and not if_leap(yaer) and day > 28:
        return False

    return True


if __name__ == '__main__':
    # print(check_date('31.10.2024'))
    name, *argv = argv
    print(check_date())
