from binary_trees_assignment_final import *

def biuld_tree():
    q=[TreeNode(-1)]
    i=0
    cou = 0
    while i < 30:
        temp= q[i]
        temp.left = TreeNode(cou+1)
        temp.right = TreeNode(cou+2)
        q.append (temp.left)
        q.append (temp.right)
        i+=1
        cou +=2
    return q[0]

def biuld_tree_mini():
    q=[TreeNode(-1)]
    i=0
    cou = 0
    while i < 30:
        if i %10 ==1:
            i+=1
            continue
        temp= q[i]
        if i % 2 == 0:
            temp.left = TreeNode(cou+1)
            q.append (temp.left)
        temp.right = TreeNode(cou+2)
        q.append (temp.right)
        i+=1
        cou +=2
    return q[0]


empty = None

full_terr = biuld_tree()

mini_terr = biuld_tree_mini()
trees = [empty,full_terr,mini_terr]
func = [inverse_tree,longest_zigzag,print_tree_by_rows]





tree_of_three = TreeNode(1,TreeNode(2),TreeNode(3))
print_tree_by_rows (tree_of_three)

new_tree = TreeNode(1,TreeNode(3),TreeNode(2))
print_tree_by_rows (new_tree)

print(are_mirror_trees (tree_of_three,new_tree))
print('!!!!!!!!!!!!!!!!!!!!!!')
print(print_tree_by_rows(full_terr))
print (longest_zigzag(full_terr))
print(lowest_common_ancestor(full_terr,full_terr.left.right.right.right,full_terr.left.right.right).key)