# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:33:23 2018

@author: DELL
"""
from collections import Counter
gold=[]
tagged=[]
def evaluate(filepath,outpath):
    with open(filepath) as f:
        for i in f:
            if i=="\n":
                continue
            i=i.strip().split()
            gold.append(i[1])#分别把答案和标注存为两个list
            tagged.append(i[2])
    c1=Counter(gold)
    c2=Counter(tagged)
    gold_num= c1["E"]+c1["BE"]#通过counter内置字典得到词数
    tagged_num= c2["E"]+c2["BE"]
    score=0
    for t ,j in enumerate(zip(gold,tagged)):
        
        
        if j[0]==j[1] and j[0]=="BE":#正确单字词数量
            score+=1
        elif j[0]==j[1] and j[0]=="B":#如果开头是B并且每个都一样，那么到E算是标对一个整词
            for c,k in zip(gold[t+1:],tagged[t+1:]):
                if c==k :
                    if c!="E":
                        continue
                    else:
                        score+=1
                        break
    with open(outpath,"w") as f1:
        print>>f1, "precision:%.2f%%"%((float(score)/gold_num)*100)
        print>>f1, "recall:%.2f%%"%((float(score)/tagged_num)*100)
        print>>f1, "F-score:%.2f%%"%((2*(float(score)/gold_num)*(float(score)/tagged_num))/(float(score)/gold_num+float(score)/tagged_num)*100)

    

                
   
    
    
            
            
if __name__=="__main__":
    evaluate(r"D:\My python\crf++ tools\output.txt",r"D:\My python\crf++ tools\evaluate.txt")