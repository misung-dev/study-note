def maximum(L):
    if not L:  # L이 비어 있는 경우
        return None
    elif len(L) == 1:  # L에 한 개의 항목이 있는 경우
        return L[0]
    else:  # L에 둘 이상의 항목이 있는 경우
        sub_max = maximum(L[1:])  # L[1:]의 최댓값을 재귀적으로 구함
        return max(sub_max, L[0])  # L[0]과 sub_max 중 큰 값을 반환

print(maximum([17, 25, 11, 9, 20, 3, 19, 17, 10, 8]))
print(maximum([17, 2, 25, 12, 28, 11, 10, 10, 30, 15, 16, 10]))
