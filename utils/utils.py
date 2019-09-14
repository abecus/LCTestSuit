#%%
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
    return re.sub('[^0-9a-zA-Z]+', '-', problemName.lower().strip())

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
    """
    #### itype: string (Question Name)
    #### rtype: None (py file with contents (problem description) written on it)
    
    if Question is not a paid question then the file will be created
    else no file will be created 
    """
    problemName = nameParser(problemName)
    query = questionDataQuery(problemName)
    raw = getData(query)
    filteredDict = raw['data']['question']
    # print(filteredDict)
    
    if filteredDict['isPaidOnly']:
        print('PaidContaint: Can not get problem description')
        return None
    
    return filteredDict


#%%
# what we want
# content = 'content'
# soup = BeautifulSoup(data['data']['question'][content], 'lxml')

# #%%
# title = data['data']['question']['title']
# question =  soup.get_text().replace('\n',' ')
# print(title, '\n', question)
