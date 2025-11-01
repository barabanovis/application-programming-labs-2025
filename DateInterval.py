import datetime as dt


class DateInterval:
    def __init__(self, first_date: dt.date, second_date: dt.date):
        self.first_date = first_date
        self.second_date = second_date
