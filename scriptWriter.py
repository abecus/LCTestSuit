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


def writeFile(ProblemName, language='Python3'):
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
    fileName = ''.join(fileName)
    
    # getting other parts of script file
    codeSnippets_raw = [i['code'] for i in raw['codeSnippets'] if i['lang']==language][0]
    meta_def = codeSnippets_raw.split('class Solution:\n')[0]
    definition, attrs, funcName = __definition(codeSnippets_raw.split('\n')[-2].strip(' '))
        
    stats = __strToObject(raw['stats'])
    content = __prettifyContent(raw['content'])   
    
    topicTags = set(i['name'] for i in raw['topicTags'])
    sampleTestCase = raw['sampleTestCase'].split('\n')
    solution = 'Available' if raw['solution'] else None
    similarQuestions =  [(i['title'], i["difficulty"]) for i in __strToObject(raw['similarQuestions'])]
    
    path = "problems/"+fileName
    with open(path, 'w') as f:
        f.write("\"\"\"\n")
        
        # title and id
        f.write('_'*25+ questionId+'. '+raw['title']+'_'*25+'\n')
        
        # metadata and solution
        f.write("Difficulty: "+ raw['difficulty']+\
                "\t\tLikes: "+ str(raw["likes"])+\
                "\t\tDislikes: "+ str(raw['dislikes']) +\
                "\t\tSolution: "+ str(solution)+\
                '\n')
        
        # acceptance rates
        f.write('Total Accepted: '+stats['totalAccepted']+\
                '\t\tTotal Submission: '+stats['totalSubmission']+\
                '\t\tAcceptance Rate: '+stats['acRate']+'\n')
        
        # tags type
        f.write('Tags:  '+', '.join(i for i in topicTags)+'\n')
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
        f.write("\"\"\"\n")
        if similarQuestions:
            f.write('similarQuestions::\n')
            for q, d in similarQuestions:
                f.write('\t\t'+q + ': '+ d+'\n')
        f.write("\"\"\"\n")
    print('File has been created, at '+ '\"'+path+'\"')


name = idToName(931)
writeFile(name)