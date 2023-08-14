class create_list:
    def __init__(self,ls=[]):
        self.data=[]
        if ls==[]:
            self.size=int(input("Enter size of the list : "))
            for i in range(self.size):
                self.data.append(int(input("Enter item for position {} : ".format(i+1))))
        else:
            self.data=ls
            self.size=len(ls)
    def display(self):
        print(self.data)
    def linearSearch(self,key):
        ind = 0
        while ind<self.size:
            if(self.data[ind]==key):
                return ind
            ind+=1
        return -1
    def binarySearch(self,key):
        # if not self.data.isAscending():
        sorted(self.data)
        low=0
        high=self.size-1
        while(low<=high):
            mid=(low+high)//2
            if self.data[mid]==key:
                return mid
            elif self.data[mid]<key:
                low=mid+1
            else:
                high=mid-1
        return -1
    
if __name__=="__main__":
    ob=create_list([1,12,14,15,3])
    print(ob.binarySearch(12))
    