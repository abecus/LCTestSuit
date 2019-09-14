# pass data entries as a dict key in jsonData['data']['question']
data = ['questionId', #int
        'questionFrontendId', #int
        'title', # str
        'content', # html
        'isPaidOnly', # bool
        'difficulty', # str
        'likes', # int
        'dislikes', # int
        'similarQuestions', # list
        'topicTags', # [{'name': 'Tree',     'slug': 'tree',     
                    # {'name': 'Depth-first Search'}]
                    
        'codeSnippets', # list with dicts iterate through all the entry and check the lang
                        # {'lang': 'Python3',
                        # 'code': '# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, x):\n#         self.val = x\n#         self.left = None\n#         self.right = None\n\nclass Solution:\n    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:\n        '},                        
                        
        'stats', # dict '{"totalAccepted": "416.2K", 
                # "totalSubmission": "820.6K", 
                # "totalAcceptedRaw": 416214, 
                # "totalSubmissionRaw": 820635, 
                # "acRate": "50.7%"}',
        
        'solution', # dict
                    # {'canSeeDetail': True}
        'sampleTestCase', # str, A testcase
        ]


{'data': 
        {'question': 
                {'questionId': '100',
                'questionFrontendId': '100',
                'title': 'Same Tree',
                'content': '<p>Given two binary trees, write a function to check if they are the same or not.</p>\r\n\r\n<p>Two binary trees are considered the same if they are structurally identical and the nodes have the same value.</p>\r\n\r\n<p><strong>Example 1:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong>     1         1\r\n          / \\       / \\\r\n         2   3     2   3\r\n\r\n        [1,2,3],   [1,2,3]\r\n\r\n<strong>Output:</strong> true\r\n</pre>\r\n\r\n<p><strong>Example 2:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong>     1         1\r\n          /           \\\r\n         2             2\r\n\r\n        [1,2],     [1,null,2]\r\n\r\n<strong>Output:</strong> false\r\n</pre>\r\n\r\n<p><strong>Example 3:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong>     1         1\r\n          / \\       / \\\r\n         2   1     1   2\r\n\r\n        [1,2,1],   [1,1,2]\r\n\r\n<strong>Output:</strong> false\r\n</pre>\r\n',
                'isPaidOnly': False,
                'difficulty': 'Easy',
                'likes': 1298,
                'dislikes': 43,
                'similarQuestions': '[]',
                'topicTags': [{'name': 'Tree'}, {'name': 'Depth-first Search'}],
                'codeSnippets': [
                {'lang': 'Python3',
                'code': 
                        """
                        # Definition for a binary tree node.\n
                        # class TreeNode:\n
                        #     def __init__(self, x):\n
                        #         self.val = x\n
                        #         self.left = None\n
                        #         self.right = None\n\n
                        
                        # class Solution:\n
                        #     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:\n
                        """
                }],
                'stats': '{"totalAccepted": "416.4K", "totalSubmission": "820.9K", "totalAcceptedRaw": 416393, "totalSubmissionRaw": 820922, "acRate": "50.7%"}',
                'solution': {'canSeeDetail': True},
                'sampleTestCase': '[1,2,3]\n[1,2,3]'}
        }
}

"if __name__ == \"__main__\":"
        
    