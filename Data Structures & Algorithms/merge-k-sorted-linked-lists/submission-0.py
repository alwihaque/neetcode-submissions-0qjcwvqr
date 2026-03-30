# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: ListNode, list2: ListNode):
            head = ListNode()
            l1, l2 = list1, list2
            node = head
            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next                    
            if l1:
                node.next = l1
            else:
                node.next = l2
            
            return head.next
        

        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_list.append(mergeTwoLists(l1,l2))
            lists = merged_list
        
        return lists[0]
        
        
        
        
                

        