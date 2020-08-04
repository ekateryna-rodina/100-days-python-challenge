from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    try:
        to_datetime = datetime.strptime(date, '%d %b, %Y')
        year = to_datetime.year
        diff_from_this_year = THIS_YEAR - year
        return diff_from_this_year
    except ValueError:
        print('Cannot convert')

def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    try:
        date_eu_str = datetime.strptime(date, '%d/%m/%Y')
        year_eu, month_eu, day_eu = date_eu_str.year, date_eu_str.month, date_eu_str.day
        us_date = datetime(year_eu, month_eu, day_eu, day_eu)
        us_date_str = datetime.strftime(us_date, '%m/%d/%Y')
        return us_date_str
    except ValueError:
        print('Cannot convert')



years_ago('8 Aug, 2015')
convert_eu_to_us_date('11/03/2002')