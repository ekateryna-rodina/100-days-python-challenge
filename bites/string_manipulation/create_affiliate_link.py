import re
def generate_affiliation_link(url):
    match = re.search(r'(?<=dp\/)([0-9a-zA-Z]+)\/?', url).groups(0)
    return f'http://www.amazon.com/dp/{match[0]}/?tag=pyb0f-20'

generate_affiliation_link('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art')