"""125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Фраза является палиндромом, если после преобразования всех заглавных букв в строчные и
удаления всех неалфавитно-цифровых символов она читается одинаково слева направо и справа налево.
Алфавитно-цифровые символы включают буквы и цифры.

Дана строка s. Верните true, если она является палиндромом, или false в противном случае."""


def isPalindrome(s):
    s = "".join(c for c in s.lower() if c.isalnum())  # оставляем только алфавитно-цифровые символы
    left, right = 0, len(s) - 1  # Два указателя: один в начале, другой в конце
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
print(isPalindrome("A man, a plan, a canal: Panama"))

# Example 2:
# Input: s = "race a car"
# Output: false
print(isPalindrome("race a car"))

# Example 3:
# Input: s = " "
# Output: true
print(isPalindrome(" "))
