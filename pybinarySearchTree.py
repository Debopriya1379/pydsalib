class Node:
    def __init__(self,val) -> None:
        self.info=val
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None
    def buildTree(self,lst):
        for item in lst:
            new_node=Node(item)
            if(self.root==None):
                self.root=new_node
            else:
                temp=self.root
                par=None
                while(temp!=None):
                    par=temp
                    if(item<temp.info):
                        temp=temp.left
                    else:
                        temp=temp.right
                if(item<par.info):
                    par.left=new_node
                else:
                    par.right=new_node
        return self.root
    def displayInorder(self,head):
        if(head==None):
            return
        self.displayInorder(head.left)
        print(head.info,' -> ',end='')
        self.displayInorder(head.right)
    def displayPreorder(self,head):
        if(head==None):
            return
        print(head.info,' -> ',end='')
        self.displayPreorder(head.left)
        self.displayPreorder(head.right)
    def displayPostorder(self,head):
        if(head==None):
            return
        self.displayPostorder(head.left)
        self.displayPostorder(head.right)
        print(head.info,' -> ',end='')
    def search(self,head,key):
        if(head==None):
            return
        if(head.info==key):
            # print('key found')
            return head
        else:
            temp=head
            while(temp!=None):
                if(temp.info==key):
                    # print('key found')
                    return temp
                elif(temp.info>key):
                    temp=temp.left
                else:
                    temp=temp.right
            # print('key not found')
            return None
    def getHeight(self,head):
        if(head==None):
            return 0
        return max(self.getHeight(head.left),self.getHeight(head.right))+1
    def getInorderSuccessor(self,head,key):
        p=self.search(head,key)
        successor=None
        while(head!=None):
            if(p.info >= head.info):
                head=head.right
            else:
                successor=head
                head=head.left
        return successor
    def deleteNode(self,head,key):
        temp=head
        par=head
        while(temp.info!=key):
            par=temp
            if(key<temp.info):
                temp=temp.left
            else:
                temp=temp.right
        if(key<par.info):                   ## deleted node is at the left subtree
            if(temp.right==None):           ## if deleted node has only left child
                child=temp.left
                del temp
                par.left=child
            elif(temp.left==None):          ## if deleted node has only right child
                child=temp.right
                del temp
                par.right=child
            elif(temp.left==None and temp.right==None): ## if deleted node has no child
                par.left=None
                del temp
            else:                           ## if deleted node has two child
                successor=self.getInorderSuccessor(head,key)
                temp2=self.search(head,key)
                # print('successor ',successor.info)
                # print('temp2 ',temp2.info)
                self.deleteNode(head,successor.info)
                temp2.info=successor.info
        else:                               ## deleted node is at the right subtree
            if(temp.right==None):           ## if deleted node has only left child
                child=temp.left
                del temp
                par.right=child
            elif(temp.left==None):          ## if deleted node has only right child
                child=temp.right
                del temp
                par.right=child
            elif(temp.left==None and temp.right==None): ## if deleted node has no child
                par.right=None
                del temp
            else:                           ## if deleted node has two child
                successor=self.getInorderSuccessor(head,key)
                temp2=self.search(head,key)
                # print('successor ',successor.info)
                # print('temp2 ',temp2.info)
                self.deleteNode(head,successor.info)
                temp2.info=successor.info

l=[50,22,10,90,80,56,34]
bst = BinarySearchTree()
root=bst.buildTree(l)
bst.displayInorder(root)
print('None')
# bst.displayPreorder(root)
# print('None')
# bst.displayPostorder(root)
# print('None')
# bst.search(root,32)
# bst.deleteNode(root,22)
# bst.displayInorder(root)
# print('None')
# temp2=bst.getInorderSuccessor(root,50)
# if(temp2!=None):print(temp2.info)
print(bst.getHeight(root))

