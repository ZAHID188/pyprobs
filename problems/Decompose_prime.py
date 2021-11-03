# Decompose a positive integer to the product of some prime numbers.
#enter 90, print out 90=2*3*3*5.


# def decompose_prime_print(n): #print out the prime numbers
#     if n <= 1:
#         return False
#     if n == 2:
#         print(n)
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     print(n)
#     return True
# print(decompose_prime_print(90))

# def decompose_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True
# print(decompose_prime(90))

# # Filename: prime.py
# from math import sqrt
# j = 2
# while j <=100:
#     i = 2
#     k= sqrt(j)
#     while i <= k:
#         if j%i == 0: 
#             break
#         i = i+1
#         if i > k:
#             print(j, end = ' ')
#         j += 1


# Filename: prime.py
# from math import sqrt
# for i in range(2,101):
#     k = int(sqrt(i))
#     for j in range(2,k+1):
#         if i%j == 0:
#             break
#         if( ):
#             print(i, end = ' ')


# Python program to display all the prime numbers within an interval

# lower = 2
# upper = 90

# def prime(x,y):
#     lower=x
#     upper=y
#     for num in range(lower,upper + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 # num=2
#                 print(num ,"*")
               

# print(prime(2,90))

          
# prime(lower,upper)
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#         #    if(num == 2):
#         #        print(num)
#            print("*",num)\


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

