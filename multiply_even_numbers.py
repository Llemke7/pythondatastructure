def multiply_even_numbers(nums):
    result = 1
    has_even = False
    for num in nums:
        if nums % 2 == 0:
            result *= num
            has_even = True
        if has_even:
            return result
        else:
            return 1
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """