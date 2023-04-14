def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    >>> check_if_last_char_is_a_letter('apple pie')
    False
    >>> check_if_last_char_is_a_letter('apple pi e')
    True
    >>> check_if_last_char_is_a_letter('apple pi e ')
    False
    >>> check_if_last_char_is_a_letter('')
    False
    """
    if txt == "":
        return False
    
    # remove whitespace at end of string
    txt = txt.rstrip()
    
    # get the last character of the string
    last_char = txt[-1]
    
    # check if the last character is alphabetical
    if last_char.isalpha():
        # get the substring before the last character
        substr = txt[:-1]
        # split the substring by spaces to get a list of "words"
        words = substr.split()
        # check if the last character is the last character of a "word"
        if len(words) == 0:
            return True
        last_word = words[-1]
        if last_char in last_word:
            return False
        else:
            return True
    else:
        return False

def check(candidate):
    assert candidate('apple') == False
    assert candidate('apple pi e') == True
    assert candidate('eeeee') == False
    assert candidate('A') == True
    assert candidate('Pumpkin pie ') == False
    assert candidate('Pumpkin pie 1') == False
    assert candidate('') == False
    assert candidate('eeeee e ') == False
    assert candidate('apple pie') == False
    assert candidate('apple pi e ') == False

def test_check():
    check(check_if_last_char_is_a_letter)

test_check()