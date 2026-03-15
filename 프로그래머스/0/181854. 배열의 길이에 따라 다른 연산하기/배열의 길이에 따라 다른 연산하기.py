def solution(arr, n):
    LEN = len(arr)
    if LEN % 2 == 1:
        for i in range(0, LEN, 2):
            arr[i] += n    
    else:
        for i in range(1, LEN, 2):
            arr[i] += n  
    return arr