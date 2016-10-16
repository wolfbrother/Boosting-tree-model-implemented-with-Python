import numpy as np
import copy
class BoostingTree:
    def __init__(self,data,iters=6):
        self.__data = copy.deepcopy(data)

        #将一个Classifier对象作为成员
        self.__classifier = Classifier()
        self.__division = [(self.__data['x'][idx]+self.__data['x'][idx+1])/2.0 for idx in range(self.__data['x'].shape[0]-1)]
        self.__iters = iters
        self.__hasmakemodel = False

    def __makemodel(self):
        residuallist = self.__data['y']

        for it in range(self.__iters):
            performancelist = []
            predictlist = np.zeros(residuallist.shape[0])
            for idx,x in enumerate(self.__division): 

                meanleft = np.mean(residuallist[:idx+1]) #左侧的均值
                predictlist[:idx+1] = meanleft
                meanright = np.mean(residuallist[idx+1:]) #右侧的均值
                predictlist[idx+1:] = meanright
                loss = np.sum(np.power(residuallist - predictlist,2)) #平方误差
                performancelist.append([loss,x,meanleft,meanright])

            #xidx是最优的分界点序号
            xidx = np.argmin([performance[0] for performance in performancelist]) 

            #下面两行求残差
            residuallist[:xidx+1] -= performancelist[xidx][2]
            residuallist[xidx+1:] -= performancelist[xidx][3]

            #添加新的弱分类器
            self.__classifier.add(performancelist[xidx][1],performancelist[xidx][2],performancelist[xidx][3])
        self.__hasmakemodel = True
    def predict(self,x):

        if self.__hasmakemodel == False:
            self.__makemodel()
        try: #当x不是单个数字元素时
            x[0]
            size = np.shape(x)[0]
            y = [0]*size
            for i in range(size):
                y[i] = self.__classifier.predict(x[i])
            return y
        except:
            return self.__classifier.predict(x)   
