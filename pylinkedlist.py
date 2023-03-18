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

class PythonCircularLinkedList:
    def __init__(self):
        self.start=None
    def insertAtBegining(self,val):
        new_node=Node(val)
        if(self.start==None):
            self.start=new_node
            new_node.next=new_node
        else:
            # prev=self.start      #approach 1 
            # self.start=new_node
            # new_node.next=prev
            # temp=prev
            # while(temp.next!=prev):
            #     temp=temp.next
            # temp.next=self.start
            temp=self.start        #approach 2
            while(temp.next!=self.start):
                temp=temp.next
            prev=self.start
            self.start=Node(val)
            self.start.next=prev
            temp.next=self.start
    def insertAtEnd(self,val):
        new_node=Node(val)
        if(self.start==None):
            self.start=new_node
            new_node.next=new_node
        temp=self.start
        while(temp.next!=self.start):
            temp=temp.next
        temp.next=new_node
        new_node.next=self.start
    def insertAtSpecificPosition(self,val,pos):
        if(pos==1):
            self.insertAtBegining(val)
        else:
            new_node=Node(val)
            i=1
            temp=self.start
            prev=self.start
            while(temp.next != self.start and i<=pos-1):
                prev=temp
                temp=temp.next
                i+=1
            if(temp.next==self.start and i<pos):
                print("Given position dees not exists")
                return
            elif(temp.next==self.start):
                self.insertAtEnd(val)
            else:
                prev.next=new_node
                new_node.next=temp
    def insertAfterSpecificValue(self,val,key):
        temp=self.start
        while(temp.next!=self.start and temp.info!=key):
            temp=temp.next
        if(temp.next==self.start and temp.info!=key):
            print("Given key does not exists in the linked list")
        elif(temp.next==self.start and temp.info==key):
            self.insertAtEnd(val)
        else:
            new_node=Node(val)
            new_node.next=temp.next
            temp.next=new_node
    def deleteAtBegining(self):
        if(self.start==None):
            print("Cannot delete, Linked list is empty")
            return
        if(self.start.next==self.start):
            prev=self.start
            item=prev.info
            del prev
            self.start=None
            return item
        else:
            prev=self.start
            item=prev.info
            self.start=prev.next
            temp=self.start
            while(temp.next!=prev):
                temp=temp.next
            temp.next=self.start
            del prev
            return item
    def deleteAtEnd(self):
        if(self.start==None):
            print("Cannot delete, Linked list is empty")
            return
        if(self.start.next==self.start):
            prev=self.start
            item=prev.info
            del prev
            self.start=None
            return item
        temp=self.start
        while(temp.next!=self.start):
            prev=temp
            temp=temp.next
        prev.next=self.start
        item=temp.info
        del temp
        return item
    def deleteAtSpecificPosition(self,pos):
        if(pos<=0):
            print("Given position dees not exists")
            return
        if(self.start==None):
            print("Cannot delete, Linked list is empty")
            return
        if(pos==1):
            self.deleteAtBegining()
            return
        temp=self.start
        i=1
        while(temp.next!=self.start and i<=pos-1):
            prev=temp
            temp=temp.next
            i+=1
        if(temp.next==self.start and i<pos):
            print("Given position dees not exists")
            return
        elif(temp.next==self.start):
            self.deleteAtEnd()
        else:
            prev.next=temp.next
            item=temp.info
            del temp
            return item
    def deleteAfterSpecificValue(self,key):
        temp=self.start
        while(temp.next!=self.start and temp.info!=key):
            temp=temp.next
        if(temp.next==self.start and temp.info!=key):
            print("Given key does not exists in the linked list")
        elif(temp.next==self.start and temp.info==key):
            print("No node after the given key")
        else:
            delNode=temp.next
            temp.next=delNode.next
            item=delNode.info
            del delNode
            return item
    def display(self):
        if(self.start==None):
            print("linked list is empty")
            return
        temp=self.start
        while(temp.next!=self.start):
            print(temp.info," <- ",end='')
            temp=temp.next
        print(temp.info)
        # print()

# if __name__=='__main__':
#     cl=PythonCircularLinkedList()
#     cl.display()
#     cl.insertAtBegining(1)
#     cl.insertAtBegining(2)
#     cl.insertAtBegining(3)
#     cl.insertAtEnd(5)
#     cl.display()
#     cl.deleteAfterSpecificValue(5)
#     # cl.insertAfterSpecificValue(7,2)
#     cl.display()
    # cl.insertAtSpecificPosition(10,70)
    # cl.deleteAtBegining()
    # print(cl.deleteAtEnd())
    # cl.deleteAtSpecificPosition(5)
    # cl.display()
    ##########################################
    # SL=PythonSinglyLinkedList()
    # SL.display()
    # SL.insertAtBegining(3)
    # SL.insertAtBegining(4)
    # SL.insertAtBegining(1)
    # SL.insertAtEnding(7)
    # SL.display()
    # SL.insertAtSpecificPosition(5,10)   
    # SL.insertAfterSpecificValue(5,70)
    # SL.display()
    # SL.insertBeforeSpecificValue(10,1) 
    # SL.deleteAtBegining()
    # SL.deleteAtEnding()
    # SL.deleteAtSpecificPosition(7)  
    # SL.deleteSpecificValue(11)      
    # SL.search(4)
    # SL.search(3)
    # SL.search(6)
    # SL.display()
