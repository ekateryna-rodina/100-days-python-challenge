def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    map_color = {(0, 0, 0) : '#000000',  # black
    (255, 255, 255):'#FFFFFF',  # white
    (255, 0, 0): '#FF0000',  # red
    (0, 255, 0): '#00FF00',  # lime
    (0, 0, 255): '#0000FF',  # blue
    (255, 255, 0): '#FFFF00',  # yellow
    (0, 255, 255): '#00FFFF',  # cyan / aqua
    (255, 0, 255): '#FF00FF',  # magenta / fuchsia
    (192, 192, 192): '#C0C0C0',  # silver
    (128, 128, 128): '#808080',  # gray
    (128, 0, 0): '#800000',  # maroon
    (128, 128, 0): '#808000',  # olive
    (0, 128, 0): '#008000',  # green
    (128, 0, 128): '#800080',  # purple
    (0, 128, 128): '#008080',  # teal
    (0, 0, 128):'#000080'}  # navy}
    
    r, g, b = rgb
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        return map_color[rgb]
    else:
        raise ValueError

    
    import pytest

from rgb2hex import rgb_to_hex


@pytest.mark.parametrize("rgb, hex_", [
    # https://www.rapidtables.com/web/color/RGB_Color.html
    ((0, 0, 0), '#000000'),  # black
    ((255, 255, 255), '#FFFFFF'),  # white
    ((255, 0, 0), '#FF0000'),  # red
    ((0, 255, 0), '#00FF00'),  # lime
    ((0, 0, 255), '#0000FF'),  # blue
    ((255, 255, 0), '#FFFF00'),  # yellow
    ((0, 255, 255), '#00FFFF'),  # cyan / aqua
    ((255, 0, 255), '#FF00FF'),  # magenta / fuchsia
    ((192, 192, 192), '#C0C0C0'),  # silver
    ((128, 128, 128), '#808080'),  # gray
    ((128, 0, 0), '#800000'),  # maroon
    ((128, 128, 0), '#808000'),  # olive
    ((0, 128, 0), '#008000'),  # green
    ((128, 0, 128), '#800080'),  # purple
    ((0, 128, 128), '#008080'),  # teal
    ((0, 0, 128), '#000080'),  # navy
])
def test_rgb_to_hex(rgb, hex_):
    assert rgb_to_hex(rgb) == hex_


def test_wrong_values():
    with pytest.raises(ValueError):
        rgb_to_hex((-1, 100, 100))
        rgb_to_hex((100, 300, 200))
        rgb_to_hex((100, 200, 256))