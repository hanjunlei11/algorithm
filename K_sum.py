#对于K=2时用头尾指针法，时间复杂度是O（N），如果给定的数组不是有序的，排序需要的时间复杂度是O(NlogN)，快速排序
#排序算法可以自己写，也可以直接使用sort（）函数，时间复杂度一样

#对于K=3时把问题退化成2sum问题，具体来说就是第一层指定第一个数字，然后使用头尾扫描，时间复杂度为O(N^2)
#如果使用排序的话，时间复杂度为O(N^2logN)

#对于K=4的情况，利用哈希表map[value]==[x,y],两两组合，时间复杂度是O(N^2)
#再排序，再然后回归到K=2的情况这一步时间复杂度是O（N），需要注意的是，这里的N是原来的N^2，所以总的时间复杂度为O(N^2)]
import sys
def take_three(k):
    return k[2]

def is_True(x1,y1,x2,y2):
    l = [x1,y1,x2,y2]
    if len(l) == len(list(set(l))):
        return True,list(set(l))
    else:
        return False,[]

def four_sum(num,sum):
    map_hash = []
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            temp = num[i]+num[j]
            map_hash.append([i,j,temp])
    map_hash.sort(key=take_three)
    print(map_hash)
    left = 0
    right = len(map_hash)-1
    res = []
    while left!=right:
        left_h = map_hash[left]
        right_h = map_hash[right]
        flog,temp = is_True(left_h[0],left_h[1],right_h[0],right_h[1])
        if (left_h[2] + right_h[2]) == sum:
            #这个地方实际上有问题，如果value值有重复的地方，那实际上应该把重复的部分进行全排列，然后再往中间递进
            #不然会漏掉
            if flog:
                if temp not in res:
                    res.append(temp)
                left+=1
            else:
                left+=1
        if (left_h[2]+right_h[2]) > sum:
            right-=1
            continue
        if (left_h[2]+right_h[2]) < sum:
            left+=1
            continue
    return res

if __name__=="__main__":
    sum = int(sys.stdin.readline().strip())
    num = list(map(int,sys.stdin.readline().strip().split()))
    print(four_sum(num,sum))