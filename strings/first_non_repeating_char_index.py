from collections import OrderedDict
def first_non_repeating_char_index(s: str):
    od = OrderedDict()
    for i in s:
        if i in od:
            od[i] = od[i] + 1
        else:
            od[i] = 1
    for key in od:
        if od[key] == 1:
              value_to_chk = key
              break
    
    if len(s) == 0:
        return -1
    else:
        try:
            return s.index(value_to_chk)
        except:
            return -1

res = first_non_repeating_char_index("longer")
print(res)


res = first_non_repeating_char_index("lovleyo")

print(res)


        
res = first_non_repeating_char_index("")

print(res)


res = first_non_repeating_char_index("mamama")

print(res)
