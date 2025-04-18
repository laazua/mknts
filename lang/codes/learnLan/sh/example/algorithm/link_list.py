#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
链表,一种线性表
"""

class ListNode:
    """
    单向链表
    """
    def __init__(self, val):
        """
        节点
        :param val:
        """
        self.val = val
        self.next = None

    def reverse(self, head):
        """
        链表反转
        1 -> 2 -> 3 -> null, 反转变为 3 -> 2 -> 1 -> null
        访问某个节点curt.next时,要检验curt是否为null
        要把反转后的最后一个节点(即反转前的第一个节点)指向null
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


class DListNode:
    """
    双向链表,反转核心在于next和prev域的交换.注意当前节点和上一个节点的递推.
    """
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head

        return curt
