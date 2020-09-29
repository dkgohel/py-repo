class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        newNode=Node(data)
        newNode.next=self.head
        if self.head is not None:
            self.head.prev=newNode
        self.head=newNode

    def insert_at_end(self,data):
        newNode=Node(data)
        newNode.next=None
        if self.head is None:
            newNode.prev=None
            self.head=newNode
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=newNode
        newNode.prev=itr
        return

    def printForward(self):
        itr=self.head
        strList=""
        while itr:
            strList+=str(itr.data)+"-->"
            itr=itr.next
        print(strList)
    
    def printBackward(self):
        itr=self.head
        last=itr
        strList=""
        while itr:
            last=itr
            #strList+=itr.data+"-->"
            itr=itr.next
        #print(strList)
        while last:
            strList+=str(last.data)+"-->"
            last=last.prev
        print(strList)

dl=DoublyLinkedList()
dl.insert_at_begining(8)
dl.insert_at_begining(10)
dl.insert_at_begining(12)
dl.printForward()
dl.insert_at_end(19)
dl.insert_at_end(21)
dl.printForward()
dl.insert_at_end(93)
dl.printForward()
dl.printBackward()
