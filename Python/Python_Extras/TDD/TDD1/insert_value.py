def insert_val_at(index, my_list, value):
    if index < 0 or index > len(my_list):
        return False
    else:
        my_list.append(value)
        count = len(my_list) -1
        while count>index:
            my_list[count], my_list[count-1] = my_list[count-1], my_list[count]
            count = count - 1
        return my_list
