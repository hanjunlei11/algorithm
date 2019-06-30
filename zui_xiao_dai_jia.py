# 题目描述
# 小明目前在做一份毕业旅行的规划。打算从北京出发，分别去若干个城市，然后再回到北京，每个城市之间均乘坐高铁，且每个城市只去一次。由于经费有限，希望能够通过合理的路线安排尽可能的省一些路上的花销。给定一组城市和每对城市之间的火车票的价钱，找到每个城市只访问一次并返回起点的最小车费花销。
# 输入描述:
# 城市个数n（1<n≤20，包括北京）
#
# 城市间的车票价钱 n行n列的矩阵 m[n][n]
# 输出描述:
# 最小车费花销 s
import sys

def TSP(N,matrix):
    m, n = N**2, N
    # 状态压缩DP,5表示0101,dp[i][j]表示从0出发,经过i中的几个到达j,要求i中有j
    dp = [[float('inf')] * n for _ in range(m)]
    dp[1][0] = 0
    for i in range(1, m):
        if not (i & 1):  # i中不能包括0,不能从0出发
            continue
        for j in range(1, n):  # j是要加入的
            if i & (1 << j):  # 如果i中包括j就重复了
                continue
            for k in range(n):
                if i & (1 << k):  # 如果i中包括k
                    # i中加上j,0到j的最短距离可能为原来i中任何一个k到j的距离与剩余最短距离之和
                    dp[(1 << j) | i][j] = min(dp[(1 << j) | i][j], dp[i][k] + matrix[k][j])
    res = float('inf')
    # 最后还要回到0
    for i in range(n):
        res = min(res, dp[m - 1][i] + matrix[i][0])
    return res


if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    maxtri = []
    for i in range(N):
        list_hang = list(map(int,sys.stdin.readline().strip().split()))
        maxtri.append(list_hang)
    print(TSP(N,maxtri))
