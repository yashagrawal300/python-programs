'''
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

'''


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        j = []
        
        k = head
        
        
        while k:
            j.append(k.val)
            k = k.next
        
        j.sort()

        
        head = ListNode(0)
        ptr = head
        
                
        for i in j:
            newNode = ListNode(i)
            ptr.next = newNode
            ptr = ptr.next
            
        return head.next
