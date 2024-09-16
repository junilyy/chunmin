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
#git add 하고 싶어요..
#언터쳐블 밖