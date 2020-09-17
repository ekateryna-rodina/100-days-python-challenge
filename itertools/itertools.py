import itertools
import sys
import time

def traffic_light():
    colors = ['green', 'amber', 'red']
    t_l = itertools.cycle(colors)
    for color in t_l:
        if color == 'green':
            print('Cross the street now!')
            time.sleep(10)
        elif color == 'amber':
            print('Faster! The light is amber')
            time.sleep(5)
        else:
            print('Stop!')
            time.sleep(10)


if __name__ == '__main__':
    traffic_light()