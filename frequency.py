def frequency(lst, search_term):
    freq = {}
        for item in search_term:
            if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
        return freq



    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """