def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """Returns True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 2:
        return False
    primes = []
    for i in range(2, a):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.append(i)
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False

def check(candidate):
    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(105) == True
    assert candidate(126) == False
    assert candidate(729) == False
    assert candidate(891) == False
    assert candidate(1001) == True

def test_check():
    check(is_multiply_prime)

test_check()
