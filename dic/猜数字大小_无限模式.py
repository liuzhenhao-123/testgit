# 猜数字是几的小游戏
while 1:
    temp = input("请输入我心中所想的数字：")
    guess = int(temp)
    if guess == 5:
        print("你猜对了," + "你是我心里的蛔虫")
    else:
        print("ERROR，没有奖励")
        if guess > 5:
            print("你猜太大了")
        if guess < 5:
            print("你猜太小了")