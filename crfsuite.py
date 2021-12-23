'''
Created on 2021年11月28日

@author: Konic
'''
import pandas as pd
from sklearn_crfsuite import CRF
from sklearn.model_selection import cross_val_predict
def read_data(file):
# data=pd.read_table(r'D:\S21-gene-train.txt',sep='\t',header=None)
    sentence=[]
    sentences=[]
    with open(file,encoding='utf-8')as f:
        
        for i in f:
    #         print(i)
            if i.strip()=='':
                 
                sentences.append(sentence)
                sentence=[]
                 
                 
            else:
                line=i.split()
                sentence.append((line[:]))
     
        sentences.append(sentence)
    return sentences
# print(sentences[0][0])
# print(data.tail(10))
def word2features(sent,i):
  word = sent[i][0]
 

  features = {
      "bias": 1.0,
      'words':word,
      "word.islower()": word.islower(),
#       "word[-3:]": word[-3:],
#       "word[2:]": word[2:],
      "word.isupper()": word.isupper(),
      "word.istitle()": word.istitle(),
      "word.isdigit()": word.isdigit(),
  }
  if i > 0:
    word1 = sent[i-1][0]
    features.update({
        '-1:word':word1,
    "-1:word.isupper()": word1.isupper(),
      "-1:word.istitle()": word1.istitle(),
      "-1:word.isdigit()": word1.isdigit(),

    })
  else:
    features["BOS"] = True
  if i < len(sent) - 1:
    word1 = sent[i+1][0]
    features.update({
        '+1:word':word1,
      "+1:word.isupper()": word1.isupper(),
      "+1:word.istitle()": word1.istitle(),
      "+1:word.isdigit()": word1.isdigit(),

    })
  else:
    features["EOS"] = True
  return features

def sent2features(sent):
  return [word2features(sent,i) for i in range(len(sent))]

def sent2labels(sent):
  return [label for _, label in sent]

# def sent2tokens(sent):
#   return [token for token, _, _ in sent]
sentences=read_data(r'D:\train2021.txt')
  
trainX=[sent2features(s) for s in sentences]
trainy=[sent2labels(s) for s in sentences]
crf=CRF(algorithm='lbfgs',c1=0.1,c2=0.1,max_iterations=100,all_possible_transitions=True )
crf.fit(trainX,trainy)
# sent=read_data(r'D:\test2021.txt')
sent=read_data(r'D:\My python\crf++ tools\test-set.txt')

# 

X=[sent2features(s) for s in sent]

# y=[sent2labels(s) for s in sent]
 
test_pre=crf.predict(X)
# print(len(test_pre),len(sent))
with open(r'D:\crfsuite-output.txt','w',encoding='utf-8') as f1:
      
    for k,a in zip(test_pre,sent):
        for v,c in zip(k,a):
    
            print(c[0]+'\t'+v,file=f1)
        print('',file=f1)
# pred=cross_val_predict(crf, X, y, groups, cv=5)
# print(pred)
