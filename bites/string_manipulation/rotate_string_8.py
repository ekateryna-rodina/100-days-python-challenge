from  collections import deque
def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    another_ = list(string)
    deque_str = deque(another_)
    counter = abs(n)
    if n > 0:
        result = string[n:] + string[:n]
        return result

        assert result == 'llohe'
    else:
        while counter > 0:
            part = deque_str.pop()
            deque_str.appendleft(part)
            counter -= 1
        result = ''.join(deque_str) 
        return result

        assert result == 'lohel'
    
print(rotate('hello', 2))
print(rotate('hello', -2))