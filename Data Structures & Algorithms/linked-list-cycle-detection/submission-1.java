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
    public boolean hasCycle(ListNode head) 
    {
        HashSet<Integer> seen = new HashSet<>();
        ListNode temp = head;
        if (temp == null){
            return false;
        }
        while (temp.next != null){
            if(!seen.add(temp.val)){
                return true;
            }
            temp = temp.next;
        }
        return false;
    }
}
