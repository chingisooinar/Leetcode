/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* cur,*prev,*tempp;
    tempp=prev=NULL;
    if (head==NULL)return head;
    cur=head;
    int temp=cur->val;
    int check=0;
    while(cur!=NULL){
        tempp=cur;
        cur=cur->next;
        if(cur==NULL)break;
        if(cur->val!=temp){
            temp=cur->val;
            prev=tempp;
        }else{
            if(tempp==head)head=cur;
            free(tempp);
            while(cur!=NULL && cur->val==temp){
                tempp=cur;
                cur=cur->next;
                if(tempp==head)head=cur;
                free(tempp);
            }
            if(cur!=NULL)temp=cur->val;
            if(prev!=NULL)prev->next=cur;
            
        }      
    }
    return head;
    

}
