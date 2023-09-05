def max(message, mes2, *numbers, **named_numbers):
    """Return the max number given in arguments

    Args:
        message (_type_): welcoming message
        mes2 (_type_): _description_
        *numbers: an infinite number of numbers given in argument

    Returns:
        max: the max number
        
    >>> max(1, 2, 3)
    '3'
    """
    max = 0
    for number in numbers:
        if max < number:
            max = number
    return str(max)

help(max)