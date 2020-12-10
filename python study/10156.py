K, N, M = map(int, input().split())
money = M-(K*N) #부족해서 빌려야하는 돈
if M-(K*N) < 0 and 1<=K and N<=1000 and 1<=M<=100000:
    print(abs(money)) #현물이므로 절대값 출력
else :
    print(0)