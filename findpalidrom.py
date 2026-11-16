

def checkpalindrom(stng:str):
    cleaned=''
    for chr in stng:
        if chr.isalnum():
            cleaned+=chr
    cleaned=cleaned.strip().lower()
    left=0
    right=len(cleaned)-1
    palindrom=True
    while left <right:
        if cleaned[left] != cleaned[right]:
            palindrom=False
            break
        else:
            left+=1
            right-=1

    return palindrom




print(checkpalindrom("A man, a plan, a canal: Panama"))
print(checkpalindrom("race a car"))
print(checkpalindrom("madam"))