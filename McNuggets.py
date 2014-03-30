def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    
    6a+9b+20c=n
    """
    if n%20 == 0 or n%9 == 0 or n%6 == 0:
        return True 
    elif n < 6:
        return False     
    elif n/20 >= 1:
        return McNuggets(n%20)
    
    elif n%20 >= 9:
        return McNuggets(n%9)

    elif n%20%9 >= 6:
        return McNuggets(n%6)
    else:
        return False

        
        
        
