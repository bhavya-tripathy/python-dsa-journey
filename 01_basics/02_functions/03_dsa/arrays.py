# arrays.py - Basic array operations
#By a liner array we mean a list of finite number N of similar dat elements refenced respectively by a set of n consecutive numbers.

arr = [10, 20, 30, 40, 50]

# Traversal
print("Elements in array:")
for num in arr:
    print(num)

# Search
x = 30
if x in arr:
    print(f"{x} found at index", arr.index(x))

# Insert
arr.append(60)
print("After appending 60:", arr)