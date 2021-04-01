"""
The module returns a graph of the dynamics of the currency exchange rate for the period.
"""

import matplotlib.pyplot as plt
import db


def get_picture(ccy, date_start, date_end):
    courses = db.get_courses(ccy, date_start, date_end)
    x = [с[1][8:] for с in courses] #dates in string format
    y = [c[3] for c in courses] #course values
    fig = plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title(f'Курс {ccy} с {date_start} по {date_end}')
    plt.savefig(r'.\chart2.jpeg')
    return open(r'.\chart2.jpeg', "rb")
