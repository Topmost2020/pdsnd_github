import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['january', 'february', 'march', 'april', 'may', 'june']
weekday_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in CITY_DATA.keys():
        print("\nYou are Welcome to this Bikeshare Program")
        print("Kindly Indicate The City You Wish To Choose From:\nChicago or New York City or Washington")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('You have typed an invalid input, please try again later')
            print("Make sure your entered the city name in small letters")
            
    month = ''
    while month not in month_list:
        print('Displaying the user input for month...')
        print("From January to June, Kindly Indicate The Month You Wish To Choose From: ")
        month = input("From January to June, Kindly Indicate The Month You Wish To Choose From:\n Answer: ").lower()
        if month not in month_list:
            print('You have typed an invalid input, please try again later')
            print("Make sure you entered the month name in small letters")
    
    day = ''
    while day not in weekday_names:
        print('Displaying the user input for day...')
        print("From Sunday to Saturday, Kindly Indicate The Day You Wish To Choose From: ")
        day = input().lower()
        if day in weekday_names:
            print('You have typed an invalid input, please try again later')
            print("Make sure you entered the day of the week in small letters")
            
      
        print("Kindly confirm if your inputs are correct,\nCity Name: {}\nMonth: {}\nDay: {}".format(city, month, day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data file into a data frame
    df = pd.read_csv(CITY_DATA[city])

    #displaying the five rows of raw data
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
        elif view_data != 'yes':
            break
    return df

   #converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   #extracting month and day of week from Start Time
   #to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

   #filtering by month if applicable
    if month != 'all':
        df = df.loc[df["month"] == month]

    #filtering by day of week if applicable
    if day != 'all':
        df = df.loc[df["day_of_week"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\nDisplaying The Most Common Month...\n')
    #Firstly, we have to convert the Start Time to Date Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Then, let's find out the month that occurred the most
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The Most Common Month is: {}.".format(popular_month))

    print('\nDisplaying The Most Common day of week...\n')
    #Firstly, we have to convert the Start Time to Date Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Then, let's find out the day of week that occurred the most
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The Most Common Day Of The Week is: {}.".format(popular_day_of_week))

    print('\nDisplaying The Most Common Start Hour...\n')
    #Firstly, we have to convert the Start Time to Date Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Then, let's find out the month that occurred the most
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The Most Common Start Hour is: {}.".format(popular_hour))
    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('\nDisplaying The Most Commonly Used Start Station...\n')
    Most_Common_Start_Station = df['Start Station'].mode()[0]
    print('The Most Common Start Station is: {}.'.format(Most_Common_Start_Station))

    print('\nDisplaying The Most Commonly Used End Station...\n')
    Most_Common_End_Station = df['End Station'].mode()[0]
    print('The Most Common End Station is: {}.'.format(Most_Common_End_Station))

    print('\nDisplaying The Most Frequently Used Start To End Station...\n')
    Trip_Combination = df['Start Station'] + ' ' + '-' + ' ' + df['End Station']
    Most_Frequent_Start_To_End_Combination = Trip_Combination.mode()[0]
    print('The Most Frequent Start and End Station is: {}.'.format(Most_Frequent_Start_To_End_Combination))

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # converting time to days, hours, minutes and seconds
    Total_Travel_Time = df['Trip Duration'].sum()

    print('Displaying keys to check number of day(s), hour(s), minute(s) and second(s)')
    Total_Travel_Time_in_days = (Total_Travel_Time // 86400)
    Total_Travel_Time_in_hours = ((Total_Travel_Time % 86400) // 3600)
    Total_Travel_Time_in_minutes = (((Total_Travel_Time % 86400) % 3600) // 60)
    Total_Travel_Time_in_seconds = (((Total_Travel_Time % 86400) % 3600) % 60)
    print('The Trip Took: {} day(s), {} hour(s), {} minute(s), {} second(s).'.format(Total_Travel_Time_in_days, Total_Travel_Time_in_hours,
    Total_Travel_Time_in_minutes, Total_Travel_Time_in_seconds))


    # converting time to hours, minutes and seconds
    Mean_Travel_Time = df['Trip Duration'].mean()
    Mean_Travel_Time_in_hours = ((Mean_Travel_Time % 86400) // 3600)
    Mean_Travel_Time_in_minutes = (((Mean_Travel_Time % 86400) % 3600) // 60)
    Mean_Travel_Time_in_seconds = (((Mean_Travel_Time % 86400) % 3600) % 60)
    print('The Mean Travel Time is: {} hour(s), {} minute(s), {} second(s).'.format(Mean_Travel_Time_in_hours,
    Mean_Travel_Time_in_minutes, Mean_Travel_Time_in_seconds))

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('Displaying the counts of user types')
    User_Types = df['User Type'].value_counts()
    print("The Counts of User Types is: {}.".format(User_Types))

    print('Displaying the counts of gender')
    try:
        gender_count = df['Gender'].value_counts()
        print("The counts of the gender are: {}.".format(gender_count))
    except:
        print("Gender stats cannot be calculated because Gender does not appear in the dataframe")


    print("\nDisplaying The Earliest, Most Recent and Most Common Year of Birth")
    try:
        Earliest_Year_Of_Birth = int(df['Birth Year'].min())
        print("The First Year of Birth is: {}.".format(Earliest_Year_Of_Birth))
        Latest_Year_Of_Birth = int(df['Birth Year'].max())
        print("The Last Year of Birth is: {}.".format(Latest_Year_Of_Birth))
        Most_Common_Year_Of_Birth = int(df['Birth Year'].mode()[0])
        print("The Most Common Year of Birth is: {}.".format(Most_Common_Year_Of_Birth))
    except:
        print("Sorry! There is no birth year for the city you entered")

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()