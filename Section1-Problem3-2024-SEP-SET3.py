def swap_last_chars_of_values(d: dict, k1, k2):
    """Swap the last chars of the values of given keys in the dict.

    Args:
        d (dict): The dictionary with string values.
        k1: The first key.
        k2: The second key.

    Returns:
        None - modifies the dictionary in-place.
    """
    
    
    a, b = d[k1], d[k2]  # to simplify the notation
    d[k1], d[k2] = a[:-1] + b[-1], b[:-1] + a[-1]

# #Another Method
# def swap_last_chars_of_values(d: dict, k1, k2):
#     val1=d[k1]
#     val2=d[k2]
    
#     last1=val1[-1]
#     last2=val2[-1]
    
#     val1=val1[0:-1:]+last2
#     val2=val2[0:-1:]+last1
    
#     d[k1]=val1
#     d[k2]=val2


# Swap the Last Chars in Dictionary Values
# Write a function that swaps the last characters of the values corresponding to two specified keys in a dictionary.

# Assume that the values in the dictionary are strings.

# Input:
# A dictionary d where the values are strings.
# Two keys k1 and k2.
# Output:
# Modify the dictionary in-place by swapping the last characters of the values of the given keys.
# The function returns None as it modifies the dictionary directly.
# Assume the values for both keys k1 and k2 are non-empty strings and the dictionary contains the keys k1 and k2.

# Examples

# Example 1

# >>> d = {"first": "apple", "second": "mango", "third":"banana"}
# >>> swap_last_chars_of_values(d, "first", "second")
# >>> d
# {'first': 'applo', 'second': 'mange', "third": "banana"}
# Example 2

# >>> d = {"key1": "hello", "key2": "world"}
# >>> swap_last_chars_of_values(d, "key1", "key2")
# >>> d
{'key1': 'helld', 'key2': 'worlo'}
