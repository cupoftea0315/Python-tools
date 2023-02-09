# coding:utf-8
"""全局最长公共子序列（序列可以不连续）"""
import numpy
import datetime


def find_lcseque(s1, s2):
    # 生成全为0的矩阵，为方便后续计算，边长均比字符串长度多一列
    m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    # 生成左上角开始的矩阵d，用来记录转移方向
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for y in range(len(s1)):
        for x in range(len(s2)):
            if s1[y] == s2[x]:  # 字符匹配成功，则该位置的值为左上方的值加1
                m[y + 1][x + 1] = m[y][x] + 1
                d[y + 1][x + 1] = 'match'
            elif m[y + 1][x] > m[y][x + 1]:  # 左值大于上值，则该位置的值为左值，并标记回溯时的方向
                m[y + 1][x + 1] = m[y + 1][x]
                d[y + 1][x + 1] = 'left'
            else:  # 上值大于左值，则该位置的值为上值，并标记回溯时的方向
                m[y + 1][x + 1] = m[y][x + 1]
                d[y + 1][x + 1] = 'up'
    # print(numpy.array(d))  # 打印箭头指向

    s = []
    y, x = len(s1), len(s2)
    while m[y][x]:  # 不为None时持续循环
        c = d[y][x]
        if c == 'match':  # 匹配成功，插入该字符，并向左上角找下一个
            s.append(s1[y - 1])
            y -= 1
            x -= 1
        if c == 'left':  # 根据标记，向左找下一个
            x -= 1
        if c == 'up':  # 根据标记，向上找下一个
            y -= 1
    s.reverse()
    return ''.join(s)


if __name__ == '__main__':
    s1 = "ATCTT"
    s2 = "CTTA"

    start_time = datetime.datetime.now()
    result = find_lcseque(s1, s2)
    end_time = datetime.datetime.now()
    print("The global longest common subsequence is: %s" % result)
    print("The length of glcs is: %d" % len(result))
    print("Running time:", (end_time - start_time))
