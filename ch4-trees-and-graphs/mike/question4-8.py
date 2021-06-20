# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 16:25:17 2021

@author: admin
"""
from BinaryTree import BinaryTree

def fca_recursion(currentNode, node1, node2, fca_reference):
    if currentNode is None:
        return 0
    elif currentNode is node1:
        return 1
    elif currentNode is node2:
        return 2
    return_left = fca_recursion(currentNode.left, node1, node2, fca_reference)
    return_light = fca_recursion(currentNode.right, node1, node2, fca_reference)
    sum = return_left + return_light
    if sum == 3 and fca_reference[0] is None:
        fca_reference[0] = currentNode
    return sum


def first_common_ancestor(head, node1, node2):
    fca_reference = [None]  # rely on mutable list to pass a reference
    fca_recursion(head, node1, node2, fca_reference)
    return fca_reference[0]



    