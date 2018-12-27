import rand_alpha
import rand_math

game = input('请选择游戏：\n1.数字游戏\n2.字母游戏\n请输入1或2进入游戏\n')
if game == '1':
    game_r = rand_math
    game_r.guess_number(0, 0)
elif game == '2':
    game_r = rand_alpha.Game_Alpha()
    game_r.Bpr()
else:
    print('输入错误')
