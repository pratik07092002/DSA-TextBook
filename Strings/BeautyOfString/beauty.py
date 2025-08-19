
# Day 22 , 19-08-2025
def beautySum(s: str) -> int:
    n = len(s)
    total = 0
    
    # iterate over all substrings
    for i in range(n):
        freq = [0] * 26  # frequency array for characters
        for j in range(i, n):
            freq[ord(s[j]) - ord('a')] += 1
            
            # filter non-zero frequencies
            non_zero = [f for f in freq if f > 0]
            
            total += max(non_zero) - min(non_zero)
    
    return total
