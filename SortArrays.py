from typing import Optional
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{{'value': {self.value}, 'next': {self.next}}}"


def AddNode(anteriornode,value):
    newnode = ListNode(value)
    anteriornode.next = newnode
    return(newnode)

def DecodeNode(node):
    XD = []
    while node != None:
        print(node.value)
        XD.append(node.value)
        node = node.next
    return(XD)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1,list2, "LOLLLLLLL")

        list1 = DecodeNode(list1)
        list2 = DecodeNode(list2)
        resultedlist = sorted(list1+list2)
        resultnode = ListNode(resultedlist[0])
        a = resultnode
        for i in resultedlist[1:]:
            a = AddNode(a,i)
        
    

        return(resultnode)
        

head = ListNode(1)

a = head
for i in [2,3,4,5]:
    a = AddNode(a,i)


a = head


# a = AddNode(head,2)
# AddNode(a,5)
print("lol:",head.next)
print("total head:",head )



DecodeNode(a)







# print(a.value)
# print(b.value)
# print(c.value)

node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

x = Solution().mergeTwoLists(ListNode(None), a)
