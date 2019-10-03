# LCTestSuit
A LeetCode Test Suit for offline Debugging and for Autocomplete

Automatically Script files get created with the specified file extension along with problem statement, metadata and functions defination  and testcase for solving LeetCode problems.



        -w              Write Script File
        -p              Problem Name
        -s              creates the file with function and problem statement on terminal
        -d              Display problem statement on terminal
        -i              Index of Problem
        -h              help

              To create the file write Problem Name Separated by '-' or
              index of the problem anywhere in the command line
              with -w and -p Problem Name/Problem Index

              for example:

              py -3.x -m main.py -s -i 100

run build/main.exe directly from command line e.g.      ```main.exe -w -i 100```

Change the programming language for file creation and function from scriptWriter.py in each function default is Python3
