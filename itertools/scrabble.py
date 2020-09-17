from itertools import permutations
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

def len_(x):
    return len(x)
def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    result = []
    permutations = _get_permutations_draw(draw)
    max_ = ''
    for p in permutations:
        p_ = ''.join(p).lower()
        all_ = [w for w in dictionary if p_.startswith(w)]
        words_ = max(all_, key=len)
        result.append(words_)
    return set(result)

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return list(permutations(draw))


print(get_possible_dict_words(['O', 'N', 'V', 'R', 'A', 'Z', 'H']))
