__all__ = ['check_queens']
COUNT_TWO = 8


# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка
# 8 ферзей на доске, определите, есть ли среди них
# пара бьющих друг друга. Программа получает на вход
# восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def check_queens() -> bool:
    queens = []
    count_two = 1
    for _ in range(COUNT_TWO):
        x, y = map(int, input(f"Введите {count_two}-ю пару ферзей через запятую (доска 8х8): ").split(','))
        count_two += 1
        if 1 <= x <= COUNT_TWO or 1 <= y <= COUNT_TWO:
            queens.append((x, y))
        else:
            print("Неверный ввод")
            check_queens()

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
    print(check_queens())
