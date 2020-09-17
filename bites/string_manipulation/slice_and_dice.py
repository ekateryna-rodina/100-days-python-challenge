from string import ascii_lowercase
import re

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def slice_and_dice(text: str = another_text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    text = text.strip()
    lines = [line.strip() for line in text.split('\n') if line.strip()[0].islower()]
    searched_words = [re.findall(r'([:\)]*[a-z]*)', line.split()[-1])[0] for line in lines]
    return searched_words
    
    assert results == ['word', 'list', 'list']
        
slice_and_dice(another_text)