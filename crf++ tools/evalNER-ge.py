# call from unix shell as
# python eval.py goldstandardfile.txt yoursystemoutput.txt
#

import sys,os



def eval(keys, predictions):
    """ Given a stream of gold standard word/tag pairs and a stream of system pairs. Figure out the the recall, precision and F1 """


    goldStandardEntities = findEntities(taggedData(keys))     # get the entities in the gold standard
    systemEntities = findEntities(taggedData(predictions))    # and the entities in the system output

    numEntities = len(goldStandardEntities)                   # number of entities there should be
    print(numEntities)
    numReturned = len(systemEntities)                         # number actually tagged by system
    print(numReturned)
    numTruePositives = len(set.intersection(goldStandardEntities,systemEntities))    # number of those that were right

    precision = float(numTruePositives)/numReturned
    recall = float(numTruePositives)/numEntities
    f1 = 2 * (precision * recall)/(precision + recall)

    print(numEntities, " entities in gold standard.")
    print(numReturned, " total entities found.")
    print(numTruePositives, " of which were correct.")
    
    print("\t", "Precision: ", precision, "Recall: ", recall, "F1-measure: ", f1)

def findEntities(data):
    """ Find all the IOB delimited entities in the data.  Return as a set of (begin, end) tuples. Data is sequence of word, tag pairs. """

    entities = set()

    entityStart = 0
    entityEnd = 0
    
    currentState = "Q0"
    count = 0

    for tag in data:
        count = count + 1
        if currentState == "Q0":
            if tag == 'B':
                currentState = "Q1"
                entityStart = count
        elif currentState == "Q1":
            if tag == "B":
                entityEnd = count - 1
                entities.add((entityStart, entityEnd))
                entityStart = count
            if tag == "O":
                entityEnd = count - 1
                entities.add((entityStart, entityEnd))
                currentState = "Q0"

    if currentState == "Q1":
        entities.add((entityStart, entityEnd))

    return entities

def taggedData(file):
    for line in file:
        if line.strip() == '\n':
            yield(['</s>', 'O'])
        else:
            yield line.strip()

if __name__ == "__main__":
#	file=sys.argv[1]
	os.system('crf_learn -f 4 -p 24 -a CRF-L2 -c 4.0 template1 train2021-new.txt model2021')
	os.system('crf_test -m model2021 test2021-new.txt >output1127.txt')
	
	with open(r'output1127.txt',encoding='utf-8')as f:
		keys=[i.split()[1] if i!='\n' else '\n' for i in f]
	with open(r'output1127.txt',encoding='utf-8')as f:
		predictions=[i.split()[2] if i!='\n' else '\n' for i in f]
	eval(keys,predictions)
