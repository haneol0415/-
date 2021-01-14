def solution(L, x):
    lower = 0
    upper = len(L)-1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        if L[mid]==x:
            return mid
        elif L[mid] < x:
            lower = mid + 1
        else:
            upper = mid - 1
    
    return -1
