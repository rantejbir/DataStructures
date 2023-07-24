# sort function to arrange elements in ascending order
def sort_func(list_sort):
    for itm in range(len(list_sort)):
        for i in range(0, len(list_sort) - itm - 1):
            if list_sort[i] > list_sort[i + 1]:
                temp = list_sort[i]
                list_sort[i] = list_sort[i + 1]
                list_sort[i + 1] = temp
    return list_sort


# search function to search the element from the list
def binary_search(list_arr, num):
    list_arr = sort_func(list_arr)
    low = 0
    high = len(list_arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if list_arr[mid] < num:
            low = mid + 1
        elif list_arr[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 4, 7, 2, 6, 2, 3, 1, 4]
# test case 1
result = binary_search(arr, 4)
if result == -1:
    print("number not found")
else:
    print("number found at: ", result)

# test case 2
result = binary_search(arr, 8)
if result == -1:
    print("number not found")
else:
    print("number found at: ", result)