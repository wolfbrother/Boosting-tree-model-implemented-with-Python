import numpy as np
class Classifier:
    def __init__(self):
        self.__stumps = []
        self.aa = self.__stumps
        self.__hasmakemodel = False

        self.__posuniq = np.nan
        self.__valuelist = np.nan
    def add(self,pos,val1,val2):
        self.__hasmakemodel = False
        exceptlabel = False
        try:
            np.sum(np.array([pos,val1,val2])+1)       
        except:
            exceptlabel = True
        if exceptlabel == False:
            stump = self.__stump(pos,val1,val2)
            self.__stumps.append(stump)
        else:
            print 'Input parameter is INVALID.\n\t Try again please.'

    def __stump(self,pos,val1,val2):
        return {'pos':pos,'val':(val1,val2)}
    def __makemodel(self):

        self.__posuniq = list(set([stump['pos'] for stump in self.__stumps]))
        self.__posuniq.sort()
        self.__valuelist = np.zeros(len(self.__posuniq)+1)

        for stump in stumps:
            idx = self.__posuniq.index(stump['pos'])
            self.__valuelist[:idx+1] += stump['val'][0]
            self.__valuelist[idx+1:] += stump['val'][1] 
        self.__hasmakemodel = True
    def predict(self,x):
        if self.__hasmakemodel == False:
            self.__makemodel()            
        for idx in range(len(self.__posuniq)+1):
            try:
                if x <  self.__posuniq[idx]:
                    break
            except:
                pass  
        y = self.__valuelist[idx]   
        return y
if __name__ == "__main__":
    classifier = Classifier()
    classifier.add(6.5,6.24,8.91)
    classifier.add(3.5,-0.52,0.22)
    classifier.add(6.5,0.15,-0.22)
    classifier.add(4.5,-0.16,0.11)
    classifier.add(6.5,0.07,-0.11)
    classifier.add(2.5,-0.15,0.04)

    predictlist = np.array([classifier.predict(i+1) for i in range(10)])
    valuelist = np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])
    loss = np.sum(np.power(predictlist - valuelist,2))
    print '平方误差：',str(loss)    
