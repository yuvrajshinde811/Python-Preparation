def factorial(n):

    fact = 1
    for i in range(1, n):
        fact = fact * n
        n = n - 1
    print(fact)

factorial(5)