"""
Counting Sundays
Problem 19
"""

months = {
    1 : 31, # January
    2 : 29, # February
    3 : 31, # March
    4 : 30, # April
    5 : 31, # May
    6 : 30, # June
    7 : 31, # July
    8 : 31, # August
    9 : 30, # September
    10 : 31, # October
    11 : 30, # November
    12 : 31, # December
}

if __name__ == '__main__':
    # Unfortunately another lame Project Euler question that's super dirty.

    # We store the current day as an array with day/month/year
    current_sunday = { 'day' : 7, 'month' : 1, 'year' : 1900 }
    sundays = 0

    # Go through every sunday from 1900 to 2000
    while current_sunday['year'] < 2001:
        # Increment to the next sunday, seven days later
        current_sunday['day'] += 7

        # Check if it's the next month (including leap years!)
        leap_year = (current_sunday['month'] == 2 and current_sunday['year'] % 4 == 0 and \
                     current_sunday['year'] % 400 != 0 and current_sunday['day'] > 28)
        if current_sunday['day'] > months[current_sunday['month']] or leap_year:
            # If it's december, do a loop around to january
            if current_sunday['month'] == 12:
                current_sunday['day'] -= months[12]
                current_sunday['month'] = 1
                current_sunday['year'] += 1
            else:
                current_sunday['day'] -= months[current_sunday['month']] + leap_year
                current_sunday['month'] += 1

        # Check if it's on the first
        if current_sunday['day'] == 1 and 2001 > current_sunday['year'] > 1900:
            sundays += 1

    print sundays
