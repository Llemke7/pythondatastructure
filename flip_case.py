def flip_case(phrase, to_swap):
         result = ''
         for char in phrase:
             if char == to_swap:
                 result += char.swapcase()
                 return result

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """