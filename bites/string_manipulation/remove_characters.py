import pytest
import re

def remove_(str_):
    match = re.findall(r'\w+|\s', str_)
    return ''.join(match)

remove_('Hello, I am Tim.')