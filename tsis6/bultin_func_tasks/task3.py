def palidrom(string):
    reverse = ''.join(reversed(string))

    if string == reverse:
        return True
    return False


string = 'abba'
if isinstance(string, str):
    if palidrom(string):
        print('String is palidrom')
    else:
        print('String is not palidrom')
else:
    raise ValueError('Input is not a string')
