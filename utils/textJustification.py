import itertools
import functools
import math


def textJustification(words, l):
    # converting words into array of words
    words = words.split(' ')
    parent = {}
    accumulated_Length = [0]+[*itertools.accumulate(map(len, words))]

    def getLength(i, j):
        # returns the length of word from including spacing between them
        return accumulated_Length[j+1] - accumulated_Length[i] + j - i

    def computeCost(lineWidth, wordsLength):
        # coputes the cost functions which has to be minimized
        return pow(lineWidth - wordsLength, 3)

    @functools.lru_cache(None)
    def foo(i):
        if i == len(words):
            # no word remains
            return 0

        cost = math.inf
        for j in range(i, len(words)):
            wordLength = getLength(i, j)

            # check if words can fit in the a line
            if wordLength > l:
                break

            # compute cost for remaining suffix array
            suffixCost = foo(j + 1)
            currCost = computeCost(l, wordLength)

            # minimise the cost and mainted parent accordingly
            if currCost + suffixCost < cost:
                cost = currCost + suffixCost
                parent[i] = j
        return cost

        # calling main function
    foo(0)

    def joinWords(i, j):
        # prettifies the words in from index [i, j)
        line = words[i: j]
        if len(line) == 1 or j == len(words):
            return (' '.join(line).ljust(l))
        else:
            n, r = divmod(l - (sum(map(len, line)) +
                               len(line)) + 1, len(line) - 1)
            narrow = ' ' * (n + 1)
            if r == 0:
                return narrow.join(line)
            else:
                wide = ' ' * (n + 2)
                return wide.join(line[:r] + [narrow.join(line[r:])])

    i = 0
    while i < len(words):
        t = parent[i]+1
        yield joinWords(i, t)
        i = t


if __name__ == "__main__":
    file = "test.txt"

    def getText(file):
        with open(file, "r") as f:
            return f.read()
    # text = """I am the one, the one who don't """ #need no gun to get respect upon the street"""
    text = """I am the one, the one who don't need no gun to get respect upon the street The following Dynamic approach strictly follows the algorithm given in solution of Cormen book. First we compute costs of all possible lines in a 2D table lc[][]. The value lc[i][j] indicates the cost to put words from i to j in a single line where i and j are indexes of words in the input sequences. If a sequence of words from i to j cannot fit in a single line, then lc[i][j] is considered infinite (to avoid it from being a part of the solution). Once we have the lc[][] table constructed, we can calculate total cost using following recursive formula. In the following formula, C[j] is the optimized total cost for arranging words from 1 to j. The above recursion has overlapping subproblem property. For example, the solution of subproblem c(2) is used by c(3), C(4) and so on. So Dynamic Programming is used to store the results of subproblems. The array c[] can be computed from left to right, since each value depends only on earlier values. To print the output, we keep track of what words go on what lines, we can keep a parallel p array that points to where each c value came from. The last line starts at word p[n] and goes through word n. The previous line starts at word p[p[n]] and goes through word p[n] – 1, etc. The function printSolution() uses p[] to print the solution. In the below program, input is an array l[] that represents lengths of words in a sequence. The value l[i] indicates length of the ith word (i starts from 1) in the input sequence."""
    # for t in textJustification(getText(file).replace("\n", " "), lineWidth=80):
    for t in textJustification(	text.strip().replace("\n", " "), 50):
        print(t)
