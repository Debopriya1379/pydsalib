class Node:
    def __init__(self,c,e):
        self.coff=c
        self.exp=e
        self.next=None

class PolynomialLL:
    def __init__(self):
        self.start=None
    def add_term(self,c,e):
        if(self.start==None):
            new_node=Node(c,e)
            self.start=new_node
            return
        else:
            temp=self.start
            while(temp!=None and temp.exp!=e):
                temp=temp.next
            if(temp!=None):
                temp.coff+=c
                return
            else:
                new_node=Node(c,e)
                prev2=None
                temp2=self.start
                while(temp2!=None and temp2.exp>e):
                    prev2=temp2
                    temp2=temp2.next
                if(temp2==None):
                    prev2.next=new_node
                    return
                else:
                    if(prev2==None):
                        new_node.next=temp2
                        self.start=new_node
                        return
                    else:
                        prev2.next=new_node
                        new_node.next=temp2
    def display(self):
        if(self.start==None):
            print("Empty")
            return
        temp=self.start
        while(temp!=None):
            print(temp.coff,"y^",temp.exp," ",end='')
            temp=temp.next
        print()

pl=PolynomialLL()
pl.display()
pl.add_term(8,2)
pl.add_term(-7,0)
pl.add_term(6,3)
pl.add_term(5,4)
pl.add_term(-2,5)
pl.add_term(5,4)
pl.add_term(6,3)
pl.add_term(6,1)
pl.display()