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

class AddTwoPolynomial:
    def __init__(self,poly1,poly2):
        self.poly1=poly1
        self.poly2=poly2
    def add(self):
        p1_temp=self.poly1.start
        p2_temp=self.poly2.start
        resPol=PolynomialLL()
        while(p1_temp!=None and p2_temp!=None):
            if(p1_temp.exp==p2_temp.exp):
                resPol.add_term((p1_temp.coff + p2_temp.coff),p1_temp.exp)
                p1_temp=p1_temp.next
                p2_temp=p2_temp.next
            elif(p1_temp.exp > p2_temp.exp):
                resPol.add_term(p1_temp.coff,p1_temp.exp)
                p1_temp=p1_temp.next
            else:
                resPol.add_term(p2_temp.coff,p2_temp.exp)
                p2_temp=p2_temp.next
        while(p1_temp!=None):
            resPol.add_term(p1_temp.coff,p1_temp.exp)
            p1_temp=p1_temp.next
        while(p2_temp!=None):
            resPol.add_term(p2_temp.coff,p2_temp.exp)
            p2_temp=p2_temp.next
        return resPol

class MultiplyTwoPolynomials:
    def __init__(self,p1,p2) -> None:
        self.poly1=p1
        self.poly2=p2
    def multiply(self):
        p1_temp=self.poly1.start
        p2_temp=self.poly2.start
        resPol=PolynomialLL()
        while(p1_temp!=None):
            while(p2_temp!=None):
                resPol.add_term((p1_temp.coff*p2_temp.coff),p1_temp.exp+p2_temp.exp)
                p2_temp=p2_temp.next
            p1_temp=p1_temp.next
            p2_temp=self.poly2.start
        return resPol


# pl1=PolynomialLL()
# pl1.add_term(8,2)
# pl1.add_term(-7,0)
# pl1.add_term(6,3)
# pl1.add_term(5,4)
# pl1.add_term(5,4)
# pl1.add_term(6,3)
# pl1.add_term(6,1)
# pl1.display()

# pl2=PolynomialLL()
# pl2.add_term(-7,0)
# pl2.add_term(6,3)
# pl2.add_term(5,4)
# pl2.add_term(-2,5)
# pl2.add_term(5,4)
# pl2.add_term(6,3)
# pl2.display()

pl1=PolynomialLL()
pl1.add_term(10,4)
pl1.add_term(5,3)
pl1.add_term(2,2)
pl1.display()

pl2=PolynomialLL()
pl2.add_term(2,4)
pl2.add_term(3,2)
pl2.add_term(1,1)
pl2.display()

# res=AddTwoPolynomial(pl1,pl2)
# resPolynomial=res.add()
# resPolynomial.display()

res=MultiplyTwoPolynomials(pl1,pl2)
resPolynomial=res.multiply()
resPolynomial.display()
