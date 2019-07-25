
if __name__=="__main__":
    with open("E:/code/sgns.merge.word/sgns.merge.word",'r',encoding='utf-8') as file:
        i = 0
        for temp in range(10):
            print(file.readline())
            if i == 10:
                break
            i+=1