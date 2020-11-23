def calc(num, item): # 계산하는 함수
    if item == '@':
        return (num * 3)
    if item == '%':
        return (num + 5)
    if item == '#':
        return (num - 7)

A = int(input()) # 테스트의 횟수 입력받기
for i in range(A):
    B = input().split() # 리스트 입력 반복
    num = float(B.pop(0))
    for j in B:
        num = calc(num, j) # 계산 함수 호출 후 num에 대입

print('%0.2f' % num) # 소수점 둘째자리까지 출력