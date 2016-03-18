print('The code assumes that no opening bracket can follow a closing one.\n'
      'E.g.: (((123)), [({1}, NOT ))123((\n')

input_string = ''
while ('(' not in input_string and ')' not in input_string) and \
      ('[' not in input_string and ']' not in input_string) and \
      ('{' not in input_string and '}' not in input_string):
    input_string = input('Enter a string with () and/or {} and/or []: ')

open_par = input_string.count('(')
close_par = input_string.count(')')
open_brackets = input_string.count('[')
close_brackets = input_string.count(']')
open_braces = input_string.count('{')
close_braces = input_string.count('}')

if open_par or close_par:
    if open_par == close_par:
        print('The number of (parentheses) is good to go.')
    elif open_par > close_par:
        print('You are missing {} closing parentheses: )'.format(open_par - \
                                                                 close_par))
    else:
        print('You are missing {} opening parentheses: ('.format(close_par - \
                                                                 open_par))

if open_brackets or close_brackets:
    if open_brackets == close_brackets:
        print('The number of [brackets] is good to go.')
    elif open_brackets > close_brackets:
        print('You are missing {} closing brackets: ]'.format(open_brackets - \
                                                              close_brackets))
    else:
        print('You are missing {} opening brackets: ['.format(close_brackets - \
                                                              open_brackets))

if open_braces or close_braces:
    if open_braces == close_braces:
        print('The number of {braces} is good to go.')
    elif open_braces > close_braces:
        print('You are missing {} closing braces: }}'.format(open_braces - \
                                                            close_braces))
    else:
        print('You are missing {} opening braces: {{'.format(close_braces - \
                                                            open_braces))
