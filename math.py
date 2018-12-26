import math

# ceil() 向上取整
print(math.ceil(5.01))
print(math.ceil(5.9))

print('=' * 20)
# floor() 向下取整
print(math.floor(5.01))
print(math.floor(5.9))

print('=' * 20)
# 查看系统保留关键字，不可以用来当做变量的命名
import keyword

print(keyword.kwlist)

print('=' * 20)
# round() 四舍五入操作
print(round(5.01))
print(round(5.5))
print(round(5.9))
print(round(5.01, 1))

print('=' * 20)
# sqrt() 开平方，返回浮点数
print(math.sqrt(4))

print('=' * 20)
# pow() 与幂运算差不多，计算一个数的次方，有两个参数，第一个是底数，第二个是指数
print(math.pow(4, 3))  # 4的三次方，返回浮点型
# 幂运算，返回整形
print(4 ** 3)

print('=' * 20)
# fabs() 对一个数值获取他的绝对值，返回的是浮点型
print(math.fabs(-1))
print(math.fabs(3))
print(math.fabs(0))

print('=' * 20)
# abs() 获取绝对值操作，不是math模块当中的，是Python内置函数，返回值由本身类型决定
print(abs(-1))
print(abs(-2.5))
print(abs(0))
print(abs(4))

print('=' * 20)
# fsum() math模块中的对整个序列求和，返回浮点型
print(math.fsum([1, 4, 5, 7]))

# sum() python内置函数的求和，返回值由本身类型决定
print(sum([1, 4, 5, 7]))

print('=' * 20)
# math.modf() 将一个浮点数拆分成整数部分（后）和小数部分（前）的元祖
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(3))
