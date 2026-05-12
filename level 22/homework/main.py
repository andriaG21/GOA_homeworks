def str_to_int(value):

    value = value.strip()

    if value == '':
        return 'invalid input'
    
    if value.startswith('-'):
        if value[1:].isdigit():
            return int(value)
        else:
            return 'invalid input'

    if value.isdigit():
        return int(value)   
    else:
        return 'invalid input'
