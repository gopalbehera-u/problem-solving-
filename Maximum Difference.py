def maxdiff(num):
    min_so_far = num[0]
    max_diff = 0

    for i in num[1:]:
        diff = i - min_so_far

        if diff > max_diff:
            max_diff = diff

        if i < min_so_far:
            min_so_far = i

    return max_diff


print(maxdiff([2, 3, 10, 6, 4, 8, 1]))