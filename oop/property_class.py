from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self._name = name, 
        self._expires = expires
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def set_name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            print('Name must be a string')
    @property
    def expires(self):
        return self._expires
    
    @expires.setter
    def set_expires(self, value):
        if isinstance(value, datetime):
            self._expires = value
        else:
            print('Expires must be a datetime')
    @property
    def expired(self):
        past_time = NOW - timedelta(seconds=3)
        if self._expires <= past_time:
            return True
        else:
            return False

past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired)
    

from datetime import timedelta
import inspect

