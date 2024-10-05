import streamlit as st
import pandas as pd
import pathlib
import dataframe
import datavisual as dv
from format import change_category, change_datetime

st.title('Dashboard Peminjaman Sepedah')

directory = pathlib.Path(__file__).parent.resolve()

file_day_path = directory.parent / 'data' / 'day.csv'
file_hour_path = directory.parent / 'data' / 'hour.csv'

df_day = pd.read_csv(file_day_path)
df_hour = pd.read_csv(file_hour_path)

change_category(df_day)
change_category(df_hour)
change_datetime(df_day)
change_datetime(df_hour)

min_date = df_day["dteday"].min()
max_date = df_day["dteday"].max()

with st.sidebar:
    dates = st.date_input(
        label='Time Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

try:
    filter_day = df_day[(df_day["dteday"] >= str(dates[0])) & 
                    (df_day["dteday"] <= str(dates[1]))]

    filter_hour = df_hour[(df_hour["dteday"] >= str(dates[0])) & 
                    (df_hour["dteday"] <= str(dates[1]))]
except IndexError:
    filter_day = df_day
    filter_hour = df_hour

#mengatur dataframe 
tenants_hour = dataframe.bike_rental_hour(filter_hour)
tenants_season = dataframe.bike_rental_season(filter_hour)
tenants_holiday = dataframe.bike_rental_holiday(filter_hour)
tenants_workingday = dataframe.bike_rental_workingday(filter_hour)
tenants_weekday = dataframe.bike_rental_weekday(filter_hour)
month_tenant_df = dataframe.bike_sharing_month(filter_day)
weekday_tenant_df = dataframe.bike_sharing_weekday(filter_day)

#mengatur datavisual
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Bike Rentals / Season',
                                        'Avg Bike Rentals on Season',
                                        'Avg Bike Rentals on Holiday',
                                        'Avg Bike Rentals on Workingday',
                                        'Avg Bike Rentals on Weekday',
                                        'Bike Sharing Rentals / Month',
                                        'Bike Sharing Rentals / Week',
                                ])

with tab1:
    fig = dv.bike_rental_hour_line(tenants_hour)
    st.pyplot(fig)

with tab2:
    fig = dv.bike_rental_season_bar(tenants_season)
    st.pyplot(fig)

with tab3:
    fig = dv.bike_rental_holiday_bar(tenants_holiday)
    st.pyplot(fig)

with tab4:
    fig = dv.bike_rental_workingday_bar(tenants_workingday)
    st.pyplot(fig)

with tab5:
    fig = dv.bike_rental_weekday_bar(tenants_weekday)
    st.pyplot(fig)

with tab6:
    fig = dv.bike_rental_month_line(month_tenant_df)
    st.pyplot(fig)

with tab7:
    fig = dv.bike_rental_weekday_line(weekday_tenant_df)
    st.pyplot(fig)



    


