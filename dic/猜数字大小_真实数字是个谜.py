# 猜数字是几的小游戏
import random

secret = random.randint(1, 10)
number = 4
i = 1
guess = 0
while guess != secret and i <= number:
    temp = input("请输入我心中所想的数字：")
    guess = int(temp)
    if guess == secret:
        print("你猜对了," + "你是我心里的蛔虫")
        print("你一共猜了", i, "次")
    else:
        if guess > secret:
            print("你猜太大了")
        elif guess < secret:
            print("你猜太小了")
        i = i + 1
        if i == number + 1:
            print("你没机会了")
            print("你一共猜了", number, "次")
        else:
            print("重新猜一下吧")
