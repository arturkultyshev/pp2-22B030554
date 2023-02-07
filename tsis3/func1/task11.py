def palidrome(string):
    new_str = string[::-1]
    if string == new_str:
        return True
    else:
        return False

print(palidrome('aba'))
print(palidrome('madam'))
print(palidrome('kick'))