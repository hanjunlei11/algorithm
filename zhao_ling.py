import sys
def helper(num):
    res = ""
    while num>0:
        if ((num-2)/2)%1==0:
            res = '3'+res
            num = (num-2)/2
        if ((num-1)/2)%1==0:
            res =  '2'+res
            num = (num-1)/2
    return res
if __name__ == "__main__":
    obj = int(sys.stdin.readline().strip())
    ans = helper(obj)
    print(ans)