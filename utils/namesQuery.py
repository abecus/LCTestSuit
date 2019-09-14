questionNamesQuery = {
    "operationName": "allQuestions",
    "variables": {},
    "query": """query allQuestions {
  allQuestions {
    ...questionSummaryFields
  }
}

fragment questionSummaryFields on QuestionNode {
  title
  questionFrontendId
  difficulty
  isPaidOnly
}
"""
}


# {'data': 
#   {'allQuestions':
#     [
#       {'title': 'Two Sum',
#       'questionFrontendId': '1',
#       'difficulty': 'Easy',
#       'isPaidOnly': False},
     
#       {'title': 'Add Two Numbers',
#     'questionFrontendId': '2',
#     'difficulty': 'Medium',
#     'isPaidOnly': False}
#     ]
#   }
# }
