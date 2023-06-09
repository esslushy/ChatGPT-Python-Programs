def simplify(x: str, n: str) -> bool:
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    >>> simplify('1/5', '5/1')
    True
    >>> simplify('1/6', '2/1')
    False
    >>> simplify('7/10', '10/2')
    False
    """
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    product_num = x_num * n_num
    product_denom = x_denom * n_denom
    gcd = find_gcd(product_num, product_denom)
    simplified_num = product_num // gcd
    simplified_denom = product_denom // gcd
    return simplified_denom == 1

def find_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def check(candidate):
    assert candidate('1/5', '5/1') == True
    assert candidate('1/6', '2/1') == False
    assert candidate('5/1', '3/1') == True
    assert candidate('7/10', '10/2') == False
    assert candidate('2/10', '50/10') == True
    assert candidate('7/2', '4/2') == True
    assert candidate('11/6', '6/1') == True
    assert candidate('2/3', '5/2') == False
    assert candidate('5/2', '3/5') == False
    assert candidate('2/4', '8/4') == True
    assert candidate('2/4', '4/2') == True
    assert candidate('1/5', '5/1') == True
    assert candidate('1/5', '1/5') == False

def test_check():
    check(simplify)

test_check()
