import matplotlib.pyplot as plt
import seaborn as sns

def bike_rental_hour_line(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(x='hr', y='casual', data=df, label='Casual Users', marker='o', color='skyblue')
    sns.lineplot(x='hr', y='registered', data=df, label='Registered Users', marker='X', color='salmon')

    ax.set_title('Bike Rentals per Hour', fontsize=14)
    ax.set_xlabel('Hour of the Day', fontsize=12)
    ax.set_ylabel('Number of Rentals', fontsize=12)
    ax.grid(True)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')

    return fig

def bike_rental_season_bar(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('season')[['casual', 'registered']].plot(kind='bar', ax=ax,  color=['blue', 'red'])

    ax.set_title('Average Bike Rentals by User Type on Season', fontsize=12)
    ax.set_xlabel('Season', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Average Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig

def bike_rental_holiday_bar(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('holiday')[['casual', 'registered']].plot(kind='bar', ax=ax, figsize=(8,5), color=['yellow', 'green'])

    ax.set_title('Average Bike Rentals by User Type on Holiday', fontsize=12)
    ax.set_xlabel('Holiday', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Average Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig

def bike_rental_workingday_bar(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('workingday')[['casual', 'registered']].plot(kind='bar', ax=ax, figsize=(8,5), color=['pink', 'purple'])

    ax.set_title('Average Bike Rentals by User Type on Working Day', fontsize=12)
    ax.set_xlabel('Working Day', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Average Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig

def bike_rental_weekday_bar(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('weekday')[['casual', 'registered']].plot(kind='bar', ax=ax, figsize=(8,5), color=['orange', 'yellow'])

    ax.set_title('Average Bike Rentals by User Type on Week Day', fontsize=12)
    ax.set_xlabel('Week day', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Average Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig
    
def bike_rental_month_line(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='mnth', y='cnt', data=df, marker="X", linewidth=2.5, color='purple')

    ax.set_title('Bike Sharing Rentals per Month', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_ylabel('Count of Rentals', fontsize=12)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.grid(True, linestyle='--',alpha=0.6)

    return fig

def bike_rental_weekday_line(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='weekday', y='cnt', data=df, marker="X", linewidth=2.5, color='orange')

    ax.set_title('Bike Sharing Rentals per Week Day', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    
    ax.set_ylabel('Count of Rentals', fontsize=12)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.grid(True, linestyle='--',alpha=0.6)

    return fig

