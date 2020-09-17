names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()
middle_col_len = 11

def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, n_c in enumerate(zip(names, countries)):
        print('{num}. {name: <11}{country}'.format(num=i+1, name=n_c[0], country=n_c[1]))
