from utils.utils import *


def __prettifyContent(content):
    # returns html without tags with indentation
    soup = BeautifulSoup(content, 'html.parser').text
    return soup

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

def __definition(s):
    """extracts def line with no extra definitions or types
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


def __quesToText(ProblemName, language='Python3', forWhat="write"):
    extensions = {'Python3':'.py',
                  'cpp': '.cpp'
                  }
    raw = getContents(ProblemName)

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
    definition, attrs, funcName = __definition(codeSnippets_raw.split('\n')[-2].strip(' '))
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

def writeFile(problemName, language='Python3', path='C:\\Users\\ABDUL BASID\\Desktop\\AI\\ml\\DS-and-Algorithms\\problems\\leetcode\\', separate=False):
    fileName, titleAndId, metaData, accRate, tags, content, meta_def,\
    definition, attrs, sampleTestCase, funcName, similarQuestions = \
        __quesToText(problemName, language)
      
    path = path+fileName
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
            
            # contents
            f.write(content)
            f.write("\"\"\"\n\n\n")
            
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

def display(problemName, language='Python3'):
    titleAndId, metaData, accRate, tags, content, meta_def,\
    definition, attrs, sampleTestCase, funcName, similarQuestions = \
        __quesToText(problemName, language, forWhat='show')
      
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
    
# display('two sum', language='Python3')