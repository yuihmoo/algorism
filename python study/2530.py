A, B, C = map(int, input().split()) # 현재 시, 분, 초에 대한 값 입력
D = int(input()) # 오븐이 수행하는데에 걸리는 시간
if 0<=A<=23 and 0<=B<=59 and 0<=C<=59 and 0<=D<=500000: # 입력값에 대한 조건
    print((A + ((B + (C + D)//60)//60)) % 24, (B + ((C + D)//60)) % 60, ((C + D) % 60)) # 시간 계산 식
else:
    False
