def sort_func(list_sort):
    for itm in range(len(list_sort)):
        for i in range(0,len(list_sort)-itm-1):
            if list_sort[i] > list_sort[i + 1]:
                temp = list_sort[i]
                list_sort[i] = list_sort[i + 1]
                list_sort[i + 1] = temp
    return list_sort


print(sort_func([1,4,7,2,6,2,3,1,4]))