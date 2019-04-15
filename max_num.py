#P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x）
# #则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
import sys

def sor(k):
    return k[0]

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    num = [[]]*N
    for i in range(N):
        x,y = list(map(int,sys.stdin.readline().strip().split()))
        num[i] = [x,y]
    num.sort(key=sor)
    res = []
    while len(num)>0:
        temp = num.pop()
        res.append(temp)
        temp1 = []
        for i in range(len(num)):
            if num[i][1]>temp[1]:
                temp1.append(num[i])
        num = temp1
    len_x = len(res)
    for i in range(len(res)):
        len_x-=1
        print(str(res[len_x][0])+' '+str(res[len_x][1]))
