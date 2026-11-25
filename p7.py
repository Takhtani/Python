arr = [34, 7, 89, 21, 56, 3, 68]
print("Array:", arr)

largest = arr[0]
smallest = arr[0]
for x in arr:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print("Largest element  :", largest)
print("Smallest element :", smallest)

# verification using built-in functions
print("Check with max() and min():", max(arr), min(arr))
