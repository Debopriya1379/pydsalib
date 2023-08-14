class PythonLinearQueue:
    def __init__(self,size=10):
        self.qu=[0 for i in range(size)]
        self.front=-1
        self.rear=-1
        self.size=size
    def enqueue(self,item):
        if self.rear==self.size-1 :
            print('Cannot insert, Queue is full')
            return
        self.rear+=1
        self.qu[self.rear]=item
        if self.front==-1:
            self.front=0
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print('Cannot delete, Queue is empty')
            return
        item=self.qu[self.front]
        if self.front==self.rear:
            self.rear=-1
            self.front=-1
        else:
            self.front+=1
        return item
    def display(self):
        if self.front==-1 and self.rear==-1:
            print('Queue is empty')
            return
        for i in range(self.front,self.rear+1):
            print(self.qu[i],'<- ',end='')
        print()
    def isEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False

class PythonCircularQueue:
    def __init__(self,s):
        self.cqu=[0 for i in range(s)]
        self.front=-1
        self.rear=-1
        self.size=s
    def enqueue(self,item):
        if self.front==(self.rear+1)%self.size:
            print('Cannot insert, Queue is full')
            return
        self.rear+=1
        self.cqu[self.rear]=item
        if self.front==-1:
            self.front=0
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print('Cannot delete, Queue is empty')
            return
        item=self.cqu[self.front]
        if self.front==self.rear:
            self.rear=-1
            self.front=-1
        else:
            self.front=(self.front+1)%self.size
        return item
    def display(self):
        if(self.front == -1):
            print ("Queue is Empty")
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.cqu[i],'<-',end = " ")
            print ()
        else:
            for i in range(self.front, self.size):
                print(self.cqu[i],'<-',end = " ")
            for i in range(0, self.rear + 1):
                print(self.cqu[i],'<-',end = " ")
            print ()
        print()
    def isEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False
        
# if __name__=='__main__':
#     Q=PythonLinearQueue(10)
#     Q.enqueue(4)
#     Q.enqueue(3)
#     Q.enqueue(2)
#     Q.enqueue(1)
#     Q.display()
# #     Q.display()
#     Q.dequeue()
#     Q.dequeue()
#     Q.display()
#     # Q.enqueue(4)
#     # Q.enqueue(5)
#     # Q.display()
#     # Q.enqueue(6)
#     # Q.display()
#     # Q.display()
#     CQ=PythonCircularQueue(5)
#     CQ.display()
#     # CQ.enqueue(1)
#     # CQ.enqueue(2)
#     CQ.enqueue(3)
#     # CQ.enqueue(4)
#     # CQ.enqueue(5)
#     CQ.enqueue(6)
#     CQ.display()
    # CQ.enqueue(7)
    # CQ.display()
    # CQ.dequeue()
    # CQ.dequeue()
    # CQ.display()