questionTypesQuery = {
    "operationName": "questionTags",
    "variables": {"skipCompanyTags": True},
    "query": """query questionTags($skipCompanyTags: Boolean = false) {
  questionTopicTags {
    edges {
      node {
        name
        questionIds
      }
    }
  }
  questionCompanyTags @skip(if: $skipCompanyTags) {
    edges {
      node {
        name
        questionIds
      }
    }
  }
}
"""
}



# {'data': 
#   {'questionTopicTags':
#     {
#       'edges': 
#         [
#           {'node': {'name': 'Rolling Hash', 'questionIds': [1251]}},
#           {'node': {'name': 'Suffix Array', 'questionIds': [1133]}}
#         ]
#     }    
#   }
# }
