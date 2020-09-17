PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    no_duplicates = list(dict.fromkeys(names))
    titled_no_duplicates = [name.title() for name in no_duplicates]
    return titled_no_duplicates

    assert no_duplicates == ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos', 
                                'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites', 
                                'al pacino', 'brad pitt', 'matt damon']
    


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_names = sorted(names, key=lambda n: n.split()[1], reverse=True)
    return sorted_names


    assert sorted_names == [['Julian Sequeira', 'Arnold Schwarzenegger', 'Keanu Reeves', 'Julbob Pybites', 
                                'Brad Pitt', 'Al Pacino', 'Matt Damon', 'Sandra Bullock', 'Bob Belderbos', 'Alec Baldwin']]
def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest = min(names, key=lambda n: len(n.split()[0]))
    shortest_name = shortest.split()[0]
    return shortest_name

    assert shortest == 'Dan'

names = dedup_and_title_case_names(PY_CONTENT_CREATORS)
names = sort_by_surname_desc(names)
print(shortest_first_name(names))
