def solution(s):
    if len(s) == 0:
        return []
    res = []
    for i in range(len(s)):
        if i % 2 == 0 :
            res.append(s[i])
        else:
            res[int((i-1)/2)]+= s[i]
    if len(res[-1]) == 1:
        res[-1] += '_'
    return res