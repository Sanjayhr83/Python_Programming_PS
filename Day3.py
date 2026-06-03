# Day-3 Number Program's

# To check the given number is prime_number(divisible by 1 or itself) or not
def prime_number(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return f"{n} is Prime number"
    else:
        return f"{n} is not Prime number"
n=int(input("Enter a number: "))
print(prime_number(n))

#To reverse the number from given number
def rev_num(n):
    rev=0
    while n>0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    return rev
n=int(input("Enter a number: "))
print(rev_num(n))

#To reverse the number from given number check if palindrome or not
def num_palindrome(n):
    rev=0
    temp=n
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if n==rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
n=int(input("Enter a number: "))
print(num_palindrome(n))

#To check whether the given number is armstrong number or not
"""armstrong number: sum of power(length of number) of individual digits equal to given number
 Ex : n=12 (not a armstrong number)
      1^2 + 2^2
      1+4=5

      n=153 (it is a armstrong number)
       1^3+5^3+3^3
      1+125+27=153
 """
def armstrong_num(n):
    sum=0
    for i in str(n):
        num=int(i)
        sum=sum+num**len(str(n))
    if sum==n:
        return f"{n} is an Armstrong number."
    else:
        return f"{n} is not an Armstrong number."
n=int(input("Enter a number: "))
print(armstrong_num(n))
"""---------------------OR------------------"""
def is_armstrong(number):
    # Convert number to string to easily find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    # Calculate the sum of digits raised to the power of num_digits
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum is equal to the original number
    return total_sum == number
# Test the function
user_input = int(input("Enter a number to check: "))
if is_armstrong(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is NOT an Armstrong number.")

#To check whether the given number is strong number or not
"""strong number : sum of factorial of individual digit is equal to given number
ex: n=12 (not a strong number)
    1!+2!
    1+2 = 3

    n=145 (it is a strong number)
    1!+4!+5!
    1+24+120 = 145
"""
def strong_num(n):
    total_sum = 0
    for i in str(n):
        num=int(i)
        fact=1
        for j in range(1,num+1):
            fact=fact*j
        total_sum=total_sum+fact
    if total_sum==n:
        return f"{n} strong number"
    else:
        return f"{n} not strong number"
n=int(input("enter the number : "))
print(strong_num(n))

#to check whether given number is perfect number or not
"""
perfect number : sum of the number is equal is given number
ex: n=8 (not a perfect number)
    1+2+4=7

    n=6 (it is a perfect number)
    1+2+3=6
"""
def perfect_num(n):
    total_sum=0
    for i in range(1,n):
        if n%i==0:
            total_sum=total_sum+i
    if total_sum==n:
        return f"{n} is a perfect number"
    else:
        return f"{n} is not a perfect number"
n=int(input("enter the number : "))
print(perfect_num(n))

#to find factorial of given number
"""-------using for loop------"""
def find_factorial(n):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Factorial does not exist for negative numbers"
    fact = 1
    # Loop from 1 up to n (n + 1 is exclusive)
    for i in range(1, n + 1):
        fact = fact * i
    return f"The factorial of {n} is {fact}"
# Test the function
num = int(input("Enter a number: "))
print(find_factorial(num))
"""-------math built-in functions-------"""
import math
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    # math.factorial(num) does all the multiplication automatically
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")

# to find gcd/hcf of two number
"""
The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor), of two numbers is the largest positive integer that perfectly divides both numbers without leaving a remainder.
For example, the GCD of 12 and 18 is 6 because:
        Factors of 12: 1, 2, 3, 4, 6, 12
        Factors of 18: 1, 2, 3, 6, 9, 18
"""
"""------------Using the Euclidean Algorithm-----------"""
def find_gcd(a, b):
    # Repeat until b becomes 0
    while b != 0:
        a, b = b, a % b
    return a
# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = find_gcd(num1, num2)
print(f"The GCD/HCF of {num1} and {num2} is: {result}")
"""-------math built-in functions-------"""
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# math.gcd() handles the calculation instantly
result = math.gcd(num1, num2)
print(f"The GCD/HCF of {num1} and {num2} is: {result}")

#to find lcm of two number
"""
The LCM (Least Common Multiple) of two numbers is the smallest positive integer that is perfectly divisible by both numbers.
For example, the LCM of 4 and 6 is 12 because 12 is the smallest number that appears in both of their timetables:
Multiples of 4: 4, 8, 12, 16, 20
Multiples of 6: 6, 12, 18, 24
"""
"""-------Using the GCD Formula-------"""
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_lcm(a, b):
    # LCM formula: (a * b) divided by their GCD
    # We use integer division (//) to get a clean whole number
    return (a * b) // find_gcd(a, b)
# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

"""-------math built-in functions-------"""
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# math.lcm() handles the calculation instantly
result = math.lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

#to convert the decimal to binary
"""-------------The Algorithmic Way (Using a Loop)-------------"""
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str  # Append to the front to reverse it
        n = n // 2  # Integer division to reduce the number
    return binary_str
# Test the function
decimal_num = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_num)
print(f"The binary equivalent is: {binary_result}")

"""--------------Using Python's Built-in bin() Function (Cleanest Way)-----------"""
decimal_num = int(input("Enter a decimal number: "))
# bin() returns a string starting with '0b' (indicating binary)
# We use [2:] to slice off the '0b' prefix
binary_result = bin(decimal_num)[2:]
print(f"The binary equivalent is: {binary_result}")

#to convert binary to decimal
"""-----------------The Algorithmic Way (Using a Loop)---------------"""
def binary_to_decimal(binary_str):
    decimal_val = 0
    power = 0
    # Process the string from right to left using slicing [::-1]
    for digit in binary_str[::-1]:
        if digit == '1':
            decimal_val += 2 ** power
        power += 1
    return decimal_val
# Test the function
binary_input = input("Enter a binary number: ")
result = binary_to_decimal(binary_input)
print(f"The decimal equivalent is: {result}")

"""-------------using Python's Built-in int() function--------------"""
binary_input = input("Enter a binary number: ")
# The second argument '2' tells Python the input string is in base-2 (binary)
decimal_result = int(binary_input, 2)
print(f"The decimal equivalent is: {decimal_result}")

#to Swap two number with using temporary variable
def with_temp(n1,n2):
    print(f"n1 values before {n1}, n2 values before {n2}")
    temp=n1
    n1=n2
    n2=temp
    return f"n1 values after {n1}, n2 values after {n2}"
n1=int(input("enter first number1(n1) : "))
n2=int(input("enter second number2(n2) : "))
print(with_temp(n1,n2))

#to swap two numbers without using temporary variable
def without_temp(n1, n2):
    print(f"Before: n1 = {n1}, n2 = {n2}")
    # The simultaneous swap
    n1, n2 = n2, n1
    return f"After:  n1 = {n1}, n2 = {n2}"
n1 = int(input("Enter first number1(n1): "))
n2 = int(input("Enter second number2(n2): "))
print(without_temp(n1, n2))
