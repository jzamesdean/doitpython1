# 1부터 n까지 정수의 합구하기 1(while문)

print('1부터 n까지 정수의 합을 구합니다')
n = int(input('n 값을 입력하세요. :'))

sum = 0
i = 1

while i<=n : #i가 n보다 작거나 같은동안 반복
    sum += i #sum에 i를 더함
    i += 1   #i에 1을 더함
    
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')