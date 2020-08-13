
abbr = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                'New Mexico': 'NM', 'New York': 'NY',
                'North Carolina': 'NC', 'North Dakota': 'ND',
                'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                'South Carolina': 'SC', 'South Dakota': 'SD',
                'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
st = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
                'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
                'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
                'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
                'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
                'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
                'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
                'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
                'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
                'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
                'Illinois', 'Iowa', 'Michigan', 'Delaware']
NOT_FOUND = 'N/A'
class States:
    def __init__(self):
        self.us_state_abbrev = abbr
        self.states = st
    def get_every_nth_state(self, n):
        """Return a list with every nth item (default argument n=10, so every
        10th item) of the states list above (remember: lists keep order)"""
        sorted_ = self.states[::n]
        return sorted(sorted_)

    def get_state_abbrev(self, state_name):
        """Look up a state abbreviation by querying the us_state_abbrev
        dict by full state name, for instance 'Alabama' returns 'AL',
        'Illinois' returns 'IL'.
        If the state is not in the dict, return 'N/A' which we stored
        in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
        return self.us_state_abbrev.get(state_name, NOT_FOUND)


    def get_longest_state(self, data):
        """Receives data, which can be the us_state_abbrev dict or the states
        list (see above). It returns the longest state measured by the length
        of the string"""
        max_ = 0
        max_state = ''
        for  d in data:
            len_= len(d)
            max_ = max(max_, len_)
            if max_ == len_:
                max_state = d
        return max_state
            
    def combine_state_names_and_abbreviations(self):
        """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
        the us_state_abbrev dict, and the last 10 states from the states
        list (see above) and combine them into a new list. The resulting list
        has both sorted, so:
        ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
        (see also test_combine_state_names_and_abbreviations)"""
        test_combine_state_names_and_abbreviations = []
        sorted_keys = [self.us_state_abbrev[key] for key in self.us_state_abbrev.keys()][:10]
        another = sorted(states)[-10:]
        combined = sorted(sorted_keys + another)
        return combined


statess= States()
print(statess.get_every_nth_state(10))