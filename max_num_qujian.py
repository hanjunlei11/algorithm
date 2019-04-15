#给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
#区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。

#思路：两个要素，区间当中最小点的值、区间的和，当区间中最小的值固定时，区间越长越好。
#1、遍历给定数组中的点，把改点当做最小值的点，向左向右遍历点，知道找到比该点小的点。
#2、到达左右边界，遍历的时候依次计算区间的和（sum）。
#3、计算最小值和sum的乘积，如果比之前计算的最大值大，就更新最大值，否则继续选择下一个最小点。重复步骤1/2/3。
import sys

def max_num(num,N):
    res = 0
    for i in range(N):
        min_x = num[i]
        if min_x == 0:
            continue
        left_x = i-1
        right_x = i+1
        sum_x = min_x
        while 0<=left_x<=N-1:
            if num[left_x]>=min_x:
                sum_x+=num[left_x]
                left_x-=1
            else:
                break
        while 0<=right_x<=N-1:
            if num[right_x]>=min_x:
                sum_x+=num[right_x]
                right_x+=1
            else:
                break
        sqrt_x = min_x*sum_x
        if sqrt_x>res:
            res = sqrt_x
    return res

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    num = [int(i) for i in sys.stdin.readline().strip().split()]
    print(max_num(num,N))