def twosum(num,target):
    seen=set()

    for i in num:
        needed=target-i

        if needed in seen:
            return True
        seen.add(i)
    return False



print(twosum([2,8,9,7,90],9))