#Linear Search

def search(list, m):
    print(list)
    print(m)
    for i in range(len(arr)):
        if arr[i] == k:
            return True
        return False
    
arr = [3,4,5,6,1,2,9]

k = int(input('Enter the number you want to search for??'))

if search(arr,k):
    print('Found')
else:
    print('Not Found')