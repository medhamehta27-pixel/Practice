# Bubble sort
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                c = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = c

nums = [7,15, 10,9,6,2]
sort(nums)

print(nums)