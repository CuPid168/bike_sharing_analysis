import pandas as pd

def change_datetime(df):
    df['dteday'] = pd.to_datetime(df['dteday'])

def change_category(df):
    season_map = {
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    }
    df['season'] = df['season'].map(season_map)

    year_map = {0: 2011, 1: 2012}
    df['yr'] = df['yr'].map(year_map)

    month_map = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
        }

    df['mnth'] = df['mnth'].map(month_map)

    holiday_map = {0: 'no', 1: 'yes'}
    df['holiday'] = df['holiday'].map(holiday_map)

    weekday_map = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    df['weekday'] = df['weekday'].map(weekday_map)

    workingday_map = {0: 'No', 1: 'Yes'}
    df['workingday'] = df['workingday'].map(workingday_map)

    weatherlist_map = {
        1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
        2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
        3: 'Light Snow, Light',
        4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'
    }
    df['weathersit'] = df['weathersit'].map(weatherlist_map)
