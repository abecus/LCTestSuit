from scriptWriter import *
import sys

langs = ["C++", 
"Java", 
"Python", 
"Python3", 
"C", 
"C#", 
"JavaScript",
"Ruby", 
"Swift", 
"Go", 
"Scala", 
"Kotlin", 
"Rust", 
"PHP", 
]

mapping = {'-w':'Write Script File',
           '-h':"help",
           '-p':"Problem Name",
           '-s':"Create file with function and problem statement on terminal",
           '-d': 'Display problem statement on terminal',
           '-i':'Index of Problem',
           "-sp": 'Set path to directory were file should be created',
        #    "l": f"""Set Programming Languages
        #                 ({langs}) for File Creation (Default:Python3)"""
           }

def __findProblemName(args):
    name = None
    if '-p' in args:
        idx = args.index('-p')+1
    else:
        idx = args.index('-i')+1
    name = args[idx]
    return name

def __getPath(args):
    path = None
    idx = args.index('-sp')+1
    path = args[idx]
    return path

def __getLang(args):
    lang = None
    idx = args.index('-l')+1
    lang = args[idx]
    return lang

def CLI():
    try:
        args = sys.argv[1:]
    except: 
        print('No Argument are Passed')  
        return
    
    if '-h' in args:
        for c, m in mapping.items():
            print('\t'+c+'\t\t'+m, end='\n')
        print("""
            To create file write Problem Name Saperated by '-' or
            index of the problem after -i/-p in command line
            with -w and -p Problem Name/Problem Index.
              for example:
              py -3.x -m main.py -s -i 100\n
            To set Path of file:
              py -3.x -m main.py -s -i 100 -sp "path" 
              """
            # or to choose language use:
            #   -l "language"
              )
        return

    if args:
        lang = 'Python3'
        path = "C:\\Users\ABDUL BASID\Desktop\AI\ml\DS-and-Algorithms\problems\leetcode\\"    # default path 
        
        if not ('-p' in args or '-i' in args):
            print('NO -p or -i Command Was Given')
            return
        
        if '-sp' in args:
            # get path form CLI
            tp = __getPath(args)
            if tp:
                if tp[-1]!='\\':
                    tp += '\\'
                path = tp
        
        name = __findProblemName(args)  # extract the name or id of problem
        if not name:
            print("NO Problem Name/Problem Index Was Given")
            return
        
        if '-l' in args:
            # get language form CLI
            tl = __getLang(args)
            if tl:
                lang=tl
                
        if '-d' in args:
            # to just display on screen
            if not name.isdigit():
                display(name)
                return
            try:
                problemName = idToName(int(name))
                display(problemName)
            except:
                print("""FatalError: The problem is Paid or No problem exist with given index/name""")    
            return
        
        if '-w' in args:
            # to just write on file
            if not name.isdigit():
                writeFile(name, path=path, language=lang)
                return
            try:
                problemName = idToName(int(name))
                
                writeFile(problemName, path=path, language=lang)
            except:
                print("""FatalError: The problem is Paid or No problem exist with given index/name""")
            return
                
        if '-s' in args:
            if not name.isdigit():
                display(name)
                writeFile(name, path=path, language=lang, separate=True)
                return
            try:
                problemName = idToName(int(name))
                display(problemName)
                writeFile(problemName, language=lang, separate=True)
            except:
                print("""FatalError: The problem is Paid or No problem exist with given index/name""")
            return
            
    print('No Argument are Passed')  

CLI()    
