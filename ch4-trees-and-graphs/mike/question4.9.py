# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:56:31 2021

@author: admin
"""
from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree
def initalize_find(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            sequences = combine(left, right, [node.key], sequences)
    return sequences


def combine(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first[0]
    prefix.append(head)
    results = combine(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = combine(first, second[1:], prefix, results)
    prefix.pop()
    return results


def find_recursion(bst):
    if not bst.root:
        return []

    answer = []

    def recursion(sequence, combine):
        if not len(sequence):
            answer.append(combine)
            return

        for i in range(len(sequence)):
            nextsequence = sequence[:i] + sequence[i + 1 :]
            if sequence[i].left:
                nextsequence += [sequence[i].left]
            if sequence[i].right:
                nextsequence += [sequence[i].right]
            recursion(nextsequence, combine + [sequence[i].key])

    recursion([bst.root], [])
    return answer


def treesolution():
    bst = BinarySearchTree()
    bst.addnode(20)
    bst.addnode(9)
    bst.addnode(25)
    bst.addnode(5)
    bst.addnode(12)


    sequences = initalize_find(bst)
    print(sequences)

    sequences = find_recursion(bst)
    print(sequences)


if __name__ == "__main__":
    treesolution()