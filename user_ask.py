import datetime as dt
import DateInterval as DI


def ask_int(none) -> int:
    s = input()
    while (not s.isdecimal()) or s <= 0:
        print("Введите количество в виде десятичного натурального числа: ", end="")
        s = input()
        return int(s)


def ask_date(none) -> dt.date:
    s = input()
    day, mounth, year = list(map(int, s.split('.')))
    while True:
        try:
            res = dt.date(day=day, mounth=mounth, year=year)
            return res
        except ValueError:
            print("Неправильный формат даты. Попробуйте ещё раз.")


def ask_info(none) -> list[DI.DateInterval]:
    print("Введите количество диапазонов дат: ", end="")
    n = ask_int()
    periods = list()
    for i in range(n):
        first_date = ask_date()
        second_date = ask_date()
        tmp = DI.DateInterval(first_date, second_date)
        periods += tmp
    return periods
