i=1 #변수 i 선언
def truth_number(i): #함수 선언
    while i > 0 : #반복문 조건
        num1, num2 = map(int, input().split()) #두 수 입력받기
        if num1-num2 > 0:
            print('Yes')
        elif num1==0 and num2==0: #탈출 조건
            break
        else:
            print('No')

truth_number(i) #함수 호출