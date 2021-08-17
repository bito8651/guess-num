import random

r = random.randint(1, 100) # 產生範圍1~100的隨機整數
while True:
    num = input('請猜1~100的數字： ')
    num = int(num)
    if num == r:
        print('你猜對了！')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')