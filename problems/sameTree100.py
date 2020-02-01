"""
_________________________100. Same Tree_________________________
Difficulty: Easy		Likes: 1608		Dislikes: 49		Solution: Available
Total Accepted: 473.7K		Total Submission: 916.9K		Acceptance Rate: 51.7%
Tags:  Depth-first Search, Tree


Given two binary trees, write a function to check if they are the
same or not. Two binary trees are considered the same if they
are structurally identical and the nodes have the same value. 


Example 1:Input:     1         1
          / \       / \         2   3     2   3        [1,2,3],   [1,2,3]Output: true

Example 2:Input:     1         1
          /           \         2             2        [1,2],     [1,null,2]Output: false

Example 3:Input:     1         1
          / \       / \         2   1     1   2        [1,2,1],   [1,1,2]Output: false

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isSameTree(p, q):






if __name__ == "__main__":
	p = [1,2,3]
	q = [1,2,3]
	print(isSameTree(p,q,))


"""
"""
