year = int(input()) #년도 입력받기
def leap_year(year): #윤년 판별 기능 함수 정의
    if year%4 == 0 and year%100 !=0 or year%400 ==0: #윤년을 위한 조건문
        print(1)
    else:
        print(0)

leap_year(year)