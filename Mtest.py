def Mcompare(A,B):
    notfound = False
    for i in A:
        for j in B:
            if j > i:
                notfound = True
                break
            elif j == i:
                break
        if notfound:
            break
    if notfound:
        print("A not contained in B")
    else:
        print("A contained in B")
    notfound = False
    for i in B:
        for j in A:
            if j > i:
                notfound = True
                break
            elif j == i:
                break
        if notfound:
            break
    if notfound:
        print("B not contained in A")
    else:
        print("B contained in A")

A = [1,2,3,4,5]    
B = [1,2,3,4,5,6,7,8]

Mcompare(A,B)