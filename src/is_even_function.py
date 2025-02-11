def is_even(value:int) -> bool:
    if not isinstance(value, int):
        raise ValueError('Value must be integer')
    
    if value%2==0:
        return True
        
    return False