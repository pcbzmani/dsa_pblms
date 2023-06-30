def detect_duplicate_products(product_ids: list[int]) -> bool:
    if len(product_ids) == len(set(product_ids)):
        return False
    else:
        return True


product_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert detect_duplicate_products(product_ids) == False

product_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
assert detect_duplicate_products(product_ids) == True
