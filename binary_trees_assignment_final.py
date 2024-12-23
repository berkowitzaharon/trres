class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Function 1: Inverse Tree
# Write a function `inverse_tree(root)` that receives the root of a binary tree
# and makes the tree a mirror image of itself.
# Example:
# Input Tree:
#       1
#      / \
#     2   3
#
# Output Tree:
#       1
#      / \
#     3   2


def inverse_tree(root):
    if root is None:
        return
    
    root.left,root.right = root.right,root.left
    inverse_tree(root.left)
    inverse_tree(root.right)
    return root




# Function 2: Boolean Mirror Trees
# Write a function `are_mirror_trees(root1, root2)` that receives two tree roots
# and returns `True` if the trees are mirror images of each other,
# and `False` otherwise.
# Example:
# Tree 1:
#       1
#      / \
#     2   3
#
# Tree 2:
#       1
#      / \
#     3   2
# Output: True


def are_mirror_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is  None or root2 is None:
        return False
    return (root1.key == root2.key) and (are_mirror_trees (root1.left,root2.right))and (are_mirror_trees(root1.right,root2.left))



# Function 3: Longest Zigzag Path
# Write a function `longest_zigzag(root)` that receives the root of a binary tree
# and returns a list of keys along the longest zigzag path.
# A "zigzag" occurs when the path alternates directions (left -> right -> left or right -> left -> right).
# The alternations do not have to be in consecutive levels of the tree to be considered part of a zigzag.
# Example:
# Tree:
#         1
#        / \
#       2   3
#      / \    \
#     0   4     5
#        /     / \
#       6     12  7
#                 /
#                8
#               / \
#              6   9
#                   \
#                   17
#                   /
#                  10

# Longest Zigzag Path: [1, 3, 5, 7, 8, 9, 17, 10]

def longest_zigzag(root):
    if root is None:
        return []
    counter_l ,zigzags_l = _longest_zigzag (root.left , 0, "left")
    counter_r ,zigzags_r = _longest_zigzag (root.right,0,"right")
    if counter_l < counter_r:
        return  (zigzags_r+ [root.key])[::-1]
    
    return (zigzags_l+ [root.key])[::-1]

def _longest_zigzag (root, counter_zigzags =0, direcion = None):
    if root is None :
        return  counter_zigzags , []
    counter_l,zigzags_l = _longest_zigzag(root.left,counter_zigzags + int(direcion != 'left'),direcion= "left")
    counter_r,zigzags_r = _longest_zigzag(root.right,counter_zigzags + int(direcion != 'right'),direcion= "right")
    if counter_l < counter_r:
        return counter_r, zigzags_r + [root.key]
    return counter_l, zigzags_l+ [root.key]    



# Function 4: Lowest Common Ancestor
# Write a function `lowest_common_ancestor(root, node1, node2)` that receives the root of a binary tree and two nodes.
# It should return the lowest common ancestor (LCA) of the two nodes.
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
#      / \
#     8   6
#        / \
#       7   10

# LCA of 8 and 10: 5
# LCA of 6 and 4: 2
# LCA of 7 and 3: 1

def lowest_common_ancestor(root, node1, node2):
    n_1 = find_node(root,node1)
    n_2 = find_node(root,node2)
    lenght = len(n_1) if len(n_1)< len(n_2) else len(n_2)
    for j in range (0,lenght):
        if n_1[j] != n_2[j]:
            return n_1[j-1]
    return n_1[j-1]

def find_node(root,node):
    if root is None:
        return []
    if node == root:
        return[root]
    find_l = find_node (root.left,node)
    find_r = find_node (root.right,node)

    if find_l:
        return [root]+find_l
    if find_r:
        return [root]+find_r 
    return []
# Function 5: Print Tree by Rows
# Write a function `print_tree_by_rows(root)` that prints the tree level by level using a breadth-first search (BFS).
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#
# Output:
# 1
# 2 3
# 4 5 6

def print_tree_by_rows(root):
    q =[]
    if root is None:
        return q

    q.append((root, 0))
    i=0
    while i< len(q):
        
        if q[i][0].left:
            q.append((q[i][0].left, q[i][1] + 1))
        if q[i][0].right:
            q.append((q[i][0].right, q[i][1] + 1))
        i+=1
    depth = 0
    for node in q:
        node_p,dep_p = node
        if dep_p > depth:
            print()
            depth = dep_p
        print(node_p.key,end= " ")




# Instructions for Writing Tests
# Write test cases for each of the above functions. For each test:
# - Provide an example input (tree or trees for comparison).
# - Include the expected output based on the provided examples.
# - Ensure that your tests cover various edge cases, such as empty trees, single-node trees, or trees with specific structures.
# You can use helper functions to build binary trees for testing.



# Recommendation:
# To visualize binary trees, you can use the `graphviz` library. It allows you to create graphical representations of trees
# and save them as image files. This can be especially useful for debugging and understanding tree structures.
# Example:
# 1. Install Graphviz:
#    pip install graphviz
# 2. Use the following function to visualize a binary tree:

from graphviz import Digraph

def visualize_tree(root, filename="tree"):
    def add_nodes_edges(node, dot=None):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right, dot)

    dot = Digraph()
    add_nodes_edges(root, dot)
    dot.render(filename, format="png", cleanup=True)  # Save as PNG
    print(f"Tree visualization saved as {filename}.png")



