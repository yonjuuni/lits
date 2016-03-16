input_string = ''
while '(' not in input_string and ')' not in input_string:
    input_string = input('Enter a string with parentheses: ')

opening = input_string.count('(')
closing = input_string.count(')')

if opening == closing:
    print('The number of parentheses is good to go.')
elif opening > closing:
    print('You are missing {} closing parentheses'.format(opening - closing))
else:
    print('You are missing {} opening parentheses'.format(closing - opening))
