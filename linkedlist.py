class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    """ Node class
        
            up
             |
    left - data - right
             |
           down
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None


head = ListNode(0)

curr_node = head

new_node = ListNode(1)
curr_node.next = new_node
curr_node=curr_node.next

curr_node.next = ListNode(2)
curr_node=curr_node.next

curr_node.next = ListNode(3)
curr_node=curr_node.next

curr_node.next = ListNode(4)
curr_node=curr_node.next

node=head
while node:
    print(node.val)
    node=node.next

#ㅎㅇ
asdflajsdf;ljadsf;lkjakdfl

#이준영 바보, 정희원 바보, 최유찬 바보.
#jun branch 내용 변경
#PR 연습
#제발 돼라-최유찬