// https://leetcode.com/problems/add-two-numbers/description/
class ListNode(
    var `val`: Int
) {
    var next: ListNode? = null
}

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val dummy = ListNode(0)

        var node1 = l1
        var node2 = l2
        var currentNode = dummy
        var carry = 0

        while (node1 != null || node2 != null || carry != 0) {
            val sum = (node1?.`val` ?: 0) + (node2?.`val` ?: 0) + carry
            val next = ListNode(sum % 10)
            carry = sum / 10

            currentNode.next = next
            currentNode = next

            node1 = node1?.next
            node2 = node2?.next
        }

        return dummy.next
    }
}
