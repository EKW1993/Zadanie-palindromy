def check_palindrome(word):
    """
        Return whether string is a palindrome or not
        Parameters:
        word (str): A string that is to be checked for palindrome.
        Returns:
        True: If the given string is a palindrome.
        False: If the given string is not a palindrome.
        Return type: bool
    """
    if word == word[::-1]:
        return True
    else:
        return False  
print(check_palindrome("kajak"))
print(check_palindrome("potop"))
print(check_palindrome("kot"))