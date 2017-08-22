def bubbleSort(arr):
    sorted = False
    while sorted is False:
        this_sort_count = 0
        for idx in range(0, len(arr)-1):
            if arr[idx] > arr[idx+1]:
                this_sort_count = this_sort_count + 1
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        if this_sort_count == 0:
            sorted = True
    return arr

sorted_arr = bubbleSort([1,3,2,4,8,6,5,7])
print sorted_arr
