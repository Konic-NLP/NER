'''
Created on 2021年11月17日

@author: Konic
'''
from collections import defaultdict


def greedy(filename):
    '''
    get each token with its frequent labels and store in a dict from the training set
    '''
#     tag=defaultdict(int)
    word2freq=defaultdict(lambda :defaultdict(int))
    with open(filename,encoding='utf-8')as f:
        for i in f:
            if i=='\n':
                continue
            i=i.split()
            word,tag=i[0],i[1]
         
            word2freq[word][tag]+=1
            
    return word2freq


def greedytag(filename,output,dic):
    '''
    tag the test set with the dict
    '''
    num=1
    
    with open(filename, encoding='utf-8')as f, open(output,'w',encoding='utf-8')as f1:
         for i in f:

            i=i.split()
            if i==[]:
                print('\n',end='',file=f1)
                num=1
            else:
                word=i[1]
                if dic[word]=={}:
                    maxtag='O'
                else:
                    maxtag=max(dic[word], key =lambda x:dic[word][x])
                print(str(num)+'\t'+word+'\t'+maxtag,file=f1)
                num+=1
                
    

dic=greedy(r'D:\train2021-new.txt')
greedytag(r'D:\网页下载\F21-gene-test.txt', r'D:\greedytag-pre.txt', dic)