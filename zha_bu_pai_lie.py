# 请听题：给定N（可选作为埋伏点的建筑物数）、D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，计算在这次行动中，大锤的小队有多少种埋伏选择。
# 注意：
# 1. 两个特工不能埋伏在同一地点
# 2. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用

import sys

def pailie(N,D,location):
    dp = 0
    j = 0
    for i in range(2,N):
            while (location[i]-location[j])>D and j<i:
                j += 1
            n = i-j
            dp = (dp+n*(n-1)//2)%99997867 if n>=2 else dp
    return dp

if __name__=='__main__':
    N,D = list(map(int,sys.stdin.readline().strip().split()))
    location = list(map(int,sys.stdin.readline().strip().split()))
    print(pailie(N,D,location))