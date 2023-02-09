# coding:utf-8
"""局部最长公共子序列（序列必须连续）"""
import datetime


def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成全为0的矩阵，为方便后续计算，边长均比字符串长度多一列
    mmax = 0  # 局部最长公共子序列的长度
    p = 0  # 局部最长公共子序列对应在s1中的最后一位
    for y in range(len(s1)):
        for x in range(len(s2)):
            if s1[y] == s2[x]:  # 如果相等，则加入现有的公共子串
                m[y + 1][x + 1] = m[y][x] + 1  # 左上方值+1
                if m[y + 1][x + 1] > mmax:
                    mmax = m[y + 1][x + 1]
                    p = y + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度


if __name__ == '__main__':
    s1 = "GATAGGTCTTGTGCTCCTACACTCTAGTGGTAGTCGCCTTCCCCCAGATCAAGTACGGAAGTCTCGTGGGGGCCTGAAATAGGGCGACTTAGCGGTCAAA"
    s2 = "GGGACTTATCTCTCACGAAAGAAAAGAATATGGGCCCAATCGGTGATTGGTGAGAAATAATCGGGGGTCACAGATCATAGCATCCCCCCCTATGGCTGAA"

    start_time = datetime.datetime.now()
    result = find_lcsubstr(s1, s2)
    end_time = datetime.datetime.now()

    print("The local longest common subsequence is: %s" % result[0])
    print("The length of llcs is: %d" % result[1])
    print("Running time:", (end_time - start_time))
