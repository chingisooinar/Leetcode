/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    struct ListNode* cur=head,*temp=NULL,*prev=NULL;
    if(head==NULL || k==0)return head;
    int len=1;
    while(cur->next!=NULL){
        cur=cur->next;
        len++;
    }
    k=k%len;
    cur=head;
    temp=head;
    if(cur->next!=NULL){
    while(k){
        prev=cur;
        cur=cur->next;
        if(cur->next==NULL){
            cur->next=temp;
            temp=cur;
            prev->next=NULL;
            k--;
        }
    }
    }

    return cur;

}
