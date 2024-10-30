class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def level_order(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return result

import sys

input_lines = sys.stdin.read().strip().splitlines()
C = int(input_lines[0])

results = []

for case_number in range(1, C + 1):
    N = int(input_lines[2 * case_number - 1])
    values = list(map(int, input_lines[2 * case_number].split()))
    
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)

    level_order_result = bst.level_order()

    results.append(f"Case {case_number}:")
    results.append(" ".join(map(str, level_order_result)))
    results.append("")  # linha em branco após cada caso

print("\n".join(results))