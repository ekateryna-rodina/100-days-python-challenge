from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    global PYBITES_BORN
    PYBITES_BORN_month = PYBITES_BORN.month
    PYBITES_BORN_days = PYBITES_BORN.day
    for i in range(100, 900, 100):
        next_ = PYBITES_BORN + timedelta(days=i)
        temp_pyth_ = datetime(year=next_.year, month=PYBITES_BORN_month, day=PYBITES_BORN_days) 
        temp_ = next_ + timedelta(days=100)
        yield next_
        if temp_pyth_ < temp_ and temp_pyth_ > next_:
            yield temp_pyth_

