# Enter an integer to find the number in its reverse order.
# Note: although it is easy to get the reverse number of a number by string slicing,
# it is a good example for logical thinking to get the reverse number by using an loop.

def reverse_order():
    n=int(input("Enter an integer: "))
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return reverse
print(reverse_order())

