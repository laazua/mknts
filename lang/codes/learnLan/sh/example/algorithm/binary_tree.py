#!/usr/bin/env python3
# -*- condig: utf-8 -*-
"""
二叉树是每个节点最多有两个子树的树结构,子树唷左右之分,二叉树常被用于实现二叉查找树和二叉堆.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Traversal(object):
    def __init__(self):
        self.traverse_path = list()

        def preorder(self, root):
            if root:
                self.traverse_path.append(root.val)
                self.preorder(root.left)
                self.preorder(root.right)

        def inorder(self, root):
            if root:
                self.inorder(root.left)
                self.traverse_path.append(root.val)
                self.inorder(root.right)

        def postorder(self, root):
            if root:
                self.postorder(root.left)
                self.postorder(root.right)
                self.traverse_path.append(root.val)