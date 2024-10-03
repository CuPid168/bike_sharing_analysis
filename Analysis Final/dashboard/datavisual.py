import matplotlib.pyplot as plt
import seaborn as sns

def bike_rental_hour_line(df):
    plt.figure(figsize=(10, 6))

    sns.lineplot(x='hr', y='casual', data=df, label='Casual Users', marker='o', color='skyblue')
    sns.lineplot(x='hr', y='registered', data=df, label='Registered Users', marker='X', color='salmon')

    plt.title('Bike Rentals by Hour (Casual vs Registered)', fontsize=14)
    plt.xlabel('Hour of the Day', fontsize=12)
    plt.ylabel('Number of Rentals', fontsize=12)
    plt.grid(True)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')

def bike_rental_season_bar(df):
    plt.figure(figsize=(8, 5))

    df.set_index('season')[['casual', 'registered']].plot(kind='bar', figsize=(8,5), color=['blue', 'red'])

    plt.title('Average Bike Rentals by User Type on Season', fontsize=12)
    plt.xlabel('Season', fontsize=12)
    plt.xticks(rotation=0)
    plt.ylabel('Average Number of Rentals', fontsize=12)

    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')

def bike_rental_holiday_bar(df):
    plt.figure(figsize=(8, 5))

    df.set_index('holiday')[['casual', 'registered']].plot(kind='bar', figsize=(8,5), color=['yellow', 'green'])

    plt.title('Average Bike Rentals by User Type on Holiday', fontsize=12)
    plt.xlabel('Holiday', fontsize=12)
    plt.xticks(rotation=0)
    plt.ylabel('Average Number of Rentals', fontsize=12)

    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')

def bike_rental_workingday_bar(df):
    plt.figure(figsize=(8, 5))

    df.set_index('workingday')[['casual', 'registered']].plot(kind='bar', figsize=(8,5), color=['pink', 'purple'])

    plt.title('Average Bike Rentals by User Type on Working Day', fontsize=12)
    plt.xlabel('Working Day', fontsize=12)
    plt.xticks(rotation=0)
    plt.ylabel('Average Number of Rentals', fontsize=12)

    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')

def bike_rental_weekday_bar(df):
    plt.figure(figsize=(8, 5))

    df.set_index('weekday')[['casual', 'registered']].plot(kind='bar', figsize=(8,5), color=['orange', 'yellow'])

    plt.title('Average Bike Rentals by User Type on Week Day', fontsize=12)
    plt.xlabel('Week day', fontsize=12)
    plt.xticks(rotation=0)
    plt.ylabel('Average Number of Rentals', fontsize=12)

    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.legend(title='User Type')\
    
def bike_rental_month_line(df):
    plt.figure(figsize=(8, 6))

    sns.lineplot(x='mnth', y='cnt', data=df, marker="X", linewidth=2.5, color='purple')

    plt.title('Bike Sharing Rentals per Month', fontsize=14, fontweight='bold')
    plt.xlabel('')
    plt.xticks(rotation=45)
    plt.ylabel('Count of Rentals', fontsize=12)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.grid(True, linestyle='--',alpha=0.6)

def bike_rental_weekday_line(df):
    plt.figure(figsize=(8, 6))
    sns.lineplot(x='weekday', y='cnt', data=df, marker="X", linewidth=2.5, color='orange')

    plt.title('Bike Sharing Rentals per Week Day', fontsize=14, fontweight='bold')
    plt.xlabel('')
    plt.xticks(rotation=45)
    plt.ylabel('Count of Rentals', fontsize=12)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    plt.grid(True, linestyle='--',alpha=0.6)