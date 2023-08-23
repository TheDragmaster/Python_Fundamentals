#Arrays (called lists in python)
arr = [1, 2, 3, 4]
print(arr)

nums = [1, 2, 3]

#Using index
for i in range(len(nums)):
    print(nums[i])

#Without index
for n in nums:
    print(n)

#with index and value
for i, n in enumerate(nums):
    print(i, n)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr[0] = 0
arr[3]  = 0
print(arr)

#call the last value in the array with -1
print(arr[-1])

#Sublists (aka slicing the list)
print(arr[1:3])


ar = [1, 2, 3]
n = 5
ar = [1] * n
print(arr)
print(len(arr))