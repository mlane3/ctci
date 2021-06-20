# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:38:44 2021

@author: admin
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def addnode(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("Error")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("Error")
        return new


def example():
    t = BinaryTree()
    n1 = t.addnode(1, None)
    n2 = t.addnode(2, n1)
    n3 = t.addnode(3, n1)
    n4 = t.addnode(4, n2)
    t.addnode(5, n2)
    t.addnode(7, n3)
    t.addnode(8, n4)
    return t

    print(t.root.left.left.left.key)


if __name__ == "__main__":
    example()