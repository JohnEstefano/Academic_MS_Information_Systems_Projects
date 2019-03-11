import csv
import time
import operator
from collections import defaultdict
from datetime import datetime, timedelta


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    city = city.lower()
    if city == 'chicago':
        return chicago
    elif city == 'new york':
        return new_york_city
    elif city == 'washington':
        return washington
    else:
        print('Please input a vaild city...')
        print('Let\'s try that again.')
        statistics()


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    time_period = time_period.lower()

    if time_period == 'month':
        return time_period
    elif time_period == 'day':
        return time_period
    elif time_period == 'none':
        return time_period
    else:
        print('Please input a vaild time period...')
        print('Let\'s try that again.')
        statistics()


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    months = ['January','February','March','April','May','June','July',
              'August','September','October','November','December']
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    month = month.lower()
    month = month.title()

    if month in months:
        return month
    else:
        print ('Please enter a valid month...')
        print('Let\'s try that again.')
        statistics()


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = int(input('\nWhich day? Please type your response as an integer.\n'))
    day31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    day30 = ['April', 'June', 'September', 'November']
    day28 = ['February']

    message_day = 'Please enter a vaild day...'

    #Check if input is vaild
    if month in day31:
        if day > 31 or day < 1:
            print(message_day)
            get_day(month)
        elif day > 0 and day < 10:
            day = '0'+str(day)
            return day
        else:
            return str(day)

    elif month in day30:
        if day > 30 or day < 1:
            print(message_day)
            get_day(month)
        elif day > 0 and day < 10:
            day = '0'+str(day)
            return day
        else:
            return str(day)

    elif month in day28:
        if day > 28 or day < 1:
            print(message_day)
            get_day(month)
        elif day > 0 and day < 10:
            day = '0'+str(day)
            return day
        else:
            return str(day)

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    count_jan = count_feb = count_mar = count_apr = count_may = count_jun = 0

    with open(city_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Start Time'].startswith('01', 5, 7):
                count_jan += 1
            elif row['Start Time'].startswith('02', 5, 7):
                count_feb += 1
            elif row['Start Time'].startswith('03', 5, 7):
                count_mar += 1
            elif row['Start Time'].startswith('04', 5, 7):
                count_apr += 1
            elif row['Start Time'].startswith('05', 5, 7):
                count_may += 1
            elif row['Start Time'].startswith('06', 5, 7):
                count_jun += 1

    if count_jan is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('January is the most popular month for start time')
    elif count_feb is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('February is the most popular month for start time')
    elif count_mar is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('March is the most popular month for start time')
    elif count_apr is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('April is the most popular month for start time')
    elif count_may is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('May is the most popular month for start time')
    elif count_jun is max(count_jan, count_feb, count_mar, count_apr, count_may, count_jun):
        print('June is the most popular month for start time')



def popular_day(city_file, time_period, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    count_sun = count_mon = count_tue = count_wed = count_thu = count_fri = count_sat = 0

    with open(city_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if time_period== 'none' or month == 'January':
                if row['Start Time'].startswith('01', 5, 7):
                    jan_sun = ['01', '08', '15', '22', '29']
                    jan_mon = ['02', '09', '16', '23', '30']
                    jan_tue = ['03', '10', '17', '24', '31']
                    jan_wed = ['04', '11', '18', '25']
                    jan_thu = ['05', '12', '19', '26']
                    jan_fri = ['06', '13', '20', '27']
                    jan_sat = ['07', '14', '21', '28']
                    if row['Start Time'].startswith(tuple(jan_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(jan_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(jan_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(jan_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(jan_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(jan_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(jan_sat), 8, 10):
                        count_sat += 1
            if time_period== 'none' or month == 'February':
                if row['Start Time'].startswith('02', 5, 7):
                    feb_sun = ['05', '12', '19', '26']
                    feb_mon = ['06', '13', '20', '27']
                    feb_tue = ['07', '14', '21', '28']
                    feb_wed = ['01', '08', '15', '22']
                    feb_thu = ['02', '09', '16', '23']
                    feb_fri = ['03', '10', '17', '24']
                    feb_sat = ['04', '11', '18', '25']
                    if row['Start Time'].startswith(tuple(feb_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(feb_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(feb_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(feb_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(feb_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(feb_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(feb_sat), 8, 10):
                        count_sat += 1
            if time_period== 'none' or month == 'March':
                if row['Start Time'].startswith('03', 5, 7):
                    mar_sun = ['05', '12', '19', '26']
                    mar_mon = ['06', '13', '20', '27']
                    mar_tue = ['07', '14', '21', '28']
                    mar_wed = ['01', '08', '15', '22', '29']
                    mar_thu = ['02', '09', '16', '23', '30']
                    mar_fri = ['03', '10', '17', '24', '31']
                    mar_sat = ['04', '11', '18', '25']
                    if row['Start Time'].startswith(tuple(mar_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(mar_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(mar_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(mar_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(mar_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(mar_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(mar_sat), 8, 10):
                        count_sat += 1
            if time_period== 'none' or month == 'April':
                if row['Start Time'].startswith('04', 5, 7):
                    apr_sun = ['02', '09', '16', '23', '30']
                    apr_mon = ['03', '10', '17', '24']
                    apr_tue = ['04', '11', '18', '25']
                    apr_wed = ['05', '12', '19', '26']
                    apr_thu = ['06', '13', '20', '27']
                    apr_fri = ['07', '14', '21', '28']
                    apr_sat = ['01', '08', '15', '22']
                    if row['Start Time'].startswith(tuple(apr_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(apr_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(apr_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(apr_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(apr_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(apr_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(apr_sat), 8, 10):
                        count_sat += 1
            if time_period== 'none' or month == 'May':
                if row['Start Time'].startswith('05', 5, 7):
                    may_sun = ['07', '14', '21', '28']
                    may_mon = ['01', '08', '15', '22', '29']
                    may_tue = ['02', '09', '16', '23', '30']
                    may_wed = ['03', '10', '17', '24', '31']
                    may_thu = ['04', '11', '18', '25']
                    may_fri = ['05', '12', '19', '26']
                    may_sat = ['06', '13', '20', '27']
                    if row['Start Time'].startswith(tuple(may_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(may_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(may_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(may_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(may_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(may_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(may_sat), 8, 10):
                        count_sat += 1
            if time_period== 'none' or month == 'June':
                if row['Start Time'].startswith('06', 5, 7):
                    jun_sun = ['04', '11', '18', '25']
                    jun_mon = ['05', '12', '19', '26']
                    jun_tue = ['06', '13', '20', '27']
                    jun_wed = ['07', '14', '21', '28']
                    jun_thu = ['01', '08', '15', '22', '29']
                    jun_fri = ['02', '09', '16', '23', '30']
                    jun_sat = ['03', '10', '17', '24']
                    if row['Start Time'].startswith(tuple(jun_sun), 8, 10):
                        count_sun += 1
                    elif row['Start Time'].startswith(tuple(jun_mon), 8, 10):
                        count_mon += 1
                    elif row['Start Time'].startswith(tuple(jun_tue), 8, 10):
                        count_tue += 1
                    elif row['Start Time'].startswith(tuple(jun_wed), 8, 10):
                        count_wed += 1
                    elif row['Start Time'].startswith(tuple(jun_thu), 8, 10):
                        count_thu += 1
                    elif row['Start Time'].startswith(tuple(jun_fri), 8, 10):
                        count_fri += 1
                    elif row['Start Time'].startswith(tuple(jun_sat), 8, 10):
                        count_sat += 1

    if count_sun is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Sunday is the most popular day for start time')
    elif count_mon is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Monday is the most popular day for start time')
    elif count_tue is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Tuesday is the most popular day for start time')
    elif count_wed is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Wednesday is the most popular day for start time')
    elif count_thu is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Thursday is the most popular day for start time')
    elif count_fri is max(count_sun, count_mon, count_tue, count_wed, count_thu, count_fri):
        print('Friday is the most popular day for start time')

def popular_hour(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''

    def time_count():

        count_0 = count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = 0
        count_7 = count_8 = count_9 = count_10 = count_11 = count_12 = 0
        count_13 = count_14 = count_15 = count_16 = count_17 = count_18 = 0
        count_19 = count_20 = count_21 = count_22 = count_23 = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith('00', 11, 13):
                    count_0 += 1
                elif row['Start Time'].startswith('01', 11, 13):
                    count_1 += 1
                elif row['Start Time'].startswith('02', 11, 13):
                    count_2 += 1
                elif row['Start Time'].startswith('03', 11, 13):
                    count_3 += 1
                elif row['Start Time'].startswith('04', 11, 13):
                    count_4 += 1
                elif row['Start Time'].startswith('05', 11, 13):
                    count_5 += 1
                elif row['Start Time'].startswith('06', 11, 13):
                    count_6 += 1
                elif row['Start Time'].startswith('07', 11, 13):
                    count_7 += 1
                elif row['Start Time'].startswith('08', 11, 13):
                    count_8 += 1
                elif row['Start Time'].startswith('09', 11, 13):
                    count_9 += 1
                elif row['Start Time'].startswith('10', 11, 13):
                    count_10 += 1
                elif row['Start Time'].startswith('11', 11, 13):
                    count_11 += 1
                elif row['Start Time'].startswith('12', 11, 13):
                    count_12 += 1
                elif row['Start Time'].startswith('13', 11, 13):
                    count_13 += 1
                elif row['Start Time'].startswith('14', 11, 13):
                    count_14 += 1
                elif row['Start Time'].startswith('15', 11, 13):
                    count_15 += 1
                elif row['Start Time'].startswith('16', 11, 13):
                    count_16 += 1
                elif row['Start Time'].startswith('17', 11, 13):
                    count_17 += 1
                elif row['Start Time'].startswith('18', 11, 13):
                    count_18 += 1
                elif row['Start Time'].startswith('19', 11, 13):
                    count_19 += 1
                elif row['Start Time'].startswith('20', 11, 13):
                    count_20 += 1
                elif row['Start Time'].startswith('21', 11, 13):
                    count_21 += 1
                elif row['Start Time'].startswith('22', 11, 13):
                    count_22 += 1
                elif row['Start Time'].startswith('23', 11, 13):
                    count_23 += 1

        count_list = (count_0, count_1, count_2, count_3, count_4, count_5,
                      count_6, count_7, count_8, count_9, count_10, count_11,
                      count_12, count_13, count_14, count_15, count_16,
                      count_17, count_18, count_19, count_20, count_21,
                      count_22, count_23)

        for count in count_list:
            if count is max(count_list):
                print('{} is the most popular hour for start time'.format(count_list.index(count)))

    def month_time_count(m1):

        count_0 = count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = 0
        count_7 = count_8 = count_9 = count_10 = count_11 = count_12 = 0
        count_13 = count_14 = count_15 = count_16 = count_17 = count_18 = 0
        count_19 = count_20 = count_21 = count_22 = count_23 = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('00', 11, 13):
                    count_0 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('01', 11, 13):
                    count_1 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('02', 11, 13):
                    count_2 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('03', 11, 13):
                    count_3 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('04', 11, 13):
                    count_4 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('05', 11, 13):
                    count_5 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('06', 11, 13):
                    count_6 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('07', 11, 13):
                    count_7 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('08', 11, 13):
                    count_8 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('09', 11, 13):
                    count_9 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('10', 11, 13):
                    count_10 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('11', 11, 13):
                    count_11 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('12', 11, 13):
                    count_12 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('13', 11, 13):
                    count_13 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('14', 11, 13):
                    count_14 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('15', 11, 13):
                    count_15 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('16', 11, 13):
                    count_16 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('17', 11, 13):
                    count_17 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('18', 11, 13):
                    count_18 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('19', 11, 13):
                    count_19 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('20', 11, 13):
                    count_20 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('21', 11, 13):
                    count_21 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('22', 11, 13):
                    count_22 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith('23', 11, 13):
                    count_23 += 1

        count_list = (count_0, count_1, count_2, count_3, count_4, count_5,
                      count_6, count_7, count_8, count_9, count_10, count_11,
                      count_12, count_13, count_14, count_15, count_16,
                      count_17, count_18, count_19, count_20, count_21,
                      count_22, count_23)

        for count in count_list:
            if count is max(count_list):
                print('{} is the most popular hour for start time'.format(count_list.index(count)))

    def day_time_count(m1, day):

        count_0 = count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = 0
        count_7 = count_8 = count_9 = count_10 = count_11 = count_12 = 0
        count_13 = count_14 = count_15 = count_16 = count_17 = count_18 = 0
        count_19 = count_20 = count_21 = count_22 = count_23 = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('00', 11, 13):
                    count_0 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('01', 11, 13):
                    count_1 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('02', 11, 13):
                    count_2 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('03', 11, 13):
                    count_3 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('04', 11, 13):
                    count_4 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('05', 11, 13):
                    count_5 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('06', 11, 13):
                    count_6 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('07', 11, 13):
                    count_7 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('08', 11, 13):
                    count_8 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('09', 11, 13):
                    count_9 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('10', 11, 13):
                    count_10 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('11', 11, 13):
                    count_11 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('12', 11, 13):
                    count_12 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('13', 11, 13):
                    count_13 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('14', 11, 13):
                    count_14 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('15', 11, 13):
                    count_15 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('16', 11, 13):
                    count_16 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('17', 11, 13):
                    count_17 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('18', 11, 13):
                    count_18 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('19', 11, 13):
                    count_19 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('20', 11, 13):
                    count_20 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('21', 11, 13):
                    count_21 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('22', 11, 13):
                    count_22 += 1
                elif row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10) and row['Start Time'].startswith('23', 11, 13):
                    count_23 += 1

        count_list = (count_0, count_1, count_2, count_3, count_4, count_5,
                      count_6, count_7, count_8, count_9, count_10, count_11,
                      count_12, count_13, count_14, count_15, count_16,
                      count_17, count_18, count_19, count_20, count_21,
                      count_22, count_23)

        for count in count_list:
            if count is max(count_list):
                print('{} is the most popular hour for start time'.format(count_list.index(count)))

    if time_period == 'none':
        time_count()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_time_count(m1)
        elif month == 'February':
            m1='02'
            month_time_count(m1)
        elif month == 'March':
            m1='03'
            month_time_count(m1)
        elif month == 'April':
            m1='04'
            month_time_count(m1)
        elif month == 'May':
            m1='05'
            month_time_count(m1)
        elif month == 'June':
            m1='06'
            month_time_count(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_time_count(m1, day)
        elif month == 'February':
            m1='02'
            day_time_count(m1, day)
        elif month == 'March':
            m1='03'
            day_time_count(m1, day)
        elif month == 'April':
            m1='04'
            day_time_count(m1, day)
        elif month == 'May':
            m1='05'
            day_time_count(m1, day)
        elif month == 'June':
            m1='06'
            day_time_count(m1, day)



def trip_duration(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    def get_time(sec, message):
        days = sec // 86400
        sec -= 86400*days

        hrs = sec // 3600
        sec -= 3600*hrs

        mins = sec // 60
        sec -= 60*mins

        print (message, days, 'days:', hrs, 'hrs:', mins, 'mins:', sec, 'secs')

    def none_trip_duration():
        total_trip_duration = 0
        trip_count = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                total_trip_duration += int(row['Trip Duration'])
                trip_count += 1

        average_trip = (total_trip_duration/trip_count)
        message_1 = 'Total trip duration is: '
        message_2 = 'Average trip duration is: '

        get_time(int(total_trip_duration), message_1)
        get_time(int(average_trip), message_2)

    def month_trip_duration(m1):
        total_trip_duration = 0
        trip_count = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    total_trip_duration += int(row['Trip Duration'])
                    trip_count += 1

        average_trip = (total_trip_duration/trip_count)

        message_1 = 'Total trip duration is: '
        message_2 = 'Average trip duration is: '

        get_time(int(total_trip_duration), message_1)
        get_time(int(average_trip), message_2)

    def day_trip_duration(m1, day):
        total_trip_duration = 0
        trip_count = 0

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    total_trip_duration += int(row['Trip Duration'])
                    trip_count += 1

        average_trip = (total_trip_duration/trip_count)

        message_1 = 'Total trip duration is: '
        message_2 = 'Average trip duration is: '

        get_time(int(total_trip_duration), message_1)
        get_time(int(average_trip), message_2)

    if time_period == 'none':
        none_trip_duration()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_trip_duration(m1)
        elif month == 'February':
            m1='02'
            month_trip_duration(m1)
        elif month == 'March':
            m1='03'
            month_trip_duration(m1)
        elif month == 'April':
            m1='04'
            month_trip_duration(m1)
        elif month == 'May':
            m1='05'
            month_trip_duration(m1)
        elif month == 'June':
            m1='06'
            month_trip_duration(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_trip_duration(m1, day)
        elif month == 'February':
            m1='02'
            day_trip_duration(m1, day)
        elif month == 'March':
            m1='03'
            day_trip_duration(m1, day)
        elif month == 'April':
            m1='04'
            day_trip_duration(m1, day)
        elif month == 'May':
            m1='05'
            day_trip_duration(m1, day)
        elif month == 'June':
            m1='06'
            day_trip_duration(m1, day)

def popular_stations(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    def none_popular_stations():

        start_stations=list()
        end_stations=list()

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                start_stations.append(row['Start Station'])
                end_stations.append(row['End Station'])

        start_stations_dict= defaultdict(int)
        for station in start_stations:
            start_stations_dict[station] += 1

        end_stations_dict= defaultdict(int)
        for station in end_stations:
            end_stations_dict[station] += 1

        start_max = max(start_stations_dict, key=start_stations_dict.get)
        end_max = max(end_stations_dict, key=end_stations_dict.get)

        print('The most popular start station is: '+start_max)
        print('The most popular end station is: '+end_max)
    def month_popular_stations(m1):
        start_stations=list()
        end_stations=list()

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    start_stations.append(row['Start Station'])
                    end_stations.append(row['End Station'])

        start_stations_dict= defaultdict(int)
        for station in start_stations:
            start_stations_dict[station] += 1

        end_stations_dict= defaultdict(int)
        for station in end_stations:
            end_stations_dict[station] += 1

        start_max = max(start_stations_dict, key=start_stations_dict.get)
        end_max = max(end_stations_dict, key=end_stations_dict.get)

        print('The most popular start station is: '+start_max)
        print('The most popular end station is: '+end_max)

    def day_popular_stations(m1, day):
        start_stations=list()
        end_stations=list()

        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    start_stations.append(row['Start Station'])
                    end_stations.append(row['End Station'])

        start_stations_dict= defaultdict(int)
        for station in start_stations:
            start_stations_dict[station] += 1

        end_stations_dict= defaultdict(int)
        for station in end_stations:
            end_stations_dict[station] += 1

        start_max = max(start_stations_dict, key=start_stations_dict.get)
        end_max = max(end_stations_dict, key=end_stations_dict.get)

        print('The most popular start station is: '+start_max)
        print('The most popular end station is: '+end_max)

    if time_period == 'none':
        none_popular_stations()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_popular_stations(m1)
        elif month == 'February':
            m1='02'
            month_popular_stations(m1)
        elif month == 'March':
            m1='03'
            month_popular_stations(m1)
        elif month == 'April':
            m1='04'
            month_popular_stations(m1)
        elif month == 'May':
            m1='05'
            month_popular_stations(m1)
        elif month == 'June':
            m1='06'
            month_popular_stations(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_popular_stations(m1, day)
        elif month == 'February':
            m1='02'
            day_popular_stations(m1, day)
        elif month == 'March':
            m1='03'
            day_popular_stations(m1, day)
        elif month == 'April':
            m1='04'
            day_popular_stations(m1, day)
        elif month == 'May':
            m1='05'
            day_popular_stations(m1, day)
        elif month == 'June':
            m1='06'
            day_popular_stations(m1, day)


def popular_trip(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    def none_popular_trip():

        popular_trip_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                popular_trip_list.append(row['Start Station']+' | TO | '+row['End Station'])

        popular_trip_dict= defaultdict(int)
        for trip in popular_trip_list:
            popular_trip_dict[trip] += 1
        trip_max = max(popular_trip_dict, key=popular_trip_dict.get)

        print('The most popular trip is: '+trip_max)

    def month_popular_trip(m1):

        popular_trip_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    popular_trip_list.append(row['Start Station']+' | TO | '+row['End Station'])

        popular_trip_dict= defaultdict(int)
        for trip in popular_trip_list:
            popular_trip_dict[trip] += 1
        trip_max = max(popular_trip_dict, key=popular_trip_dict.get)

        print('The most popular trip is: '+trip_max)

    def day_popular_trip(m1, day):

        popular_trip_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    popular_trip_list.append(row['Start Station']+' | TO | '+row['End Station'])

        popular_trip_dict= defaultdict(int)
        for trip in popular_trip_list:
            popular_trip_dict[trip] += 1
        trip_max = max(popular_trip_dict, key=popular_trip_dict.get)

        print('The most popular trip is: '+trip_max)

    if time_period == 'none':
        none_popular_trip()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_popular_trip(m1)
        elif month == 'February':
            m1='02'
            month_popular_trip(m1)
        elif month == 'March':
            m1='03'
            month_popular_trip(m1)
        elif month == 'April':
            m1='04'
            month_popular_trip(m1)
        elif month == 'May':
            m1='05'
            month_popular_trip(m1)
        elif month == 'June':
            m1='06'
            month_popular_trip(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_popular_trip(m1, day)
        elif month == 'February':
            m1='02'
            day_popular_trip(m1, day)
        elif month == 'March':
            m1='03'
            day_popular_trip(m1, day)
        elif month == 'April':
            m1='04'
            day_popular_trip(m1, day)
        elif month == 'May':
            m1='05'
            day_popular_trip(m1, day)
        elif month == 'June':
            m1='06'
            day_popular_trip(m1, day)


def users(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    def none_users():
        users_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users_list.append(row['User Type'])

        users_dict = defaultdict(int)
        for user in users_list:
            users_dict[user] += 1
        for element in users_dict:
            print('The count for \''+element+'\' is '+str(users_dict[element]))

    def month_users(m1):
        users_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    users_list.append(row['User Type'])

        users_dict = defaultdict(int)
        for user in users_list:
            users_dict[user] += 1
        for element in users_dict:
            print('The count for \''+element+'\' is '+str(users_dict[element]))

    def day_users(m1, day):
        users_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    users_list.append(row['User Type'])

        users_dict = defaultdict(int)
        for user in users_list:
            users_dict[user] += 1
        for element in users_dict:
            print('The count for \''+element+'\' is '+str(users_dict[element]))



    if time_period == 'none':
        none_users()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_users(m1)
        elif month == 'February':
            m1='02'
            month_users(m1)
        elif month == 'March':
            m1='03'
            month_users(m1)
        elif month == 'April':
            m1='04'
            month_users(m1)
        elif month == 'May':
            m1='05'
            month_users(m1)
        elif month == 'June':
            m1='06'
            month_users(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_users(m1, day)
        elif month == 'February':
            m1='02'
            day_users(m1, day)
        elif month == 'March':
            m1='03'
            day_users(m1, day)
        elif month == 'April':
            m1='04'
            day_users(m1, day)
        elif month == 'May':
            m1='05'
            day_users(m1, day)
        elif month == 'June':
            m1='06'
            day_users(m1, day)


def gender(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    def none_gender():
        gender_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                gender_list.append(row['Gender'])

        gender_dict = defaultdict(int)
        for gender in gender_list:
            gender_dict[gender] += 1
        for element in gender_dict:
            print('The count for \''+element+'\' is '+str(gender_dict[element]))

    def month_gender(m1):
        gender_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    gender_list.append(row['Gender'])

        gender_dict = defaultdict(int)
        for gender in gender_list:
            gender_dict[gender] += 1
        for element in gender_dict:
            print('The count for \''+element+'\' is '+str(gender_dict[element]))

    def day_gender(m1, day):
        gender_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    gender_list.append(row['Gender'])

        gender_dict = defaultdict(int)
        for gender in gender_list:
            gender_dict[gender] += 1
        for element in gender_dict:
            print('The count for \''+element+'\' is '+str(gender_dict[element]))


    if time_period == 'none':
        none_gender()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_gender(m1)
        elif month == 'February':
            m1='02'
            month_gender(m1)
        elif month == 'March':
            m1='03'
            month_gender(m1)
        elif month == 'April':
            m1='04'
            month_gender(m1)
        elif month == 'May':
            m1='05'
            month_gender(m1)
        elif month == 'June':
            m1='06'
            month_gender(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_gender(m1, day)
        elif month == 'February':
            m1='02'
            day_gender(m1, day)
        elif month == 'March':
            m1='03'
            day_gender(m1, day)
        elif month == 'April':
            m1='04'
            day_gender(m1, day)
        elif month == 'May':
            m1='05'
            day_gender(m1, day)
        elif month == 'June':
            m1='06'
            day_gender(m1, day)


def birth_years(city_file, time_period, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    def none_birth_years():

        birth_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                birth_list.append(row['Birth Year'])

        birth_dict = defaultdict(int)
        for year in birth_list:
            birth_dict[year] += 1

        print('The oldest user(s) was/were born in '+str(min(filter(None,birth_list))))
        print('The youngest user(s) was/were born in '+str(max(birth_list)))

        birth_max_count = max(birth_dict, key=birth_dict.get)
        print('The most popular birth year is '+'\''+birth_max_count+'\'')

    def month_birth_years(m1):

        birth_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7):
                    birth_list.append(row['Birth Year'])

        birth_dict = defaultdict(int)
        for year in birth_list:
            birth_dict[year] += 1

        print('The oldest user(s) was/were born in '+str(min(filter(None,birth_list))))
        print('The youngest user(s) was/were born in '+str(max(birth_list)))

        birth_max_count = max(birth_dict, key=birth_dict.get)
        print('The most popular birth year is '+'\''+birth_max_count+'\'')

    def day_birth_years(m1, day):

        birth_list = list()
        with open(city_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                    birth_list.append(row['Birth Year'])

        birth_dict = defaultdict(int)
        for year in birth_list:
            birth_dict[year] += 1

        print('The oldest user(s) was/were born in '+str(min(filter(None,birth_list))))
        print('The youngest user(s) was/were born in '+str(max(birth_list)))

        birth_max_count = max(birth_dict, key=birth_dict.get)
        print('The most popular birth year is '+'\''+birth_max_count+'\'')

    if time_period == 'none':
        none_birth_years()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_birth_years(m1)
        elif month == 'February':
            m1='02'
            month_birth_years(m1)
        elif month == 'March':
            m1='03'
            month_birth_years(m1)
        elif month == 'April':
            m1='04'
            month_birth_years(m1)
        elif month == 'May':
            m1='05'
            month_birth_years(m1)
        elif month == 'June':
            m1='06'
            month_birth_years(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_birth_years(m1, day)
        elif month == 'February':
            m1='02'
            day_birth_years(m1, day)
        elif month == 'March':
            m1='03'
            day_birth_years(m1, day)
        elif month == 'April':
            m1='04'
            day_birth_years(m1, day)
        elif month == 'May':
            m1='05'
            day_birth_years(m1, day)
        elif month == 'June':
            m1='06'
            day_birth_years(m1, day)



def display_data(city_file, time_period, month, day):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')

    def loop1(reader):
        i = 0
        while i < 5:
            print(next(reader))
            i += 1

        display = input('\nWould you like to see more?'
                         ' Type \'yes\' or \'no\'.\n')

        while display == 'yes' or display == 'Yes':
            loop1(reader)
        else:
            return

    def none_display_data():

        if display == 'yes' or display == 'Yes':
            with open(city_file) as csvfile:
                reader = csv.DictReader(csvfile)
                loop1(reader)

    def month_display_data(m1):

        if display == 'yes' or display == 'Yes':
            with open(city_file) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Start Time'].startswith(m1, 5, 7):
                        loop1(reader)

    def day_display_data(m1, day):

        if display == 'yes' or display == 'Yes':
            with open(city_file) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Start Time'].startswith(m1, 5, 7) and row['Start Time'].startswith(day, 8, 10):
                        loop1(reader)

    if time_period == 'none':
        none_display_data()

    if time_period == 'month':
        if month == 'January':
            m1='01'
            month_display_data(m1)
        elif month == 'February':
            m1='02'
            month_display_data(m1)
        elif month == 'March':
            m1='03'
            month_display_data(m1)
        elif month == 'April':
            m1='04'
            month_display_data(m1)
        elif month == 'May':
            m1='05'
            month_display_data(m1)
        elif month == 'June':
            m1='06'
            month_display_data(m1)

    if time_period == 'day':
        if month == 'January':
            m1='01'
            day_display_data(m1, day)
        elif month == 'February':
            m1='02'
            day_display_data(m1, day)
        elif month == 'March':
            m1='03'
            day_display_data(m1, day)
        elif month == 'April':
            m1='04'
            day_display_data(m1, day)
        elif month == 'May':
            m1='05'
            day_display_data(m1, day)
        elif month == 'June':
            m1='06'
            day_display_data(m1, day)


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''

    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # Choose a month
    if time_period == 'Month' or time_period == 'month':
        month = get_month()
        month = month

    # Choose a day
    if time_period == 'Day' or time_period == 'day':
        month = get_month()
        month = month
        day = get_day(month)
        day = day


    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        month = 'none'
        day = 'none'
        start_time = time.time()

        popular_month(city, time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        day = 'none'
        start_time = time.time()

        popular_day(city, time_period, month)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular hour of day for start time?
    if time_period == 'none' or time_period == 'month' or time_period == 'day':
        start_time = time.time()
        popular_hour(city, time_period, month, day)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")


    # What is the total trip duration and average trip duration?
    start_time = time.time()
    trip_duration(city, time_period, month, day)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")


    # What is the most popular start station and most popular end station?
    start_time = time.time()
    popular_stations(city, time_period, month, day)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip

    start_time = time.time()
    popular_trip(city, time_period, month, day)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    # What are the counts of each user type?

    start_time = time.time()
    users(city, time_period, month, day)

    print("That took %s seconds." % (time.time() - start_time))

    if city =='chicago.csv' or city =='new_york_city.csv':
        print("Calculating the next statistic...")

    # What are the counts of gender?
        start_time = time.time()
        gender(city, time_period, month, day)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?

        start_time = time.time()
        birth_years(city, time_period, month, day)

        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to

    display_data(city, time_period, month, day)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()



if __name__ == "__main__":
	statistics()
