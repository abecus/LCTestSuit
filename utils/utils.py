#%%
from alive_progress import alive_bar
import re
import lxml
import requests
from bs4 import BeautifulSoup

from utils.namesQuery import questionNamesQuery
from utils.typesQuery import questionTypesQuery
from utils.dataQuery import questionDataQuery

#%%
def nameParser(problemName):
    """
    itype: string
    
    rtype: string
    
    converts the strings same as to get feed into urls
    lowers the alphabets and replaces non alphanumerics to '-'
    """
    # this is how leet-code stores the name of problems
    problemName = re.sub('[^0-9a-zA-Z]+', '-', problemName.lower().strip())
    if not problemName[-1].isalnum():
        return problemName[:-1]
    return problemName

def getData(query):
    """
    itype: Query
      
    rtype: raw Json output
    """

    queryUrl = 'https://leetcode.com/graphql'
    raw = requests.post(queryUrl, json=query).json()
    return raw

def nameToId(problemName):
    """
    itype: string for problem name
    rtype: int as problem id
    
    """
    # it is slow due hashed string matching
    hashedProblem = hash(problemName)
    raw = getData(questionNamesQuery)
    filteredList = raw['data']['allQuestions'] 
       
    for ques in filteredList:
        # loopthrough all the questions title and 
        # match the hashes and then string
        if hash(ques['title']) == hashedProblem and ques['title']==problemName:
            return int(ques['questionFrontendId'])
    else:
        print('DidNotFound: check your problem name')
        return None

def idToName(problemId):
    """
    itype: int as problem id 
    rtype: string for problem name
    
    """
    if problemId<=0:
        print('DidNotFound: problemId is greater than 0')
        return None
    
    # it is slow due hashed string matching
    raw = getData(questionNamesQuery)
    filteredList = raw['data']['allQuestions'] 
       
    for ques in filteredList:
        # loopthrough all the questions questionFrontendId and match
        if int(ques['questionFrontendId'])==problemId:
            return ques['title']
    else:
        print('DidNotFound: check your problemId')
        return None
    
#%%
def getContents(problemName='two sum'):
    # print(problemName)
    """
    #### itype: string (Question Name)
    #### rtype: None (py file with contents (problem description) written on it)
    
    if Question is not a paid question then the file will be created
    else no file will be created 
    """
    rawName = problemName
    with alive_bar(3) as bar:
        bar(f"Searching Problem: {rawName}...")
        problemName = nameParser(problemName)
        bar(f"Searched Problem: {problemName}")
        
        query = questionDataQuery(problemName)
        raw = getData(query)

        if "errors" in raw:
            bar("Didn't Got Contents Successfully")
            print("No problem exist with given index/name, Try Changing Index to Name (Taken from url)")
            return None
        
        filteredDict = raw['data']['question']
        if 'isPaidOnly' in filteredDict and filteredDict['isPaidOnly']:
            bar("Didn't Got Contents Successfully")
            print('PaidContaint: Can not get problem description')
            return None
        
        bar("Got Contents Successfully")
        return filteredDict
