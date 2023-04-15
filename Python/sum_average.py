count = 0
sum = 0
average = 0

print("점수 입력")

while True:
    score = int(input())

    if score == 0:
        break

    elif score < 0:
        continue

    else:
        sum += score
        count += 1


if count > 0:
    average = sum / count
        
print("합:", sum, "개수:", count, "평균: %.2f" %average)
