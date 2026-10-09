#merge sorted araay and find the median of the merged array without function 

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6]

merged = []
i, j = 0, 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

merged.extend(arr1[i:])
merged.extend(arr2[j:])


n = len(merged)
if n % 2 == 0:
    median = (merged[n//2 - 1] + merged[n//2]) / 2
else:
    median = merged[n//2]

print("Merged Array:", merged)
print("Median:", median)
