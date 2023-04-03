import matplotlib.pyplot as plt
import csv
import seaborn as sns
from datetime import datetime, timedelta

import numpy as np

from settings import *
import pandas as pd
import calmap
import calplot


def is_hours(expected_time, time):
    if time//60 >= expected_time:
        return True
    else:
        return False


def total_focus():
    minutes = 0
    with open('data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            minutes += int(row[1])
    return minutes


def most_productive():
    day = {"Monday": 0,
           "Tuesday": 0,
           "Wednesday": 0,
           "Thursday": 0,
           "Friday": 0,
           "Saturday": 0,
           "Sunday": 0}

    with open('data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            weekday = date.strftime('%A')
            day[weekday] += int(row[1])
    print(max(day, key=day.get))
    return max(day, key=day.get)


def weekday_plot():
    day = {"Monday": 0,
           "Tuesday": 0,
           "Wednesday": 0,
           "Thursday": 0,
           "Friday": 0,
           "Saturday": 0,
           "Sunday": 0}

    with open('data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            weekday = date.strftime('%A')
            day[weekday] += int(row[1])

    plt.plot(day.keys(),
             day.values(),
             linestyle='dashed',
             marker='o')
    plt.xticks(rotation=25)
    plt.xlabel('weekdays')
    plt.ylabel('Total time (minutes)')
    plt.title('Focus by weekday', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()


def year_plot():
    month = {"January": 0,
             "February": 0,
             "March": 0,
             "April": 0,
             "May": 0,
             "June": 0,
             "July": 0,
             "August": 0,
             "September": 0,
             "October": 0,
             "November": 0,
             "December": 0}

    with open('data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            weekday = date.strftime('%B')
            month[weekday] += int(row[1])

    plt.plot(month.keys(),
             month.values(),
             linestyle='dashed',
             marker='o')
    plt.xticks(rotation=25)
    plt.xlabel('months')
    plt.ylabel('Total time (minutes)')
    plt.title('Focus by months', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()
