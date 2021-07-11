_query = """
        query allQuestions {
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
questionNamesQuery = {
    "operationName": "allQuestions",
    "variables": {},
    "query": _query
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
