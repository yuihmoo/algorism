point_list = [] #리스트 선언
i = 0 
def point_avg(i): #평균점수 구하는 함수 선언
    for i in range(5): #반복문 시작
        point = int(input()) #점수 입력받기
        if point < 40: #조건문
            point_list.append(40) #40점으로 치환
        else:
            point_list.append(point) #리스트에 저장
    print(sum(point_list)//len(point_list)) #리스트 평균 구하기

point_avg(i) #함수 호출