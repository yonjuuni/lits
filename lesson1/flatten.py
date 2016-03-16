input_list = [1, [2, 3], 4, [[6, 7]]]
    
def flatten(lst):
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])

print(flatten(input_list))
