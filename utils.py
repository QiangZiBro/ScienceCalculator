# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：task2-calc -> utils
@IDE    ：PyCharm
@Author ：QiangZiBro
@Date   ：2020/3/20 6:03 下午
@Desc   ：
=================================================='''


def wrapper(b):
    """在一个四则运算中，比如a+b，其中b是从其他运算（log，tan计算而来），如果b是负数，
    整个表达式会变成a+-b，造成解析难度，为了化为一般情况，将小于0的数b变为(0-b）
    :param b:
    :return:
    """
    return "(0" + b + ")"


def wrapper_inverse(b):
    if b[0] == "(" and b[-1] == ")":
        return "1÷" + b
    else:
        return "1÷(" + b + ")"


class History(list):
    # TODO
    def __init__(self, parent=None):
        super(History, self).__init__()
        self.parent = parent
        self.pos = None

    def append(self, object) -> None:
        super().append(object)
        self.pos = len(self)-1

    def next(self):
        if self.pos < len(self)-1:
            self.pos += 1
            self.parent.lineEdit.setText(self[self.pos])

    def last(self):
        if self.pos > 0:
            self.pos -= 1
            self.parent.lineEdit.setText(self[self.pos])


if __name__ == "__main__":
    h = History()
    h.append(33)
    h.append(44)
    h.append(42)
    print(h.last())
    print(h.last())
    print(h.last())
