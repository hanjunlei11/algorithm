#作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。
# 为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
# 手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。
# 请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个串珠中出现了至少两次。
#第一行输入n，m，c三个数，用空格隔开。(1 <= n <= 10000, 1 <= m <= 1000, 1 <= c <= 50)
# 接下来n行每行的第一个数num_i(0 <= num_i <= c)表示第i颗珠子有多少种颜色。
# 接下来依次读入num_i个数字，每个数字x表示第i颗柱子上包含第x种颜色(1 <= x <= c)

#一个非负整数，表示该手链上有多少种颜色不符需求。
#算法复杂度过大，通过率60%

if __name__=="__main__":
    N,M,C = map(int,input().split())
    num = [[]]*N
    for i in range(N):
        temp = list(map(int,input().split()))
        if temp[0]!=0:
            num[i]=temp[1:]
    num = num+num[0:M]
    res = set()
    for i in range(N):
        dic = {}
        temp = num[i:M+i]
        for j in range(M):
            for k in temp[j]:
                if str(k) not in dic:
                    dic[str(k)] = 1
                else:
                    res.add(k)
    print(len(res))