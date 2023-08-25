#Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

ar = ["bob", "alice", "jane", "doe"]
ar.sort()
print(ar)

#Sort in order of length of string 
ar.sort(key=lambda x: len(x))
print(ar) 