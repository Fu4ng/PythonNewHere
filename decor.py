# --------------------------------------#
#
# Created by Fu4ng on 2017/7/26.
#
# 博文地址:
# --------------------------------------#


# 装饰器


def outer(func):
    def inner():
        print('before!')
        func()
        print('after!')

    return inner


@outer
def fun():
    print('called!')


fun()
