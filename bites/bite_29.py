import re
def get_index_different_char(chars):
    alpha_num_pattern = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alpha_num_items = []
    other_items = []

    for i, ch in enumerate(chars):
        if ch in alpha_num_pattern:
            alpha_num_items.append((i, ch))
        else:
            other_items.append((i, ch))
    if len(alpha_num_items) > len(other_items):
        return other_items[0][0]
    else:
        return alpha_num_items[0][0]


get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'])