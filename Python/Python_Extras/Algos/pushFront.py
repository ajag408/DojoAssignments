def push_front(arr, val):
    arr.append(val)
    for count in range(1, len(arr)):
        arr[len(arr)-count], arr[len(arr)-count-1] = arr[len(arr)-count-1], arr[len(arr)-count]
    return arr

test = push_front([1,2,3], 4)
print test
