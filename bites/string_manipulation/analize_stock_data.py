import requests
import numpy as np
from collections import defaultdict
STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    cap = cap.replace('$', '')
    if 'M' in cap:
        cap = cap.replace('M', '')
        cap = float(cap)
    elif 'B' in cap:
        cap = cap.replace('B', '')
        cap = float(cap)*1000
    return cap
        


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_cap = sum([_cap_str_to_mln_float(item['cap']) for item in data if item['industry'] == industry])
    return round(industry_cap, 2)

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    filtered_stock = max(data, key=lambda i: _cap_str_to_mln_float(i['cap']))
    return filtered_stock['symbol']

def default_stock_cap():
    return 0

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    stocks = defaultdict(default_stock_cap)
    for stock in data:
        sector = stock['sector']
        cap = stock['cap']
        stocks[sector] += _cap_str_to_mln_float(cap)
    min_ = min(stocks, key = stocks.get)
    max_ = max(stocks, key = stocks.get)
    return (max_, min_)



from stocks import (_cap_str_to_mln_float,
                    get_stock_symbol_with_highest_cap,
                    get_industry_cap,
                    get_sectors_with_max_and_min_stocks)


def test_cap_str_to_mln_float():
    assert _cap_str_to_mln_float('n/a') == 0
    assert _cap_str_to_mln_float('$100.45M') == 100.45
    assert _cap_str_to_mln_float('$20.9B') == 20900


def test_get_stock_symbol_with_highest_cap():
    assert get_stock_symbol_with_highest_cap() == 'JNJ'


def test_get_industry_cap():
    assert get_industry_cap("Business Services") == 368853.27
    assert get_industry_cap("Real Estate Investment Trusts") == 243295.36


def test_get_sectors_with_max_and_min_stocks():
    assert get_sectors_with_max_and_min_stocks() == ('Finance',
                                                     'Transportation')