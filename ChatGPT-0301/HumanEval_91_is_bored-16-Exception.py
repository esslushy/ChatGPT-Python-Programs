def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """
    # Initialize the boredom count to 0
    boredom_count = 0
    
    # Split the string into sentences
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith('I'):
            # Increment the boredom count
            boredom_count += 1
        else:
            # Split the sentence into sub-sentences
            sub_sentences = sentence.split('?')
            sub_sentences = [s.strip() for s in sub_sentences if s.strip()]
            
            for sub_sentence in sub_sentences:
                # Check if the sub-sentence starts with "I"
                if sub_sentence.startswith('I'):
                    # Increment the boredom count
                    boredom_count += 1
    
    # Return the boredom count
    return boredom_count

def check(candidate):
    assert candidate('Hello world') == 0
    assert candidate('Is the sky blue?') == 0
    assert candidate('I love It !') == 1
    assert candidate('bIt') == 0
    assert candidate('I feel good today. I will be productive. will kill It') == 2
    assert candidate('You and I are going for a walk') == 0

def test_check():
    check(is_bored)

test_check()