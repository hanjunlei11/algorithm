# 我叫王大锤，是一家出版社的编辑。我负责校对投稿来的英文稿件，这份工作非常烦人，因为每天都要去修正无数的拼写错误。但是，优秀的人总能在平凡的工作中发现真理。我发现一个发现拼写错误的捷径：
#
# 1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

#通过

import sys
def check_string(string):
    string2 = ''
    for char in string:
        if len(string2)<2:
            string2+=char
            continue
        if len(string2)>=2:
            if char == string2[-1] and char == string2[-2]:
                continue
        if len(string2)>=3:
            if char == string2[-1] and string2[-2] == string2[-3]:
                continue
        string2 += char
    return string2

if __name__=='__main__':
    N = int(sys.stdin.readline())
    for i in range(N):
        string = sys.stdin.readline().strip()
        chars = check_string(string=string)
        print(chars)