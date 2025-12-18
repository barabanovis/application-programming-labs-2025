import datetime as dt
import DateInterval as DI


def ask_int() -> int:
    '''
    Спрашивает целое число число у пользователя
    '''
    flag = False
    while (not flag):
        try:
            s = int(input())
            flag = True
        except:
            print('Введено не натуральное число. Попробуйте ещё раз: ')
    return s


def ask_natural() -> int:
    '''
    Спрашивает натуральное число число у пользователя
    '''
    x = ask_int()
    while (x <= 0):
        print('Введено не натуральное число! Попробуйте ещё раз: ')
        x = ask_int()
    return x


def ask_date() -> dt.date:
    '''
    Спрашивает дату у пользователя
    '''
    s = input()
    while (True):
        try:
            day, month, year = list(map(int, s.split('.')))
            break
        except:
            print("Неправильный формат даты. Попробуйте ещё раз.") 
            s = input()
    return dt.date(day=day, month=month, year=year)


def ask_info() -> list[DI.DateInterval]:
    '''
    Спрашивает полную информацию по загрузке у пользователя
    '''
    print("Введите количество диапазонов дат (натуральное число): " , end="")
    n = ask_natural()
    periods = list()
    for i in range(n):
        first_date = ask_date()
        second_date = ask_date()
        tmp = DI.DateInterval(first_date, second_date)
        periods += [tmp]
    return periods
