# 猜数字是几的小游戏
guess = 1
i = 1
while guess != 5 and i <= 3:
    temp = input("请输入我心中所想的数字：")
    guess = int(temp)
    if guess == 5:
        print("你猜对了," + "你是我心里的蛔虫")
    else:
        if guess > 5:
            print("你猜太大了")
        if guess < 5:
            print("你猜太小了")
        i = i + 1
        if i == 4:
            print("你没机会了")
        else:
            print("重新猜一下吧")
