#Binary Search, all values must be sorted
pos=-1

def search(list, m):
    l = 0;
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == m:
            globals()['pos'] = mid
            return True
        elif list[mid] < m:
            l = mid
        else:
            u = mid
    return False

    
arr = [4,6,8,9,10,14]

k = int(input('Enter the number you want to search for??'))

if search(arr,k):
    print('Found at position', pos+1)
else:
    print('Not Found')