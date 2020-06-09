from functools import lru_cache
from itertools import accumulate, islice


def textJustification(text, lineWidth=80):

    if len(text)<=lineWidth:
        yield text
        return
    
    # split the word in texts in word and add extra word (calibration
    # done using trial and error)
    textList = text.split(' ')+['']
    
    # find max lineWidth
    lineWidth = max(lineWidth, *map(len, textList))
    
    # make faster to find word lengths
    accLength = [*accumulate(map(len, textList))]

    def getCost(x,y):
        # calculates the cost of words in a line 
        # from index x to y inclusive
        lw=getLen(x,y)
        return float('inf') if lw>lineWidth else pow(lineWidth-lw, 2)
    
    def getLen(x,y):
        # len of word from index x to index y inclusive using 
        # accumulate array and spaces are also counted
        if x==0:	
            return accLength[y]+y-x
        return accLength[y]-accLength[x-1]+y-x

    @lru_cache(None)
    def minimiseTextSplitCost(i):
        if i==len(textList)-1:
            # if all words are done (remember we had included "")
            return 0

        temp=float('inf')
        for k in range(i+1, len(textList)+1):
            # if its not possible to fit words from i to k-1 in one line, break
            if getLen(i,k-1) > lineWidth:
                break
            
            # split at index k and find min cost from there on
            cost = getCost(i,k-1) + minimiseTextSplitCost(k)
            if temp >= cost:
                breakPoints[i] = k
                temp = cost
                
        return temp

    # stores the split indexes
    breakPoints = [0]*len(textList)
    
    # main function which update the split indexes and finds min cost
    minimiseTextSplitCost(0)
     
    # generator for lines
    i=0
    while i<len(textList)-1:
        yield " ".join(islice(textList, i, breakPoints[i]))
        i=breakPoints[i]


if __name__ == "__main__":
    file = "test.txt"
    def getText(file):
        with open(file, "r") as f:
            return f.read()
    # text = """I am the one, the one who don't """ #need no gun to get respect upon the street"""
    text = """I am the one, the one who don't need no gun to get respect upon the street The following Dynamic approach strictly follows the algorithm given in solution of Cormen book. First we compute costs of all possible lines in a 2D table lc[][]. The value lc[i][j] indicates the cost to put words from i to j in a single line where i and j are indexes of words in the input sequences. If a sequence of words from i to j cannot fit in a single line, then lc[i][j] is considered infinite (to avoid it from being a part of the solution). Once we have the lc[][] table constructed, we can calculate total cost using following recursive formula. In the following formula, C[j] is the optimized total cost for arranging words from 1 to j. The above recursion has overlapping subproblem property. For example, the solution of subproblem c(2) is used by c(3), C(4) and so on. So Dynamic Programming is used to store the results of subproblems. The array c[] can be computed from left to right, since each value depends only on earlier values. To print the output, we keep track of what words go on what lines, we can keep a parallel p array that points to where each c value came from. The last line starts at word p[n] and goes through word n. The previous line starts at word p[p[n]] and goes through word p[n] – 1, etc. The function printSolution() uses p[] to print the solution. In the below program, input is an array l[] that represents lengths of words in a sequence. The value l[i] indicates length of the ith word (i starts from 1) in the input sequence."""
    # for t in textJustification(getText(file).replace("\n", " "), lineWidth=80):
    for t in textJustification(
            text.strip().replace("\n", " "), 
            lineWidth=50
            ):
        print(t)
        