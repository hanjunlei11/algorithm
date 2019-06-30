# 总共有36张牌，每张牌是1~9。每个数字4张牌。
# 你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌
# 14张牌中有2张相同数字的牌，称为雀头。
# 除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）
#
# 例如：
# 1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
# 1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
# 1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。
#
# 现在，小包从36张牌中抽取了13张牌，他想知道在剩下的23张牌中，再取一张牌，取到哪几种数字牌可以和牌。
#思路：利用递归思想，逐个条件判断
import sys
def quehun(pai):
    n = len(pai)
    if n==0:
        return True
    first = pai.count(pai[0])
    if n % 3 != 0 and first>=2 and quehun(pai[2:])==True:
        return True
    if first>=3 and quehun(pai=pai[3:]) == True:
        return True
    if pai[0]+1 in pai and pai[0]+2 in pai:
        temp = pai.copy()
        temp.remove(pai[0])
        temp.remove(pai[0]+1)
        temp.remove(pai[0]+2)
        if quehun(temp)==True:
            return True
    return False

if __name__=="__main__":
    pai = list(map(int,sys.stdin.readline().strip().split()))
    card = {}
    for i in pai:
        if i in card:
            card[i] = card[i]+1
        else:
            card[i] = 1
    card_k = set(range(1,10))-{i for i,v in card.items() if v==4}
    res = []
    for i in card_k:
        if quehun(sorted(pai+[i])):
            res.append(str(i))
    if len(res)==0:
        print(0)
    else:
        print(' '.join(res))
