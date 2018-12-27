import random, math

'''
输入一个三位数与程序随机数比较大小
1.如果大于程序随机数，则分别输出这个三位数的个位\十位\百位
2.如果等于程序随机数，则提示中奖，记100分
3.如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串长度为12，单独占一行，而且前四个是字母，后八个是数字）
'''


def one_line():
    # 定义一个空字符串用于拼接字符
    str_num = ''
    # 循环前四个随机数字(用ASCII对应的值来转换为字母)
    for i in range(4):
        # 随机小写字母的ASCII值
        num = random.randrange(97, 123)
        # 将ASCII值转换成对应的字母
        str_s = chr(num)
        # 依次拼接得到的随机字母
        str_num = str_num + str_s
    # 循环后八个随机数字
    for i in range(8):
        num = random.randrange(0, 10)
        str_num += str(num)
    return str_num


def guess_number(total, score):
    while True:
        # 输入函数
        # 输入函数输入的是字符串类型，不强制转换会报错
        num = input('请输入一个三位整数:')
        # 输入-1结束
        if int(num) == -1:
            break
        # 程序随机数
        random_num = random.randrange(100, 1000)
        # 检测输入是否为纯数字
        if num.isdigit():
            # 检测输入的数字是否为三位数
            if 100 <= int(num) <= 999:
                total += 1
            else:
                print('输入值不是三位整数！')
        else:
            print('请按规定输入！')

        # 将num强制类型转换成int
        num = int(num)

        # 打印一下程序随机数的值
        print('随机数的值为：{}'.format(random_num))

        # 判断随机数与输入值的大小
        if num > random_num:
            # 分别输出这个三位数的个位\十位\百位
            gw = num % 10
            sw = num % 100 // 10
            bw = num // 100
            print('你输入的值的个位是{0}, 十位是{1}, 百位是{2}'.format(gw, sw, bw))
        # 提示中奖，记100分
        elif num == random_num:
            score += 100
            print('恭喜你，中奖了！记100分。')
        # 将120个字符输入到文本文件中
        else:
            # 由于120个字母每行12个字符，需要10行
            for i in range(10):
                str_line = one_line()
                # 执行文件存入操作
                with open('str_num.txt', 'a') as f:
                    # 注意需要换行符号
                    f.write(str_line + '\n')
            print('str_num已保存')


# 程序入口
if __name__ == '__main__':
    global total
    global score
    # 定义一个初始值来存储次数
    total = 0
    # 定义一个初始值来存储分数
    score = 0
    guess_number(total, score)
    print('你一共玩了{}次，的最终分数为{}'.format(total, score))
