def is_divisible_by_last_two_digits(num: int):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by both last two digits, False otherwise.
    """
    
    
    a,b = str(num)[-2:]
    a, b = int(a), int(b)
    return a!=0 and b!=0 and num % a == 0 and num % b == 0
    

# #Another Method:
# def is_divisible_by_last_two_digits(num: int):
#     u=num%10
#     t=(num%100)//10
    
#     if u==0 or t==0:
#         return False
#     elif num%u==0 and num%t==0:
#         return True
#     else:
#         return False

# Check Divisibility by Last Two Digits
# Write a function that checks whether a given number is divisible by both of its last two digits.

# Return False if any of the last two digits is zero.



# Input: A positive integer num with at least two digits.
# Output: True if the number is divisible by both of its last two digits, otherwise False.
# Examples

# 1236 -> True, 1236 is divisible by both 3 and 6.
# 345 -> False, 345 is divisible by 5 but not divisible by 4.
# 748 -> False, 748 is divisible by 4 but not divisble by 8.
# 740 -> False, the last digit is 0.

