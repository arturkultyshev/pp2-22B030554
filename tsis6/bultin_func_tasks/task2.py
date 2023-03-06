def low_up(string):
    low_case = 0
    upper_case = 0

    for i in string:
        if i.islower():
            low_case += 1
        elif i.isupper():
            upper_case += 1
    return low_case, upper_case


string = 'hello'
illig_val = '!@#$%^&*()_+=-/;:?'
if isinstance(string, str):
    for i in string:
        if i.isdigit() or i in illig_val:
            raise ValueError('Digit or spec_symb in str')
else:
    raise ValueError('Not str')
ob = low_up(string)
print(f'low_case: {ob[0]}, upper_case: {ob[1]}')
