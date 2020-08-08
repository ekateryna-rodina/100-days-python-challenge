from collections import Counter, defaultdict
import re
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    result = ', '.join([car for car in cars['Jeep']])
    return result


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    result = []
    for family, model in cars.items():
        result.append(model[0])
    # assert(len(result)) == 5
    return result


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    # pattern = cars.any(lambda car: return re.search(r'trail', car, flags=re.I)
    result = []
    for family, models in cars.items():
        for model in models:
            if re.search(grep, model, flags=re.I):
                result.append(model)
    return sorted(result)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    dict_copy = defaultdict(list)
    for family in cars.keys():
        dict_copy[family] = sorted(cars[family])
    return dict_copy