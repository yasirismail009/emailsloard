import re
import hashlib
from calendar import monthrange
from datetime import datetime, timedelta


def md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def last_year_regex():
    today = datetime.today()
    return re.compile((today.replace(day=1, month=1) - timedelta(days=1)).strftime('%Y-'))


def last_month_regex():
    today = datetime.today()
    return re.compile((today.replace(day=1) - timedelta(days=1)).strftime('%Y-%m-'))

def last_30_regex():
    today = datetime.today()
    return re.compile((today.replace(day=1) - timedelta(days=1)).strftime('%Y-%m-%d'))

def last_day_regex():
    today = datetime.today()
    return re.compile((today - timedelta(days=1)).strftime('%Y-%m-%d'))


def number_of_days_in_last_month():
    last_month = datetime.today().replace(day=1) - timedelta(days=1)
    return monthrange(last_month.year, last_month.month)[1]


def chunkify(lst, n):
    n = max(1, n)
    return (lst[i:i + n] for i in range(0, len(lst) or 1, n))


def validate_page_number(page):
    try:
        return abs(int(page))

    except ValueError:
        return 1
