class Fabo():
    num = int(input("Enter a number : "))
    a, b = 0, 1
    
    print("Fibonacci Series:")
    for i in range(num):
        print(a , end=" ")
        a, b = b, a + b
        
f1 = Fabo()
