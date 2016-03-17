input_string = ''
while not input_string.startswith('[') or not input_string.endswith(']'):
    input_string = input('Enter a list: ')

input_list = eval(input_string)
    
def flatten(lst):
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])

print('Result:', flatten(input_list))
