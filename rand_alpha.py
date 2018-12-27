class Game_Alpha():


    def Apr(self):
        # 打印字母A
        # 控制行
        for i in range(5):
            # 判断开始输入的位置
            for k in range(5 - i):
                print(' ', end='')
            # 控制列
            for j in range(i + 1):
                # 控制行首和行尾还有列首和列尾打印星星
                if i == 1 or i == 2 or j == 0 or j == i:
                    print('*', end=' ')
                # 控制其余地方打印空格
                else:
                    print(' ', end=' ')
            # 换行
            print()


    def Bpr(self):
        # 打印字母B
        for i in range(3):
            for j in range(3):
                if i == 0 or i == 3 or j == 0:
                    if j < 2:
                        print('*', end=' ')
                elif j == 2:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
        for i in range(4):
            for j in range(3):
                if i == 0 or i == 3 or j == 0:
                    if j < 2:
                        print('*', end=' ')
                elif j == 2:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Cpr(self):
        # 打印字母C
        for i in range(4):
            for j in range(3):
                if i == 2 or i == 1:
                    if j == 0:
                        print('*', end=' ')
                elif (i == 0 or i == 3) and j > 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Dpr(self):
        # 打印字母D
        for i in range(4):
            for j in range(3):
                if i == 0 or i == 3 or j == 0:
                    if j < 2:
                        print('*', end=' ')
                elif j == 2:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Epr(self):
        # 打印字母E
        for i in range(5):
            for j in range(3):
                if i in [0, 2, 4] or j == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Fpr(self):
        # 打印字母F
        for i in range(5):
            for j in range(3):
                if i in [0, 2] or j == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Gpr(self):
        # 打印字母G
        for i in range(4):
            for j in range(4):
                if i in [0, 3] and j in [1, 2, 3]:
                    print('*', end=' ')
                elif i in [1, 2] and j == 0:
                    print('*', end=' ')
                elif i == 2 and j in [2, 3]:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Hpr(self):
        # 打印字母H
        for i in range(5):
            for j in range(4):
                if j in [0, 3]:
                    print('*', end=' ')
                elif i == 2:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Ipr(self):
        # 打印字母I
        for i in range(5):
            for j in range(3):
                if j == 1:
                    print('*', end=' ')
                elif i in [0, 4]:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Jpr(self):
        # 打印字母J
        for i in range(5):
            for j in range(4):
                if j == 2 and i != 4:
                    print('*', end=' ')
                elif i == 0:
                    print('*', end=' ')
                elif i == 4 and j == 1:
                    print('*', end=' ')
                elif i == 3 and j == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Kpr(self):
        # 打印字母K
        for i in range(2):
            for j in range(i, 3):
                if j in [i, 2]:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
            print()
        for i in range(3):
            for j in range(i+1):
                if j in [0, i]:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
            print()


    def Lpr(self):
        # 打印字母L
        for i in range(5):
            for j in range(3):
                if i == 4 or j == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    def Mpr(self):
        # 打印字母M
        for i in range(5):
            # 判断开始输入的位置
            for k in range(5 - i):
                print(' ', end='')
            # 控制列
            for j in range(i + 1):
                # 控制行首和行尾还有列首和列尾打印星星
                if i == 1 or j == 0 or j == i:
                    print('*', end=' ')
                # 控制其余地方打印空格
                else:
                    print(' ', end=' ')
            for k in range(4 - i):
                print(' ', end=' ')
            # 控制列
            for j in range(i + 1):
                # 控制行首和行尾还有列首和列尾打印星星
                if i == 1 or j == 0 or j == i:
                    print('*', end=' ')
                # 控制其余地方打印空格
                else:
                    print(' ', end=' ')
            # 换行
            print()


    def Npr(self):
        # 打印字母N
        for i in range(4):
            for j in range(4):
                if j in [0, 3] or i == j:
                    print('*', end=' ')
                else:
                    print(" ", end=' ')
            print()




if __name__ == '__main__':
    pass
