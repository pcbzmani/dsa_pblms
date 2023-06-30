def increment_large_integer(digits: list[int]) -> list[int]:
    whole_num = ''
    for i in digits:
        whole_num += str(i)
    
    incr_val = int(whole_num) + 1 
    
    emp_lis = []
    for i in str(incr_val):
        emp_lis.append(int(i))
    
    return emp_lis


res = increment_large_integer([1,2,3])
print(res) #[1,2,4]

res = increment_large_integer([9, 9, 9, 9])
print(res) #[1,0,0,0,0]

res = increment_large_integer([5, 6, 7, 8, 9])
print(res) #[5,6,7,9,0]
