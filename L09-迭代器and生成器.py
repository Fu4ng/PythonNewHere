# --------------------------------------#
#
# Created by Fu4ng on 2017/7/31.
#
# 博文地址:
# --------------------------------------#


###  八皇后问题

def conflict(state, nextX):
    """
    检查是否下一个皇后位置与之前的皇后是否有冲突
    有返回True
    无返回False
    :param state:之前几个皇后的X坐标
    :param nextX: 下一个皇后的X坐标
    :return:
    """
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后的位置和正在考虑的前一个皇后的水平距离为0（列相同）
        # 或者等于垂直距离（对角线判断，nextY-i就是垂直距离）
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    """
    解法生成器
    num是几排几列，默认是8，因为八皇后嘛
    :param state: 之前皇后的位置
    :return: 皇后X坐标
    """
    for pos in range(num):
        if not conflict(state, pos):  # 无冲突
            if len(state) == num - 1:  # 当len(state)==7 时，说明资讯要再生成一个位置就好了。
                yield (pos,)
            else:
                #使用for是因为，queens产生的解法不止一种，需要甄别，比如，第一排的摆法就有4种
                for result in queens(num, state + (pos,)):
                    # 递归，第一次的state是空的，然后确定了第一排的皇后
                    #第二次，state中多了第一排皇后的位置，然后再把现在的state传下去，为第二排皇后的位置做参数
                    yield (pos,) + result


def prettyprint(solution):
    """
    输出棋盘摆法
    :param solution:
    :return:
    """
    def line(pos, length=len(solution)):
        return "." * (pos) + ' X' + '.' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


import random
prettyprint(random.choice(list(queens(8))))
