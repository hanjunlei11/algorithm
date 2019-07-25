def kuaipai(L):
    end = len(L)
    if end==0:
        return []
    if end==1:
        return [L[0]]
    temp = L[0]
    left = []
    right = []
    for i in range(1,len(L)):
        if temp < L[i]:
            right.append(L[i])
        else:
            left.append(L[i])
    return kuaipai(left)+[temp]+kuaipai(right)

if __name__=="__main__":
    L=[50, 16, 30, 10, 84,38,60,  90,  2, 80, 70]
    print(kuaipai(L))