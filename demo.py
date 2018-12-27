import rand_alpha
import rand_math

game = input('请选择游戏：\n1.数字游戏\n2.字母游戏\n请输入1或2进入游戏\n')
if game == '1':
    rand_math.guess_number()
elif game == '2':
    rand_alpha.Game_Alpha.Dpr(0)
else:
    print('输入错误')
