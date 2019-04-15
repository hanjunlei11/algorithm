import sys

if __name__=="__main__":
    N = int(input().strip())
    num = list(map(int,input().split()))
    num.sort(reverse=True)
    max_value = 0
    for i in range(1,N):
        temp = num[0:i]
        print(temp)
        min_x = min(temp)
        sum_x = sum(temp)
        max_x = min_x*sum_x
        if max_x>max_value:
            max_value = max_x
    print(max_value)