# Generate  Fibonacci series 

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci()
for _ in range(10): 
    print(next(fib_gen))


# Check a string palindrome or not?

def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]  
str1 = "radar"
str2 = "hello"

print(f'"{str1}" is a palindrome: {is_palindrome(str1)}')
print(f'"{str2}" is a palindrome: {is_palindrome(str2)}')
