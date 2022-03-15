# LCTestSuit
A LeetCode Test Suit for offline Debugging and for Autocomplete

Automatically Script files get created with the specified file extension along with problem statement, metadata and functions defination  and testcase for solving LeetCode problems.



        usage:
                        py main.py [-h] | [-w {0,1,2}] | [-sp path] | -p integer/problem-name

                        example:

                                py main.py -w 0 -p 100
                                py main.py -w 1 -p same-tree


        A program for solving leetcode problems offline with various options.

        optional arguments:
          -h, --help  show this help message and exit
          -w {0,1,2}  0: Create Script File with problem statement and function at the specified path, 
                      1: Create file with function, and saperately problem statement on terminal, 
                      2: Display problem statement on terminal
          -sp PATH    Set path to directory were file should be created
          -p PROBLEM  Problem name or Problem index/number

run build/main.exe directly from command line e.g.      ```main.exe -w 0 -p 100```

Change the programming language for file creation and function from scriptWriter.py in each function default is Python3
