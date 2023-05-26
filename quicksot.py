def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot ]
        return quicksort(less) + [pivot] + quicksort(greater)
    
arr = [2,9,4,6,7,8,3]

print(quicksort(arr))