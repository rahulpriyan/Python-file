class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("none")
    def insert_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return
        self.head=self.head.next
    def delete_last(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
L1=linkedlist()
L1.insert_end(10)
L1.insert_end(20)
L1.insert_end(30)
print("original list:")
L1.traverse()
L1.insert_begin(5)
print("after insert at beginning:")
L1.traverse()
L1.insert_begin(40)
print("after insert at end:")
L1.traverse()
L1.delete_first()
print("after delete first:")
L1.traverse()
L1.delete_last()
print("fter delete last:")
L1.traverse()