def selectSort(arr):
    count = 0
    while count < len(arr):
        mini = count
        for idx in range(count, len(arr)):
            if arr[idx] < arr[mini]:
                mini = idx
        arr[count], arr[mini] = arr[mini], arr[count]
        count = count + 1
    return arr

sorted = selectSort([1,4,2,3])
print sorted
