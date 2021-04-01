"""
The module returns data on the exchange rate for the selected period from the official website of the Central Bank.
"""
import requests
from bs4 import BeautifulSoup
from all_currency import get_r0
from datetime import datetime


def string_to_date(s):
    return datetime.strptime(s, "%d.%m.%Y")


def date_to_string(d):
    return d.strftime("%d.%m.%Y")


def get_for_period(ccy, date_begin, date_end):
    r0 = get_r0(ccy)
    url = f"https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDb" \
          f"Query.date_req2=&UniDbQuery.VAL_NM_RQ={r0}&UniDbQuery.From={date_to_string(date_begin)}&UniDbQuery.To" \
          f"={date_to_string(date_end)}"

    html = requests.get(url).content
    htmlmonth = BeautifulSoup(html, 'html.parser')
    cbrtables = htmlmonth.find_all("table")
    courses = []
    for table in cbrtables:
        for row in table.findAll("tr")[1:]:
            cells = row.findAll(["th", "td"])
            courses.append((cells[0].text, cells[1].text, cells[2].text))
    courses.pop(0)
    return [(string_to_date(c[0]), int(c[1]), float(c[2].replace(",", "."))) for c in courses]


