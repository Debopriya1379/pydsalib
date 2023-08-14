import pylqueue
class Node:
    def __init__(self,val) -> None:
        self.info=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self) -> None:
        self.root=None
        self.idx=-1
    def buildTreeFromPreorder(self,lst):
        self.idx+=1
        if(lst[self.idx]==-1):
            return None
        new_node=Node(lst[self.idx])
        new_node.left=self.buildTreeFromPreorder(lst)
        new_node.right=self.buildTreeFromPreorder(lst)
        return new_node
    def displayInorder(self,head):
        if(head==None):
            return
        self.displayInorder(head.left)
        print(head.info,' -> ',end='')
        self.displayInorder(head.right)
    def displayLevelorder(self,head):
        if head==None:
            return
        qu=pylqueue.PythonLQueue()
        qu.enqueue(head)
        qu.enqueue(None)
        while(not qu.isEmpty()):
            curr=qu.dequeue()
            if(curr==None):
                print()
                if(qu.isEmpty()):
                    break
                else:
                    qu.enqueue(None)
            else:
                print(curr.info,' ',end='')
                if(curr.left != None):
                    qu.enqueue(curr.left)
                if(curr.right != None):
                    qu.enqueue(curr.right)
    def countNodes(self,head):
        if(head==None):
            return 0
        return self.countNodes(head.left)+self.countNodes(head.right)+1
    def sumNodes(self,head):
        if(head==None):
            return 0
        return self.sumNodes(head.left)+self.sumNodes(head.right)+head.info
    def getHeight(self,head):
        if head==None:
            return 0
        return max(self.getHeight(head.left),self.getHeight(head.right))+1
    def getDiameter(self,head):
        if head==None:
            return 0
        diam1=self.getDiameter(head.left)
        diam2=self.getDiameter(head.right)
        diam3=self.getHeight(head.left)+self.getHeight(head.right)+1
        return max(diam1,diam2,diam3)
    
    class TreeInfo:
        def __init__(self,h,d) -> None:
            self.height=h
            self.diam=d
    def getDiameter2(self,head):
        if head==None:
            return self.TreeInfo(0,0)
        left = self.getDiameter2(head.left)
        right = self.getDiameter2(head.right)
        myheight=max(left.height,right.height)+1
        diam1=left.diam
        diam2=right.diam
        diam3=left.height+right.height+1
        mydiam=max(diam1,diam2,diam3)
        myinfo=self.TreeInfo(myheight,mydiam)
        return myinfo

            
l=[1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
bt=BinaryTree()
root=bt.buildTreeFromPreorder(l)
bt.displayInorder(root)
print('None')
# bt.displayLevelorder(root)
# print(bt.countNodes(root))
# print(bt.sumNodes(root))
# print(bt.getHeight(root))
# print(bt.getDiameter(root))
# print(bt.getDiameter2(root).diam)

 