def insertSort(arr):
    for this_idx in range(1, len(arr)):
        sorted = False
        while sorted is False and this_idx >= 1:
            if arr[this_idx] < arr[this_idx - 1]:
                arr[this_idx-1], arr[this_idx] = arr[this_idx], arr[this_idx-1]
                this_idx = this_idx - 1
            else:
                sorted = True
    return arr

test = insertSort([1, 2, 5, 4, 3, 8])
print test
