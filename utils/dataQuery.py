def questionDataQuery(problemName):
    """
    #### itype: string (Question Name, formate: all lowercase and spaces replaced with '-')
    
    #### rtype: json formated query
    """
    
    Query = {
        "operationName": "questionData",
        "variables": {"titleSlug": problemName},
        "query": """query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        content
        isPaidOnly
        difficulty
        likes
        dislikes
        similarQuestions
        topicTags {
        name
        }
        codeSnippets {
        lang
        code
        }
        stats
        solution {
        canSeeDetail
        }
        sampleTestCase
    }
    }
    """
    }

    return Query
    