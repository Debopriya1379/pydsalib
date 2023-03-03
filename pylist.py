class PythonList() :
    def __init__(self,s):
        self.lst=[0 for i in range(s)]
    def create_list(self):
        for i in range(len(self.lst)):
            self.lst[i]=int(input('Enter element : '))
    def display_list(self):
        print(self.lst)
    def linearSearch(self,item):
        i=0
        while i<self.size :
            if(self.lst[i]==item):
                return i
            i+=1
        return -1
    def binarySearch(self,item):
        l=0
        h=self.size-1
        while l<=h :
            mid=(l+h)//2
            if(self.lst[mid]==item):
                return mid
            if(item<self.lst[mid]):
                h=mid-1
            else:
                l=mid+1
        return -1
    def sum(self) :
        def getSum(l):
            if(l==[]) :
                return 0
            return l[0] + getSum(l[1:])
        return getSum(self.lst)
    def reverse(self) :
        def getReverse(l):
            if(l==[]) :
                return []
            return  getReverse(l[1:]) +[l[0]]
        return getReverse(self.lst)
    def checkPalindrome(self):
        def check(l):
            if(len(l)==1) :
                return True
            if(l[0]==l[-1]):
                return True and check(l[1:-1])
            return False
        return check(self.lst)

if __name__=='__main__' :
    a=PythonList(int(input('Enter no. of elements : ')))
    

# a=PythonList(int(input('Enter no. of elements : ')))
# a.display_list()
# a.create_list()
# a.display_list()
# print(a.sum())
# print(a.reverse())
# print(a.checkPalindrome())
# ans=a.linearSearch(int(input('Enter no. to serach :')))
# print(ans)
# ans=a.binarySearch(int(input('Enter no. to serach :')))
# print(ans)
# print(list(enumerate(l)))

# Fibonacci using recusion in O(n)
# def FibonacciEle(n,l=[0,1]):
#     if n==0 :
#         return 0
#     if n== 1:
#         return l[1]
#     return FibonacciEle(n-1,[l[1],l[0]+l[1]])

# for i in range(10):
#     print(FibonacciEle(i))


# memorising previous values
# def joyDeep(n,m=[]):
#     if n==0:
#         return m
#     return joyDeep(n-1,m+[n-1])
# print(joyDeep(4,[56,78]))
