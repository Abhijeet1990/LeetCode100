class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        # the idea is to convert the linked list to a string and reverse it to get the integer
        # add the two number and again reverse it as a string and store in another linked list and return
        f1 = ''
        f2 = ''
        while l1:
            f1 += str(l1.val)
            l1 = l1.next

        while l2:
            f2 += str(l2.val)
            l2 = l2.next

        f1_i = int(f1[::-1])
        f2_i = int(f2[::-1])

        res = f1_i + f2_i

        # reverse it as a string and store in another linked list and return
        res_s = str(res)[::-1]
        return self.createLinkedList(res_s)

    def createLinkedList(self,valString):
        # insertion into linked-list
        head = prev = None

        for ch in valString:
            node = ListNode(int(ch))
            #print(node.val)
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev

        return head


n1 = 564
n2 = 243

l = ListNode()

L1 = l.createLinkedList(str(n1))
L2 = l.createLinkedList(str(n2))

res = l.addTwoNumbers(L1,L2)

res_s = ''
while res:
    res_s+=str(res.val)
    res = res.next

print('Sum of {} and {} is : {} '.format(str(n1),str(n2),res_s[::-1]))


