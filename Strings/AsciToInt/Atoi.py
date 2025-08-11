def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = 1
    i = 0
    if s[0] in ['+', '-']:
        if s[0] == '-':
            sign = -1
        i += 1

    num_str = ""
    while i < len(s) and s[i].isdigit():
        num_str += s[i]
        i += 1

    if not num_str:  
        return 0

    num = sign * int(num_str)

    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num


print(my_atoi("   -42abc"))  
print(my_atoi("4193 with words"))  
print(my_atoi("words and 987"))   
print(my_atoi("-91283472332"))    
