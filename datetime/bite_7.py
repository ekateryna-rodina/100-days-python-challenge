from datetime import datetime
import os
import urllib.request
import dateutil.parser as dt_parser
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

def convert_to_datetime(line):
    """
        Extract timestamp from logline and convert it to a datetime object.
        For example calling the function with:
        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
        returns:
        datetime(2014, 7, 3, 23, 27, 51)
    """
    pattern = r'[A-Z]\s([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2})'
    m = re.search(pattern, line)
    dt_str = m.group(1)
    dt = dt_parser.parse(dt_str)
    return dt


def time_between_shutdowns(loglines):
    """
        Extract shutdown events ("Shutdown initiated") from loglines and
        calculate the timedelta between the first and last one.
        Return this datetime.timedelta object.
    """
    first = [x for x in loglines if 'INFO 2014-07-03T23:27:51 supybot Shutdown initiated.' in x]
    last = [x for x in loglines if 'INFO 2014-07-03T23:31:22 supybot Shutdown initiated.' in x]

    data_time_f = convert_to_datetime(first[0])
    data_time_l = convert_to_datetime(last[0])
    return data_time_l - data_time_f

with open(logfile) as f:
    loglines = f.readlines()
    delta_between_shutdowns = time_between_shutdowns(loglines)
    print(f'The interval between shutdowns is {delta_between_shutdowns / 60} minutes')