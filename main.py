def is_palindrome(text):
    text = ''.join([c for c in text if c.isalpha()]).lower()
    if text == text[::-1]:
        return True
    else:
        return False

for i in range(10):
    print(is_palindrome(input()))
