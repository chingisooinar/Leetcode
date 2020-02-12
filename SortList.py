class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        cur=head
        lis=[]
        while(cur):
            lis.append(cur.val)
            cur=cur.next
        cur=head
        lis.sort()
        i=0
        while(cur):
            cur.val=lis[i]
            cur=cur.next
            i+=1
        return head
