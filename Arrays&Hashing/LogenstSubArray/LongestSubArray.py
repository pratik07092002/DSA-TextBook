def logestSubArrayBruteForce(nums , target) :
    n = len(nums)
    max_len = 0

    for i in range(n):
        for j in range(i,n):
            current_sum = 0
            for k in range(i,j+1):
                current_sum += nums[k]

            if current_sum == target:
                max_len = max(max_len,j-i +1)
    return max_len 

def longestSubArratHashing(nums, target):
    my_map = {}
    max_len = 0
    prefix_sum = 0
    n = len(nums)
    for i in range (n):
        prefix_sum += nums[i]
        if(prefix_sum == target):
            max_len = i +1
        if(prefix_sum - target) in my_map:
            max_len = max(max_len,i - my_map[prefix_sum - target])    
        
        if(prefix_sum not in my_map):

            my_map[prefix_sum] = i
    return max_len        



nums = [10,5,2,7,1,9]
k = 15

print(longestSubArratHashing(nums,k))