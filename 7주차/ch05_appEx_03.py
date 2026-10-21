time = int(input('근무시간을 입력하세요. '))
computer1 = 24 // time
computer2 = 24 % time
count = computer1 if computer2 == 0 else computer1 + 1
print('필요한 컴퓨터:',count)
