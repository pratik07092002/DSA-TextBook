def largestOddInt(input_str) -> str:
    for i in range(len(input_str) -1, -1,-1):
        if(int(input_str[i])%2 == 1):
            return input_str[:i+1]
    return ""


print(largestOddInt("123456"))