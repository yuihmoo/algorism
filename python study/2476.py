N = int(input())
dice_price = []

for i in range(0, N):
    dice_1, dice_2, dice_3 = map(int, input().split())
    dice_list = [dice_1, dice_2, dice_3]
    if dice_1-dice_2==0 and dice_2-dice_3==0:
        dice_price.append(10000+(dice_1*1000))
    elif dice_1-dice_2==0 or dice_1-dice_3==0:
        dice_price.append(1000+dice_1*100)
    elif dice_2-dice_3==0: 
        dice_price.append(1000+dice_2*100)
    else:
        dice_price.append(max(dice_list)*100)

print(max(dice_price))