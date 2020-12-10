num = int(input()) #소인수분해 할 수 입력받기
i = 2 #i의 시작
def factorization(i,num): #소인수분해 함수
    while num!=1: #1을 나눈값은 항상 자기자신이기 때문에
        if num%i == 0: #나누어서 0이 되는 값이 소인수
            num = num/i #소인수 분해 규칙
            print(i) #반복할때마다 소인수 출력
        else: #탈출조건
            i += 1
factorization(i,num) #함수 호출