def maximum(L):
    if not L:  # L이 비어 있는 경우
        return None
    elif len(L) == 1:  # L에 한 개의 항목이 있는 경우
        return L[0]
    else:  # L에 둘 이상의 항목이 있는 경우
        mid = len(L) // 2
        L1 = L[:mid]  # 앞쪽 절반 L1
        L2 = L[mid:]  # 뒤쪽 절반 L2
        return max(maximum(L1), maximum(L2))  # L1과 L2의 최댓값 중 큰 값을 반환
    
print(maximum([17, 25, 11, 9, 20, 3, 19, 17, 10, 8]))
print(maximum([17, 2, 25, 12, 28, 11, 10, 10, 30, 15, 16, 10]))
