from scriptWriter import *
import sys, argparse

langs = ["C++", "Java", "Python", "Python3", "C", "C#", "JavaScript","Ruby", "Swift", "Go", "Scala", "Kotlin", "Rust", "PHP"]

usage = """
		py main.py [-h] | [-w {0,1,2}] | [-sp path] | -p integer/problem-name\n
		example:\n
			py -w 0 -p 100
			py -w 1 -p same-tree
		"""
		# or to choose language use:
		#   -l "language"

parser = argparse.ArgumentParser(description="A program for solving leetcode problems offline with various options.",
					fromfile_prefix_chars="@",
					usage=usage)

writeHelp = """
		0: Create Script File with problem statement and function at the specified path,\n
		1: Create file with function, and saperately problem statement on terminal,\n
		2: Display problem statement on terminal
	"""
parser.add_argument('-w',
					dest = "writeType",
					type=int,
					default=0,
					choices=range(0, 3),
					help=writeHelp)

parser.add_argument('-sp',
					dest = "path",
					type=str,
					help='Set path to directory were file should be created')

parser.add_argument('-p',
					dest="problem",
					type=str,
					required=True,
					help='Problem name or Problem index/number')

# parser.add_argument('-l',
# 					dest = "language",
# 					type=str,
# 					help=f"""Set Programming Languages ({langs}) for File Creation (Default:Python3)""")

args = parser.parse_args()

def cli():
	path = "C:\\Users\ABDUL BASID\Desktop\AI\ml\DS-and-Algorithms\problems\leetcode\\"
	if args.path!=None:	path = args.path

	errorMassage = """FatalError: The problem is Paid or No problem exist with given index/name"""
	lang = 'Python3'
	try:	args.problem = idToName(int(args.problem))
	except:	pass

	if args.writeType==0:
		# to just write on file
		try:	writeFile(args.problem, path=path, language=lang)
		except:	print(errorMassage)

	elif args.writeType==1:
		# for separate creation and display of problem statement and function creation
		try:
			display(args.problem,)
			writeFile(args.problem, path=path, language=lang, separate=True)
		except:	print(errorMassage)
				
	elif args.writeType==2:
		# to just display on screen
		try:	display(args.problem)
		except:	print(errorMassage)

cli()