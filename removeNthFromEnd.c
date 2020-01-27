/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    printf("%d",head->val);
    struct ListNode* cur, *del,*prev;
    cur=head;
    del=head;
    prev=NULL;
    int val=n-1;
    int count=0;
    while(cur->next!=NULL){
        if(count>=val){
            prev=del;
            del=del->next;
        }
        cur=cur->next;
        if(val!=0)count++;
    }
    if(prev!=NULL)prev->next=del->next;
    else{
        head=head->next;
    }
    free(del);
    return head;
}
