class Node:
    def __init__(self,val):
        self.info=val
        self.next=None

class PythonLQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,val):
        new_node=Node(val)
        if(self.front==None and self.rear==None):
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if(self.front==None and self.rear==None):
            print("Cannot delete, Queue is empty")
        elif(self.front==self.rear):
            temp=self.front
            self.front=None
            self.rear=None
            item=temp.info
            del temp
            return item
        else:
            temp=self.front
            self.front=temp.next
            item=temp.info
            del temp
            return item
    def display(self):
        if(self.front==None and self.rear==None):
            print("Queue is empty")
            return
        temp=self.front
        while(temp!=None):
            print(temp.info," <- ",end="")
            temp=temp.next
        print()
    def isEmpty(self):
        if(self.front==None and self.rear==None):
            return True
        else:
            return False
    
# if __name__=="__main__":
#     lq=PythonLQueue()
#     lq.display()
#     lq.enqueue(1)
#     lq.enqueue(2)
#     lq.enqueue(3)
#     lq.display()
#     lq.dequeue()
#     lq.display()