sum = 0
count = 1
average = 0
score = print("점수 입력")
while score != 0:
    score = int(input())
    if score >= 1:
        sum += score
        count += 1
        average = sum / count
        
print("합:", sum, "개수:", count - 1, "평균: %.2f" %average)
