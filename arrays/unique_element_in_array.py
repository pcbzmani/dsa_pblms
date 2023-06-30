from typing import List

def find_unique_customer_id(customerIDs: List[int]) -> int:
    x = 0
    temp_list = []
    for i in range(0,len(customerIDs)):
        if i == 0:
            temp_list.append(customerIDs[i])
        elif customerIDs[i] in temp_list:
            temp_list.remove(customerIDs[i])
        else:
            temp_list.append(customerIDs[i])
    
    for i in temp_list:
        return int(i)

res = find_unique_customer_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8])
print(res)

res = find_unique_customer_id([10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70])
print(res)

## Also we can use XOR operation ^=.. but in the second use case one num is missing 80, so this approcah is used.
