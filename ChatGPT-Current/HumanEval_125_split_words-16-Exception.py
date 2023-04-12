from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    >>> split_words('Hello world!')
    ['Hello', 'world!']
    >>> split_words('Hello,world!')
    ['Hello', 'world!']
    >>> split_words('abcdef')
    3
    """
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for c in txt:
            if c.islower() and ord(c) % 2 == 1:
                count += 1
        return count

def check(candidate):
    assert candidate('Hello world!') == ['Hello', 'world!']
    assert candidate('Hello,world!') == ['Hello', 'world!']
    assert candidate('Hello world,!') == ['Hello', 'world,!']
    assert candidate('Hello,Hello,world !') == ['Hello,Hello,world', '!']
    assert candidate('abcdef') == 3
    assert candidate('aaabb') == 2
    assert candidate('aaaBb') == 1
    assert candidate('') == 0

def test_check():
    check(split_words)

test_check()