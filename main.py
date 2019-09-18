from scriptWriter import *
import sys

mapping = {'-w':'Write Script File',
           '-p':"Problem Name",
           '-s':"create file with function and problem statement on terminal",
           '-d': 'Display problem statement on terminal',
           '-i':'Index of Problem',
           '-h':"help"
           }


def __findProblemName(args):
    name = None
    for com in args:
        # getting Problem Name/Problem Index
        if com not in mapping:
            name=com
    return name

def CLI():
    # print('in')
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
              index of the problem anywhere in command line 
              with -w and -p Problem Name/Problem Index\n
              for example:\n
              py -3.x -m main.py -s -i 100
              """
              )
        return

    if args:
        if not ('-p' in args or '-i' in args):
            print('NO -p or -i Command Was Given')
            return
            
        if '-d' in args:
            name = __findProblemName(args)
            if name:
                if not name.isdigit():
                    display(name)
                    return
                try:
                    problemName = idToName(int(name))
                    display(problemName)
                    return
                except:
                    print("""FatalError: The problem is Paid or No problem exist with given index/name""")    
                    return
            print("NO Problem Name/Problem Index Was Given")
            return
        
        if '-w' in args:
                name = __findProblemName(args)                                       
                if name:
                    if not name.isdigit():
                        writeFile(name)
                        return
                    try:
                        problemName = idToName(int(name))
                        writeFile(problemName)
                        return
                    except:
                        print("""FatalError: The problem is Paid or No problem exist with given index/name""")
                        return
                print("NO Problem Name/Problem Index Was Given")
                return
 
        if '-s' in args:
            name = __findProblemName(args)
            if name:
                if not name.isdigit():
                    display(name)
                    writeFile(name, separate=True)
                    return
                try:
                    problemName = idToName(int(name))
                    display(problemName)
                    writeFile(problemName, separate=True)
                    return
                except:
                    print("""FatalError: The problem is Paid or No problem exist with given index/name""")
                    return
            print("NO Problem Name/Problem Index Was Given")
            return
            
    print('No Argument are Passed')  

CLI()    
