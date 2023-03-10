class Node:
    def __init__(self,val):
        self.info=val
        self.next=None

class PythonSinglyLinkedList:
    def __init__(self):
        self.start=None
    def insertAtBegining(self,val):
        new_node=Node(val)
        if(self.start==None):
            self.start=new_node
        else:
            new_node.next=self.start
            self.start=new_node
    def insertAtEnding(self,val):
        new_node=Node(val)
        if(self.start==None):
            self.start=new_node
        else:
            i=self.start
            while(i.next!=None):
                i=i.next
            i.next=new_node
    def insertAtSpecificPosition(self,val,pos):    
        if pos==1:
            self.insertAtBegining(val)
            return
        new_node=Node(val)
        temp=self.start
        i=1
        while(temp!=None and i<pos-1):
            temp=temp.next
            i+=1
        if temp==None:
            print("given position doesn't exists")
            return
        new_node.next=temp.next
        temp.next=new_node
    def insertAfterSpecificValue(self,val,key):
        new_node=Node(val)
        temp=self.start
        while(temp!=None and temp.info!=key):
            temp=temp.next
        if temp==None:
            print("given value doesn't exists in the linked list")
            return
        new_node.next=temp.next
        temp.next=new_node
    def insertBeforeSpecificValue(self,val,key):
        if self.start.info==key:
            self.insertAtBegining(val)
            return
        new_node=Node(val)
        temp=self.start
        while(temp!=None and temp.info!=key):
            prev=temp
            temp=temp.next
        if temp==None:
            print("given value doesn't exists in the linked list")
            return
        new_node.next=temp
        prev.next=new_node
    def deleteAtBegining(self):
        if(self.start==None):
            print('Cannot delete, linked is is empty')
        else:
            node=self.start
            self.start=node.next
            item=node.info
            del node
            return item
    def deleteAtEnding(self):
        if(self.start==None):
            print('Cannot delete, linked is is empty')
        else:
            i=self.start
            while i.next!=None:
                prev=i
                i=i.next
            prev.next=None
            item=i.info
            del i
            return item
    def deleteAtSpecificPosition(self,pos):
        if(self.start==None):
            print('Cannot delete, linked is is empty')
            return
        if(pos==1):
            self.deleteAtBegining()
            return
        temp=self.start
        i=1
        while(temp!=None and i<pos-1):
            temp=temp.next
            i+=1
        if temp==None:
            print("given position doesn't exist")
            return
        temp.next=temp.next.next
    def deleteSpecificValue(self,val):
        if(self.start==None):
            print('Cannot delete, linked is is empty')
            return
        if self.start.info==val:
            self.deleteAtBegining()
            return
        temp=self.start
        while(temp!=None and temp.info!=val):
            prev=temp
            temp=temp.next
        if temp==None:
            print("given value doesn't exist in the linked list")
            return
        prev.next=temp.next
        temp.next=None
        del temp
    def search(self,val):
        if(self.start==None):
            print('Linked list is empty')
        else:
            i=self.start
            while(i!=None):
                if i.info==val:
                    print('item found')
                    return
                i=i.next
            print('item not found')
    def display(self):
        if(self.start==None):
            print('Linked list is empty')
        else:
            i=self.start
            while(i!=None):
                print(i.info,'<-',end=' ')
                i=i.next
            print()

if __name__=='__main__':
    SL=PythonSinglyLinkedList()
    SL.display()
    SL.insertAtBegining(3)
    SL.insertAtBegining(4)
    SL.insertAtBegining(1)
    SL.insertAtEnding(7)
    SL.display()
    # SL.insertAtSpecificPosition(5,10)   
    # SL.insertAfterSpecificValue(5,7)
    # SL.insertBeforeSpecificValue(10,1) 
    # SL.deleteAtBegining()
    # SL.deleteAtEnding()
    # SL.deleteAtSpecificPosition(7)  
    # SL.deleteSpecificValue(11)      
    SL.display()
#     SL.display()
#     SL.search(4)
#     SL.search(3)
#     SL.search(6)

