import pystack 
class InfixToPostfix:
    def __init__(self,infx:str):
        self.infixLst=infx.split(' ')
        self.sstack=pystack.PythonStack(len(self.infixLst))
        self.postfixExp=''
    def displayInfixList(self):
        for i in self.infixLst:
            if i.isalpha():
                print(i,' is operand')
            elif i == '+' or i=='-' or i=='*' or i=='/':
                print(i, ' is operator')
            elif i == '(':
                print(i, ' is left paranthesis')
            elif i == ')':
                print(i, ' is right paranthesis')
    def getPrecedence(self,opr):
        if(opr=='+' or opr=='-'):
            return 2
        elif(opr=='*' or opr=='/'):
            return 1
        elif (opr=='^'):
            return 0
    def getPostfix(self):
        for i in self.infixLst:
            if i== '(':
                self.sstack.push(i)
            elif i.isalpha():
                self.postfixExp+=i+' '
            elif i== ')':
                while(self.sstack.peek()!=None and self.sstack.peek() != '(' ):
                    self.postfixExp+=self.sstack.pop()+' '
                self.sstack.pop()
            elif i in ('+','-','*','/','^'):
                currOpPrec=self.getPrecedence(i)
                peekOpPrec=self.getPrecedence(self.sstack.peek())
                while(self.sstack.peek()!=None and peekOpPrec!=None and peekOpPrec<=currOpPrec ):
                    self.postfixExp+=self.sstack.pop()+' '
                    peekOpPrec=self.getPrecedence(self.sstack.peek())
                self.sstack.push(i)
        while(self.sstack.peek()!=None):
            self.postfixExp+=self.sstack.pop()+' '
        return self.postfixExp

            
if __name__=='__main__' :
    A=InfixToPostfix('A + (( B - C ^ Z ) / D + )E * F')
    print(A.getPostfix())