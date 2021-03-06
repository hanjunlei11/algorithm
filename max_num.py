#P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x）
# #则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
#思路：将给定的元组按照X的值从小到大排序，然后由于没有重复值，所以最右边的元组是符合条件的
#然后把最后的元组pop出来，存入list，再然后在最后元组左下方的是不符合条件的，左上方的可能符合条件。
#把左下方的去除，然后把左上方的更新到原来的list里面去，重复上述步骤，直到list为空

#通过率80%，内存超限。。。。。
import sys

def sor(k):
    return k[0]

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    num = [[]]*N
    for i in range(N):
        x,y = list(map(int,sys.stdin.readline().strip().split()))
        num[i] = [x,y]
    num.sort(key=sor,reverse=True)
    res = []
    max_y = 0
    for j in range(len(num)):
        if num[j][1]>=max_y:
            res.append(num[j])
            max_y = num[j][1]
    len_x = len(res)
    for i in range(len(res)):
        len_x-=1
        print(str(res[len_x][0])+' '+str(res[len_x][1]))
