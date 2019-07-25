import sys

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    res = 1
    for i in range(1,N+1):
        res*=i
    for i in range(2,N+1):
        temp = 1
        for j in range(N-i+1,N+1):
            temp*=j
        temp1 = 1
        for j in range(1,i+1):
            temp1*=j
        temp2 = temp//temp1
        temp3 = 1
        for j in range(1,N-i+2):
            temp3*=j
        res +=temp2*temp3
    print(res)