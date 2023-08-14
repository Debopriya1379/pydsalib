class PythonStack():
    def __init__(self,size=10):
        self.lst=[0 for i in range(size)]
        self.size=size
        self.__top=-1
    def push(self,item):
        if(self.__top==self.size-1):
            print('Stack overflowed')
            return 
        self.__top+=1
        self.lst[self.__top]=item
    def pop(self):
        if(self.__top==-1):
            print('Stack is empty')
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
        # for i in range(self.__top,-1,-1):  ## top to last element
        #     print(self.lst[i])
        for i in range(self.__top+1):  ## last element to top
            print(self.lst[i])

# if __name__=='__main__' :
#     ob=PythonStack(10)
#     ob.push(3)
#     ob.push(5)
#     ob.push(8)
#     ob.push(9)
#     ob.display()
# ob.push(0)
# ob.push(10)
# print(ob.peek())
# print()
# print(ob.pop())
# print()
# ob.disploby()