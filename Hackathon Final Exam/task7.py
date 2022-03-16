arr = [5, 1, 8, 92, -1, 30]
temp = 0

print("Original list:")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print()
print("Sorted list:")
for i in range(0, len(arr)):
    print(arr[i], end=" ");