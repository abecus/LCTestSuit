from utils.utils import *
from utils.textJustification import textJustification
import os.path
from itertools import islice


def __prettifyExamples(examples):
    for line in examples.split("\n"):
        line.strip()
        if line and line[0].isupper():
            if "Example" in line:   yield "\n"+line
            elif line.find(":")<10: yield line+"\n"
        else:   yield line

def __justifycontent(content):
    startIdx = content.find("Example")
    return "\n".join(textJustification(content[:startIdx].replace("\n", " "),
                        lineWidth=80)) + "\n\n" + \
                        "".join(__prettifyExamples(content[startIdx:]))+"\n"

def __prettifyContent(content):
    # returns html without tags with indentation
    soup = BeautifulSoup(content, 'html.parser').text
    return __justifycontent(soup)

def __strToObject(string):
    # evaluates the string to python object
    return eval(string.replace('null', 'None'))

def __findAttr(s, i):
    """gone back till a namespace and returns the word in between"""
    l = ""
    i-=1
    while s[i]!=" ":
        l = "".join((l, s[i]))
        i-=1
    return l[::-1]

def __pyDefinition(s):
    """extracts def line with no extra definitions or types for Python
    unlike how leetcode does"""
    l = ''
    attr = [] 
    i=0
    length = len(s)
    while i<length and i!=')':
        if s[i]=='(':   defName = __findAttr(s, i) # get func name
            
        if s[i]==':':
            # get a attribute form going back-ward
            attr.append(__findAttr(s, i))
            
            while s[i]!="," and s[i]!=')':
                i+=1
                if i>=length:   break
                
        l = "".join((l, s[i]))
        if s[i]==')': break
        i+=1
        
    l = "".join((l, ':'))
    return l.replace('self, ', ''), attr, defName

def __CppDefinition(s):
    """solution class def line"""
    # TODO above for cpp
    l = ''
    attr = [] 
    i=0
    length = len(s)
    while i<length and i!=')':
        if s[i]=='(':   defName = __findAttr(s, i) # get func name
            
        if s[i]==':':
            # get a attribute form going back-ward
            attr.append(__findAttr(s, i))
            
            while s[i]!="," and s[i]!=')':
                i+=1
                if i>=length:   break
                
        l = "".join((l, s[i]))
        if s[i]==')': break
        i+=1
        
    l = "".join((l, ':'))
    return l.replace('self, ', ''), attr, defName

def __quesToText(ProblemName, language='Python3', forWhat="write"):
    extensions = {'Python3':'.py',
                  'C++': '.cpp'
                  }
    raw = getContents(ProblemName) # get all raw contents to be displayed or written

    if not raw:
        print("No changes has been made")
        return

    # getting file name for script file
    questionId = raw['questionFrontendId']
    fileName = raw['title'].split(' ')+[questionId]+[extensions[language]]
    fileName[0]=fileName[0].lower()
    
    # preprocessing for future calls (dependent variables) e.g. accRate depends on stats
    codeSnippets_raw = [i['code'] for i in raw['codeSnippets'] if i['lang']==language][0]
    stats = __strToObject(raw['stats'])
    topicTags = set(i['name'] for i in raw['topicTags'])
    solution = 'Available' if raw['solution'] else None
    
    # main sections are created here
    similarQuestions =  [(i['title'], i["difficulty"]) for i in __strToObject(raw['similarQuestions'])]
    sampleTestCase = raw['sampleTestCase'].split('\n')
    definition, attrs, funcName = __pyDefinition(codeSnippets_raw.split('\n')[-2].strip(' '))
    fileName = ''.join(fileName)
    titleAndId = '_'*25+ questionId+'. '+raw['title']+'_'*25+'\n'
    meta_def = codeSnippets_raw.split('class Solution:\n')[0]
    content = __prettifyContent(raw['content'])   
    metaData = "Difficulty: "+ raw['difficulty']+\
                "\t\tLikes: "+ str(raw["likes"])+\
                "\t\tDislikes: "+ str(raw['dislikes']) +\
                "\t\tSolution: "+ str(solution)+\
                '\n'
    accRate = 'Total Accepted: '+stats['totalAccepted']+\
                '\t\tTotal Submission: '+stats['totalSubmission']+\
                '\t\tAcceptance Rate: '+stats['acRate']+'\n'
    tags =  'Tags:  '+', '.join(i for i in topicTags)+'\n'

    if forWhat == 'write':
        return fileName, titleAndId, metaData, accRate, tags, content, meta_def,\
                definition, attrs, sampleTestCase, funcName, similarQuestions
    else:
        return titleAndId, metaData, accRate, tags, content, meta_def,\
                definition, attrs, sampleTestCase, funcName, similarQuestions

def writeFile(problemName, language, path, separate=False):
    fileName, titleAndId, metaData, accRate, tags, content, meta_def,\
    definition, attrs, sampleTestCase, funcName, similarQuestions = \
        __quesToText(problemName, language)
      
    path = path+fileName
    
    if os.path.exists(path):
        print("""Warning: File Already exists on same path""")
        while True:
            user = input("Do You Want To Continue replacing File\n (Yes or yes or 1 / No or no or 0): ")
            if user=='1' or user=='Yes' or user=='yes':
                break
            if user=='0' or user=='No' or user=='no':
                print('\nNo Files has been created')
                return 0
        
    with open(path, 'w') as f:
        # if user just want to solve problem not with definition
        if not separate:
            f.write("\"\"\"\n")
            
            # title and id
            f.write(titleAndId)
            
            # metadata and solution
            f.write(metaData)
            
            # acceptance rates
            f.write(accRate)
            
            # tags type
            f.write(tags)
            f.write('\n\n')
    
    with open(path, 'ab') as f:
        if not separate:
            # contents
            f.write(content.encode('utf-8'))
            f.write("\"\"\"\n\n\n".encode('utf-8'))
    
    with open(path, 'a') as f:       
        # Code Snippet
        if meta_def:
            f.write(meta_def+'\n')    
        f.write(definition+'\n'*7)
        
        # testFunction
        f.write("if __name__ == \"__main__\":\n")
        
        # test case
        for var, val in zip(attrs, sampleTestCase):
            f.write('\t'+var+" = "+val+'\n')
            
        f.write('\tprint('+funcName+'(')
        for attr in attrs:
            f.write(attr + ",")
        f.write(')'+')')
        f.write('\n'*3)
        
        # Similar Questions
        if not separate:
            f.write("\"\"\"\n")
            if similarQuestions:
                f.write('similarQuestions::\n')
                for q, d in similarQuestions:
                    f.write('\t\t'+q + ': '+ d+'\n')
            f.write("\"\"\"\n")
        
    print('File has been created, at '+ '\"'+path+'\"')

def display(problemName):
    titleAndId, metaData, accRate, tags, content, meta_def,\
    definition, attrs, sampleTestCase, funcName, similarQuestions = \
        __quesToText(problemName, forWhat='show')
      
    print("\"\"\"\n")
        
    # title and id
    print(titleAndId)
        
    # metadata and solution
    print(metaData)
        
    # acceptance rates
    print(accRate)
        
    # tags type
    print(tags)
    print('\n\n')
        
    # contents
    print(content)
    # print('\n')
        
    # Similar Questions
    if similarQuestions:
        print('similarQuestions::\n')
        for q, d in similarQuestions:
            print('\t\t'+q + ': '+ d+'\n')
    print("\"\"\"\n")
    
    
if __name__ == "__main__":
    display('same tree')
    # __quesToText("word break")
    # __quesToText("rectangle area")
    # __quesToText("same tree")
    # __quesToText("two sum")
    pass