# import modudels for time managment
from datetime import date, timedelta

class Bite67:
    def __init__(self):
        self.start_100days = date(2017, 3, 30)
        self.pybites_founded = date(2016, 12, 19)
        self.pycon_date = date(2018, 5, 8)

# returns 100 days from kick off
def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    hundred_days_forward = start_100days + timedelta(days=100)
    return str(hundred_days_forward)

# finds delta between found and meetup 
def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return (pycon_date - pybites_founded).days