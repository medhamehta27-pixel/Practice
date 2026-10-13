# Factorial of a number
n = int(input('Enter the number'))

def fact(n):
    if n == 0:
        return 1
    else :
        return n*fact(n-1)

e= fact(n)
print('Factorial of the number is:', e)