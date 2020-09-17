import os
import sys
import requests
import json
import re

url = 'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py'
resource = requests.get(url)
text = re.sub(r'COLOR_NAMES =|(\n)', '', resource.text)
text = re.sub(r'[(]|[)]', '"', text)
text = re.sub(r',(?=})', '', text)

COLOR_NAMES = json.loads(text)
COLOR_NAMES = {k: tuple(map(int, v.split(', '))) for k, v in COLOR_NAMES.items()}


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color=None):
        self.rgb = COLOR_NAMES.get(color.upper()) if color else None

    @staticmethod
    def hex2rgb(value):
        """Class method that converts a hex value into an rgb one"""
        if not value.startswith('#') or len(value) != 7:
            raise ValueError
        value = value.lstrip('#')
        try:
            int(value, 16)
        except ValueError:
            raise

        lv = len(value)
        rgb_ =  tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
        return rgb_

        
    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if rgb not in COLOR_NAMES.values():
            raise ValueError
        hex_ = '%02x%02x%02x' % rgb
        return f'#{hex_}'

    def __repr__(self):
        """Returns the repl of the object"""
        color = [k for k, v in COLOR_NAMES.items() if v == self.rgb]
        return f"{self.__class__.__name__}('{color[0].lower()}')" if color else 'Unknown'

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb is not None else 'Unknown'

