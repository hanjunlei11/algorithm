# 小明是一名算法工程师，同时也是一名铲屎官。某天，他突发奇想，想从猫咪的视频里挖掘一些猫咪的运动信息。为了提取运动信息，他需要从视频的每一帧提取“猫咪特征”。一个猫咪特征是一个两维的vector<x, y>。如果x_1=x_2 and y_1=y_2，那么这俩是同一个特征。
#        因此，如果喵咪特征连续一致，可以认为喵咪在运动。也就是说，如果特征<a, b>在持续帧里出现，那么它将构成特征运动。比如，特征<a, b>在第2/3/4/7/8帧出现，那么该特征将形成两个特征运动2-3-4 和7-8。

# 现在，给定每一帧的特征，特征的数量可能不一样。小明期望能找到最长的特征运动。
# 第一行包含一个正整数N，代表测试用例的个数。
# 每个测试用例的第一行包含一个正整数M，代表视频的帧数。
# 接下来的M行，每行代表一帧。其中，第一个数字是该帧的特征个数，接下来的数字是在特征的取值；比如样例输入第三行里，2代表该帧有两个猫咪特征，<1，1>和<2，2>
# 所有用例的输入特征总数和<100000
# N满足1≤N≤100000，M满足1≤M≤10000，一帧的特征个数满足 ≤ 10000。
# 特征取值均为非负整数。
import sys
if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        M = int(sys.stdin.readline().strip())
        dict = {}
        res = 1
        for j in range(M):
            nums = list(map(int,sys.stdin.readline().strip().split()))
            k = nums[0]
            dict_d = {}
            for s in range(k):
                index = str(nums[s*2+1])+str(nums[s*2+2])
                if index in dict:
                    dict_d[index] = dict[index]+1
                    res = max(res,dict_d[index])
                else:
                    dict_d[index] = 1
            dict = dict_d
        print(res)