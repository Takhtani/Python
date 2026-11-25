from array import array

arr = array('i', [10, 20, 30, 40, 50])

print("Elements of the array:")
for x in arr:
    print(x, end=" ")
print()

print("\nElements with index:")
for i in range(len(arr)):
    print(f"arr[{i}] = {arr[i]}")

print("\nTotal elements:", len(arr))
