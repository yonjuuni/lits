input_string = ''
while (not input_string.startswith('[') or 
       not input_string.endswith(']') or 
       'for' in input_string):
    input_string = input('Enter a list: ')

input_list = eval(input_string)
# input_list = [1, [2, 3], 4, [[6, 7]]]

temp = str(input_list).split()
res = []
for i in temp:
    element = i.strip(',[]')
    if element:
        res.append(eval(element))

print(res)
