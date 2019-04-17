#字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
# 询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？

#输入：第一行为一个字符串S与一个非负整数m。(1<=|S|<=103,1<=m<=106)
#输出：一个非负整数，表示操作之后，连续最长的相同字母数量。

#完美通过，小心list乘以数字这种生成方法，生成的子对象都是指向同一个地址，一个变，都跟着变
#如果需要修改list中的数据，最好用range的形式复制

import sys

if __name__=="__main__":
    string,N = sys.stdin.readline().strip().split()
    N = int(N)
    res = 1
    zimu = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(zimu)):
        pos = []
        for j in range(len(string)):
            if string[j]==zimu[i]:
                pos.append(j)
        ret = 1
        dp = [[0 for _ in range(len(pos))] for _ in range(len(pos))]
        for len_x in range(2,len(pos)+1):
            for k in range(len(pos)-len_x+1):
                dp[k][k+len_x-1] = dp[k+1][k+len_x-2]+pos[k+len_x-1]-pos[k]-len_x+1
                if dp[k][k+len_x-1]<=N:
                    ret = len_x
        res = max(res,ret)
    print(res)