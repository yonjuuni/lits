input_string = ''
while ('(' not in input_string and ')' not in input_string) and \
      ('[' not in input_string and ']' not in input_string) and \
      ('{' not in input_string and '}' not in input_string):
    input_string = input('Enter a string with () and/or {} and/or []: ')

output = []
for i in input_string:
    if i in '(){}[]':
        output.append(i)
output = ''.join(output)

res = False

if len(output) % 2 == 0:
    mid = len(output) // 2
    start = output[:mid]
    end = output.replace(')', '(').\
                 replace(']', '[').\
                 replace('}', '{')[mid:]
    if start == end[::-1]:
        if (')' not in start and ')' not in end and
            ']' not in start and ']' not in end and
            '}' not in start and '}' not in end):
            res = True

if res:
    print("There's a balance.")
else:
    print("There's no balance.")
