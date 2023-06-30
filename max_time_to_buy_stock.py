def max_profit(prices:list[float]) -> float:
    if len(prices) > 0:
        min_ele_list = min(prices)
        index_min = prices.index(min_ele_list)
        print(f'min index {index_min}')
        new_list = prices[index_min:]
        print(f'{new_list} new list after small_ele' )
        
        low_price = new_list[0]
        max_ele = max(new_list)
        print(f'max ele {max_ele}')
        max_index = new_list.index(max_ele)
        if max_index > 0:
            return max_ele - low_price
        else:
            return 0


profit = max_profit([7, 1, 5, 3, 6, 4])
print(profit)
