test_range = int(input()) #테스트 횟수 입력받기
for i in range(test_range): #테스트 횟수만큼 반복문
    result = "" #반복문 값 초기화
    X, Y = input().split() 
    X = int(X)
    for j in Y: # 같은 문자 횟수만큼 반복
        for k in range(X): 
            result = result + j
    print(result)