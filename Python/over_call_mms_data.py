call = int(input('음성 통화 시간(초)? '))
mms = int(input('문자건수? '))
data = int(input('데이터 사용량? '))

if call <= 120 and mms <=200 and data <= 800:
    val = 37400
    
else:
    over_call = (call - 7200) * 1.98
    over_mms = (mms - 200) * 22
    over_data = (data - 800) * 55
    over_val = over_call + over_mms + over_data
    total_val = 37400 + over_val
    
print('초요금?', int(over_val))
print('총요금?', int(total_val))

