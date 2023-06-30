from typing import List
 
def shift_array(arr: List[int], n: int) -> List[int]:
    if n == 0:
        return arr
    elif n > 0:
        n = n % len(arr)
        return arr[-n:] + arr[:-n]
    else:
        n = abs(n) % len(arr)
        return arr[n:] + arr[:n]

res = shift_array([1, 2, 3, 4, 5], 2)
print(res)


arr = [0, 1, 2, 3, 4, 5]
n = 7
res = shift_array(arr, n)
print(res)
