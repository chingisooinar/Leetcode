/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode* cur, *prev;
    int temp=0;
    if(head==NULL)return head;
    cur=head->next;
    prev=head;
    while(prev!= NULL && cur!=NULL){
        printf("%d %d ",cur->val,prev->val);
        temp=cur->val;
        cur->val=prev->val;
        prev->val=temp;
        printf("(%d %d) ",cur->val,prev->val);
        prev=prev->next->next;
        if(prev!=NULL)cur=cur->next->next;
    }
    return head;
    
}
