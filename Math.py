import math

#Divvision in py is decimal by default
print(5 / 2)

# Double slash rounds down
print(5//2)

# By defdault negative nummbers will round down
print (3 // 2)

# Modding returns remainders
print(10 % 3)

#Math helper 
print(math.floor(3 / 2))    #Round Down
print(math.ceil(3 / 2))     #Round up
print(math.sqrt(2))     # Sqr rt
print(math.pow(2, 3))   # Power of the first number by the second

#Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite, They never overflow
print(math.pow(2, 200))

#Is this number less than infinite ?
print(math.pow(2, 200) < float("inf"))