"""
Module for determining the current exchange rate of a given currency. 
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/currency_base/daily/"


def course_val(n):
    raw_html = requests.get(url).content
    html = BeautifulSoup(raw_html, 'html.parser')
    cbrtables = html.find_all("table")
    courses = []
    for table in cbrtables:
        for row in table.findAll("tr")[1:]:
            cells = row.findAll(["th", "td"])
            courses.append((cells[0].text, cells[1].text, cells[2].text, cells[3].text, cells[4].text))
    dict_val = {i[0]: i[-1] for i in courses}
    dict_val_2 = {i[1]: i[-1] for i in courses}
    dict_val.update(dict_val_2)
    course = dict_val[n]
    amount = ''
    currency = ''
    for i in courses:
        if n.isalpha():
            if i[1] == n:
                amount, currency = i[2], i[3]
        else:
            if i[0] == n:
                amount, currency = i[2], i[3]

    result = 'Сегодня за {} {} дают {} руб.'.format(amount, currency, course)
    return result
