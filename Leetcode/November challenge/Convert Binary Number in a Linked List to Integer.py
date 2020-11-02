'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
'''


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        j = []
        
        def trav(node):
            if not node:
                return 
            else:
                j.append(node.val)
                trav(node.next)
        
        trav(head)
        
        count = 0
        for i in range(len(j)):
            count+= (2**i) * j[-i-1]
        
        
        return count

            
            
