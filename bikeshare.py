import time , datetime
import pandas as pd
import numpy as np

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """while True:
        print('To proceed with data analysis please select the city to proceed working on from \n    1- Chicago\n    2- New York City  \n    3- Washington )')
        city = input('Enter city option number: ').lower()
        if city in ['1', '2', '3']:
            break
        else:
            print ('Invalid city input, please enter proper city number from the provided list.')
    """
    city_validation_list = ['1', '2', '3']
    city_print_txt = 'To proceed with data analysis please select the city to proceed working on from \n    1- Chicago\n    2- New York City  \n    3- Washington'
    city_input_txt = 'Enter city option number: '
    city_error_txt = 'Invalid city input, please enter proper city number from the provided list.'
    city = data_entry_validation (city_validation_list, city_print_txt, city_input_txt, city_error_txt)
    # prompt the user for extra filtration on month or day

    #while True:
        #print('Please state the filteration level required, possible values are: \n    none: for no extra filtration \n    month: for month only filteration \n    day: for day of week \n    both: for both month and day of week filteration')
        #filter_option = input('Please select filteration required: ').lower()
    filter_option = data_entry_validation (['month', 'day', 'none', 'both'],'Please state the filteration level required, possible values are: \n    none: for no extra filtration \n    month: for month only filteration \n    day: for day of week \n    both: for both month and day of week filteration','Please select filteration required: ','Invalid input, please enter proper value from mentioned options.')
    if filter_option == 'month':
        #print ('Please select the requested month using full month name.')
        #month = input('Enter Month:').lower()
        month = data_entry_validation (['january', 'february', 'march', 'april', 'may', 'june'], 'Please select the requested month using full month name.', 'Enter Month:', 'Invalid Month please enter proper value.')
        day = 'all'
    #    break
    elif filter_option == 'day':
        month = 'all'
        #print ('Please select the requested day of week (sunday, monday, tuesday, wednsday, thursday, friday, saturday).')
        #day = input('Enter Day of Week:').lower()
        day = data_entry_validation (['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'], 'Please select the requested day of week (sunday, monday, tuesday, wednsday, thursday, friday, saturday).', 'Enter Day of Week:', 'Invalid Day please enter proper value.')
    #    break
    elif filter_option == 'none':
        day = 'all'
        month = 'all'
    #    break
    elif filter_option == 'both':
        #print ('Please select the requested month using full month name.')
        #month = input('Enter Month:').lower()
        month = data_entry_validation (['january', 'february', 'march', 'april', 'may', 'june'], 'Please select the requested month using full month name.', 'Enter Month:', 'Invalid Month please enter proper value.')
        #print ('Please select the requested day of week (sunday, monday, tuesday, wednsday, thursday, friday, saturday).')
        #day = input('Enter Day of Week:').lower()
        day = data_entry_validation (['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'], 'Please select the requested day of week (sunday, monday, tuesday, wednsday, thursday, friday, saturday).', 'Enter Day of Week:', 'Invalid Day please enter proper value.')

    #    break
    #else:
    #    print ('Invalid input, please enter proper value from mentioned options.')



    # Return proper values
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

    # extract city proper file

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # extract day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        print ('The most popular month in the period selected is: {}'.format(month))
    else:
        print ('You already selected one month which is: {}'.format(month))


    # display the most common day of week
    if day == 'all':
        popular_day_of_week = df['day_of_week'].mode()[0]
        print ('The most popular day of week in the period selected is: {}'.format(popular_day_of_week))
    else:
        print ('You already selected one day of week which is: {}'.format(day))
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print ('The most popular hour in the period selected is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ('The most popular start station in the period selected is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ('The most popular end station in the period selected is: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['route'] = 'From: ' + df['Start Station'] + ' To: '  + df['End Station']
    popular_route = df['route'].mode()[0]
    print ('The most popular route in the period selected is: {}'.format(popular_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = datetime.timedelta(seconds = int(df['Trip Duration'].sum()))
    #print(total_duration)
    print ('The total trip duration in the period selected is: {}'.format(total_duration))

    # display mean travel time
    mean_duration= datetime.timedelta(seconds = int(df['Trip Duration'].mean()))
    print ('The average trip duration in the period selected is: {}'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types statistics is as follows:\n{}'.format(user_types))

    # Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print('The Gender statistics is as follows:\n{}'.format(gender_counts))


    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        youngest = int(df['Birth Year'].max())
        eldest = int(df['Birth Year'].min())
        popular_year_of_bith = int(df['Birth Year'].mode()[0])
        print('Customer age statistics are:')
        print('The most common birth year is: {}'.format(popular_year_of_bith))
        print('The eldest birth year is: {}'.format(eldest))
        print('The youngest birth year is: {}'.format(youngest))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_entry_validation(validation_list, print_txt, input_txt,error_txt):
    while True:
        print (print_txt)
        parameter_value = input (input_txt).lower()
        if parameter_value in validation_list:
            print ('The selected value is: {}'.format(parameter_value))
            print('-'*40)
            break
        else:
            print (error_txt)
    return parameter_value

def display_data (df):
    view_data = data_entry_validation (['yes', 'no' ], 'Would you like to view 5 rows of individual trip data?', 'Enter yes or no?: ', 'Please enter a valid option')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = data_entry_validation (['yes', 'no' ], 'Would you like to repeat and view more 5 rows?', 'Enter yes or no?: ', 'Please enter a valid option')


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df,city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y']:
            break

if __name__ == "__main__":
	main()
