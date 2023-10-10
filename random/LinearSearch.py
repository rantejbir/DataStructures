def locate_position(list_num,num):
    pointer=0
    while True:
        if list_num[pointer]== num:
            return pointer
        pointer+=1
        if pointer==len(list_num):
            return -1

 
array1 = [13,14,13,12,1,4,6,3,2,1,5]
num_to_be_found=1

result = locate_position(array1,num_to_be_found)
if result ==-1:
    print("number not found")
else:
    print("number found at: ",result)