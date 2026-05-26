/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution 
{
    public ListNode reverseList(ListNode head) 
    {
        if(head == null || head.next == null)
        {
            return head;
        }
        Stack<Integer> stack = new Stack<Integer>();
        ListNode current = head;
        while(current != null) 
        {
            stack.push(current.val);
            current = current.next;
        }
        ListNode newHead = new ListNode(stack.pop());
        current = newHead;
        while(!stack.isEmpty())
        {
            current.next = new ListNode(stack.pop());
            current = current.next;
        }
        return newHead;
    }
}
