def common_customers(customers1: list[int], customers2: list[int]) -> list[int]:
    common_list = list(set(customers1) & set(customers2))
    common_list.sort()
    return common_list

customers1 = [1, 2, 3, 4, 5]
customers2 = [4, 5, 6, 7, 8]
assert common_customers(customers1, customers2) == [4, 5]

customers1 = [10, 20, 30, 40, 50]
customers2 = [50, 40, 30, 20, 10]
assert common_customers(customers1, customers2) == [10, 20, 30, 40, 50]
