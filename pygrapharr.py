class PythonGraph:
    def __init__(self,size) -> None:
        self.size=size
        self.matUnDir=[[0 for i in range(size)] for i in range(size)]
        self.matDir=[[0 for i in range(size)] for i in range(size)]
    def createAdjMatUnDir(self,ls):
        # n=int(input('Enter no of edges : '))
        # for i in range(n):
        #     p=int(input('Enter source : '))
        #     q=int(input('Enter destination : '))
        #     self.mat[p][q]=1
        #     self.mat[q][p]=1
        for p,q in ls:
            self.matUnDir[p][q]=1
            self.matUnDir[q][p]=1
    def createAdjMatDir(self,ls):
        for p,q in ls:
            self.matDir[p][q]=1
    def printAdjMatUnDir(self):
        for i in self.matUnDir:
            print(i)
        print()
    def printAdjMatDir(self):
        for i in self.matDir:
            print(i)
        print()
    def getDegree(self) -> list:
        ls=[0 for i in range(self.size)]
        for i,j in enumerate(self.matUnDir):
            ls[i]=j.count(1)
        return ls
    def getInOutDegree(self) -> list:
        InD=[0 for i in range(self.size)]
        OutD=[0 for i in range(self.size)]
        for i,j in enumerate(self.matDir):
            InD[i]=j.count(1)
        for i in range(self.size):
            OutD[i]=[row[i] for row in ob.matDir].count(1)
        return InD,OutD


ob=PythonGraph(int(input('Enter no of vertices : ')))
edgeListUnDir=[(0,1),(0,2),(1,2),(1,3),(2,4),(3,5),(4,5),(1,4)]
edgeListDir=[(0,1),(0,2),(1,2),(1,3),(2,4),(3,5),(4,5),(4,1)]
ob.createAdjMatUnDir(edgeListUnDir)
ob.printAdjMatUnDir()
ob.createAdjMatDir(edgeListDir)
ob.printAdjMatDir()
print(ob.getDegree())
print(ob.getInOutDegree())
