class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self._max = float('-inf')
    def __call__(self, value):
        max_ = max(self._max, value)
        self._max = max_
        return self._max