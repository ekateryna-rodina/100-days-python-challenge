MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""
    def __init__(self, *args):
        dict.__init__(self, *args)

    def _same_bd_count(self, value):
        same_bd = dict(filter(lambda bd: bd[1].day == value.day and bd[1].month == value.month, self.items()))
        return len(same_bd)

    def __setitem__(self, key, value):
        same_bd_count = self._same_bd_count(value)
        if same_bd_count > 0:
            print(MSG.format(key))
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)