num = 1234
print("Original number:", num)

rev_num = 0

while num > 0:
    last_digit = num % 10
    print(last_digit)
    
    rev_num = (rev_num *10) + last_digit
    print(rev_num)
    
    num = num // 10
    print(num)


print("Reversed number",rev_num)