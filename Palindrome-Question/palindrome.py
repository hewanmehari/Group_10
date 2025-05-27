def is_palindrome(s):
    clean_s = ''.join(c for c in s.lower() if c.isalnum())
    return clean_s == clean_s[::-1]
print(is_palindrome("local 9 "))  
print(is_palindrome("hanna@#h"))  