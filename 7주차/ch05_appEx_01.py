depth = int(input('수심을 입력하세요. '))
temperature = 20 - (0.7 * (depth // 10))
print('수온:',temperature)
