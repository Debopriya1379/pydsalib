class PythonStack():
    def __init__(self,s):
        self.lst=[0 for i in range(s)]
        self.size=s
        self.__top=-1
    def push(self,item):
        if(self.__top==self.size-1):
            print('Stack overflowed')
            return 
        self.__top+=1
        self.lst[self.__top]=item
    def pop(self):
        if(self.__top==-1):
            # print('Stack is empty')
            return -1
        item=self.lst[self.__top]
        self.__top-=1
        return item
    def peek(self):
        if(self.__top == -1):
            return
        return self.lst[self.__top]
    def display(self):
        if(self.__top==-1):
            print('Stack is empty')
            return
        for i in range(self.__top,-1,-1):
            print(self.lst[i])

if __name__=='__main__' :
    A=PythonStack(5)
    

# A.push(3)
# A.push(5)
# A.push(8)
# A.push(9)
# A.push(0)
# A.push(10)
# print(A.peek())
# print()
# print(A.pop())
# print()
# A.display()