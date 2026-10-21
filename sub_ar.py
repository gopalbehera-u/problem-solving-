def maxsubarr(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        current_sum=max(nums[i],current_sum+nums[i])
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum



print(maxsubarr( [-2, 3, -1, 5]))