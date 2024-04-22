def demo_false_setattr():
    # Create an object with a boolean attribute
    obj = {}
    setattr(obj, 'is_done', False)
    
    # Set the value of is_done to True
    setattr(obj, 'is_done', True)
    
    # Print the value of is_done
    print(getattr(obj, 'is_done'))