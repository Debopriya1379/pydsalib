class Node:
    def __init__(self,val):
        self.info=val
        self.next=None

class PythonLStack:
    def __init__(self):
        self.start=None
        self.top=None
    def push(self,val):
        new_node=Node(val)
        if(self.start==None and self.top==None):
            self.start=new_node
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
    def pop(self):
        if(self.top==None and self.start==None):
            print("Cannnot pop, stack is empty")
            return
        elif(self.top==self.start):
            temp=self.top
            self.top=None
            self.start=None
            item=temp.info
            del temp
            return item
        else:
            temp=self.top
            self.top=temp.next
            item=temp.info
            del temp
            return item
    def peek(self):
        if(self.start==None and self.top==None):
            print("stack is empty")
            return 
        item=self.top.info
        return item
    def display(self):
        if(self.start==None and self.top==None):
            print("stack is empty")
        elif(self.start==self.top):
            print(self.top.info)
        else:
            temp=self.top
            while(temp!=self.start):
                print(temp.info," <- ",end='')
                temp=temp.next
            print(temp.info)

# if __name__=="__main__":
#     ls=PythonLStack()
#     ls.display()
#     ls.push(1)
#     ls.push(2)
#     ls.push(3)
#     ls.push(4)
#     print(ls.peek())
#     ls.display()
#     ls.pop()
#     ls.display()

