def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False  
print(check_palindrome("kajak"))
print(check_palindrome("potop"))
print(check_palindrome("kot"))