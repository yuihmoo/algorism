dice_1, dice_2, dice_3 = map(int, input().split()) #주사위 3개 입력받기
dice_list = [dice_1, dice_2, dice_3] #리스트 선언

def dice_price(): #주사위 상금 함수
    if dice_1-dice_2==0 and dice_2-dice_3==0:
        print(10000+(dice_1*1000))
    elif dice_1-dice_2==0 or dice_1-dice_3==0:
        print(1000+dice_1*100)
    elif dice_2-dice_3==0: 
        print(1000+dice_2*100)
    else:
        print(max(dice_list)*100)

dice_price() #함수 호출