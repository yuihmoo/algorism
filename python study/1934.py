T = int(input()) #테스트 횟수 T 입력

def gcd(num1, num2): #최대공약수 함수 정의
    while num2 != 0: #조건문
            num1, num2 = num2, num1%num2
    return num1 #마지막 num1을 반환

for i in range(T): #반복문
    num1, num2 = map(int, input().split()) #최대공배수를 구할 두 수 입력
    print((num1*num2)//gcd(num1,num2)) #두수의 곱 나누기 최대공약수 = 최대공배수