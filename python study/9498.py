test_point = int(input()) #테스트 점수 입력받기
def test_class(test_point): #테스트 점수의 등급을 보여주는 함수
    if 90<=test_point<=100 and test_point<101:
        test_point = 'A'
        return test_point
    elif 80<=test_point<=89:
        test_point = 'B'
        return test_point
    elif 70<=test_point<=79:
        test_point = 'C'
        return test_point
    elif 60<=test_point<=69:
        test_point = 'D'
        return test_point
    else:
        test_point = 'F'
        return test_point

print(test_class(test_point)) #함수 호출