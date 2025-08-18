
# DAY 21 , 18-08-2025
def longestPalindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""
    
    start, end = 0, 0
    
    def expandFromCenter(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # length = right - left - 1 (because when loop ends, left & right moved one extra step)
        return right - left - 1

    for i in range(len(s)):
        len1 = expandFromCenter(i, i)      # Odd length
        len2 = expandFromCenter(i, i + 1)  # Even length
        length = max(len1, len2)

        if length > (end - start):
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end + 1]

print(longestPalindrome("babad"))