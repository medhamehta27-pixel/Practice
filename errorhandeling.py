#Error Handeling (Complietime error, logical error, runtime error)
#runtime error

a=5
b=8

try:

    k = int(input('Enter a number'))
    print(k)
    print('Division is', a/k)

except ZeroDivisionError as e:
    print('Hey you cannot divide a number by 0',e)

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Error')

finally:
    print('closed')