from random import randint as rnd


COUNT_TWO = 8
START = 1
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше.
# Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

def random_queens()-> list:
    queens = []

    for _ in range(8):
        x= rnd(START, COUNT_TWO)
        y = rnd(START, COUNT_TWO)
        queens.append((x, y))

    print(queens)
    return queens

def check_queens(queens: list) -> bool:

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]

            if is_attacked(x1, y1, x2, y2):
                return False

    return True




# Могут ли ферзи побить друг друга
def is_attacked(x1: int, y1: int, x2: int, y2: int) -> bool:
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


if __name__ == '__main__':
    print(check_queens(random_queens()))

