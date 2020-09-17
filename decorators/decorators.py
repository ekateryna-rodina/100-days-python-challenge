from functools import wraps

class make_html(object):
    '''Decorator to create html tags'''
    def __init__(self, tag=''):
        self.tag = tag
    
    def __call__(self, f):
        @wraps(f)
        def wrapped(*args):
            return '<' + self.tag + '>'+ f(*args) + '<' + self.tag + '>'
        return wrapped


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text())