basic = 12100
sec = int(input('음성 통화: '))
mb = int(input('데이터 사용량: '))

call = int (sec * 1.98)
data = mb * 55
total = basic + call + data

print('이용 요금: ', format(call,','))
print('데이터 사용: ', format(data, ','))
print('총 이용 요금', format (total, ','))
