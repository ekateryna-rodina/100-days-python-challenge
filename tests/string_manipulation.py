import pytest
from bites.string_manipulation import remove_characters
from unittest.mock import patch

@pytest.mark.parametrize("input_argument, expected_return", [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
        'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
        'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
        'Some other chars  lets delete them'),
])
def test(input_argument, expected_return):
    assert remove_characters.remove_(input_argument) == expected_return