N = int(input())
if 1<=N<=101 and N != 2*N:
    True
opinion_list = []
for i in range(N):
    i = int(input())
    opinion_list.append(i)

print(opinion_list)
if opinion_list.count(0) > opinion_list.count(1):
    print('Junhee is not cute!')
elif opinion_list.count(0) < opinion_list.count(1):
    print('Junhee is cute!')