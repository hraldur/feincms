def c_any(iterable):
    for element in iterable:
        if element:
            return True
    return False
