import pandas as pd

def bike_rental_hour(df):
    tenants_hour_df = df.groupby('hr').agg({
    'casual': 'sum',
    'registered': 'sum'
    }).reset_index()
    return tenants_hour_df

def bike_rental_season(df):
    tenants_season = df.groupby('season').agg({
    'casual': 'mean',
    'registered': 'mean'
    }).reset_index()
    return tenants_season

def bike_rental_holiday(df):
    tenants_holiday = df.groupby('holiday').agg({
    'casual': 'mean',
    'registered': 'mean'
    }).reset_index()
    return tenants_holiday

def bike_rental_workingday(df):
    tenants_workingday = df.groupby('workingday').agg({
    'casual': 'mean',
    'registered': 'mean'
    }).reset_index()
    return tenants_workingday

def bike_rental_weekday(df):
    tenants_weekday = df.groupby('weekday').agg({
    'casual': 'mean',
    'registered': 'mean'
    }).reset_index()
    return tenants_weekday

def bike_sharing_month(df):
    month_tenant_df = df.groupby('mnth')['cnt'].sum().reset_index()
    return month_tenant_df

def bike_sharing_month(df):
    weekday_tenant_df = df.groupby('weekday')['cnt'].sum().reset_index()
    return weekday_tenant_df