def findanagran(s,t):
    freq_s={}
    freq_t={}
    if len(s)!=len(t):
        return False

    for i in s :
        if i not in freq_s:
            freq_s[i]=1
        else :
            freq_s[i]+=1
    for j in t :
        if j not in freq_t:
            freq_t[j]=1
        else:
            freq_t[j]+=1
    return freq_t==freq_s


print(findanagran("aabb", "bbaa"))
print(findanagran("aab", "abb"))

    