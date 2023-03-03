from pystack import PythonStack
class PostfixEval:
    def __init__(self,postfix):
        self.postfixLst=postfix.split(' ')
        self.sstack=PythonStack(len(self.postfixLst))
    def getVal(self):
        for i in self.postfixLst:
            if i.isnumeric():
                self.sstack.push(i)
            elif i in ('+','-','*','/','^'):
                A=self.sstack.pop()
                B=self.sstack.pop()
                self.sstack.push(str(eval(B+i+A)))
        return self.sstack.pop()

if __name__=='__main__':
    E=PostfixEval('10 5 + 3 / 5 5 * + 4 / 8 -')
    print(E.getVal())  # -0.5
