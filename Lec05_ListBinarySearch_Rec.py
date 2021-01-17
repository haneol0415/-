def RecBinSearch(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return RecBinSearch(L, x, l, mid-1)
    else:
        return RecBinSearch(L, x, mid+1, u)
