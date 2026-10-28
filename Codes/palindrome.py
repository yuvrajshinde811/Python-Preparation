num = input("Enter a number: ")

def palindrome(num):
    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
        
palindrome(num)