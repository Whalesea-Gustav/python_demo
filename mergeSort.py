def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]

    if len(lft)>1 : lft = mergesort(lft)
    if len(rgt)>1 : rgt = mergesort(rgt)

    print("this is left part :", lft, "and this is right part:", rgt, sep=" ")

    res = []

    while (lft and rgt):
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())


    res.reverse()
    print("this is rest", res, sep=" ")
    return (lft or rgt) + res

print(mergesort([1, 10, 9, 8, 11, 0]))