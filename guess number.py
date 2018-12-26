import random

source = 0
while 1:
    num = input('请输入1,2,3中的一个数字,输入-1结束：')

    rand_num = random.randrange(1,4)
    num = int(num)
    rand_num = int(rand_num)
    if num == -1:
        break

    if num > rand_num:
        print('猜大了')
    elif num == rand_num:
        print('恭喜你，猜对了，加一分')
        source += 1
    else:
        print('猜小了')
print('你的最后得分为{}分'.format(source))