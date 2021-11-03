# Decompose a positive integer to the product of some prime numbers.
#enter 90, print out 90=2*3*3*5*5*7.


def decompose(n):
    """
    Decompose a positive integer to the product of some prime numbers.
    """
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return "1 = 1"
    else:
        res = []
        while n != 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    n = n // i
                    res.append(i)
                    break
        
        return "90="+ " * ".join(str(x) for x in res)
print(decompose(90))