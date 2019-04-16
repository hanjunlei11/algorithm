#为了不断优化推荐效果，今日头条每天要存储和处理海量数据。
# 假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，对于一类文章，每个用户都有不同的喜好值
# 我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。
# 因为一些特殊的原因，不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。

#输入输出：
#输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度
# 第3行为一个正整数q代表查询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。
# 数据范围n <= 300000,q<=300000 k是整型
#输出：一共q行，每行一个整数代表喜好值为k的用户的个数\

#逻辑没问题，牛客网超时，应该可以用数据结构优化一下

import sys

def find(num,search):
    temp = num[search[0]-1:search[1]]
    res = str(temp.count(search[2]))
    return res


if __name__=="__main__":
    N = int(input())
    num = list(map(int, input().split()))
    Q = int(input().strip())
    for i in range(Q):
        temp = list(map(int, input().split()))
        res = find(num,temp)
        print(res)
