from typing import List, Tuple
from utils.scriptWriter import *
from utils.utils import get_files_by_ext
import argparse


langs = [
	"C++",
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

usage = """
		py main.py [-h] | [-w {0,1,2}] | [-sp path] | -p integer/problem-name\n
		example:\n
			py -w 0 -p 100
			py -w 1 -p same-tree
		"""
# or to choose language use:
#   -l "language"

parser = argparse.ArgumentParser(
	description="A program for solving leetcode problems offline with various options.",
	fromfile_prefix_chars="@",
	usage=usage,
)

writeHelp = """
		0: Create Script File with problem statement and function at the specified path,\n
		1: Create file with function, and saperately problem statement on terminal,\n
		2: Display problem statement on terminal
	"""
parser.add_argument(
	"-w", dest="writeType", type=int, default=0, choices=range(0, 3), help=writeHelp
)

parser.add_argument(
	"-sp",
	dest="path",
	type=str,
	help="Set path to directory were file should be created",
)

parser.add_argument(
	"-p",
	dest="problem",
	type=str,
	required=True,
	help="Problem name or Problem index/number",
)

# parser.add_argument('-l',
# 					dest = "language",
# 					type=str,
# 					help=f"""Set Programming Languages ({langs}) for File Creation (Default:Python3)""")

args = parser.parse_args()


def get_user_confirmation_for_file_exists(matchedFiles: List[Tuple[str, str]]) -> None:
	print("""\nWarning: Similar file already exists on same path with file Names as:""")
	for i, f in enumerate(matchedFiles, 1):
		file_path, file_name = f
		print(f"{i}. {file_name}    at {file_path}/{file_name}")
	print()
	while True:
		user = input(
			"Do You Want To Continue replacing File\n (Yes or yes or 1 / No or no or 0): "
		)
		if user == "1" or user == "Yes" or user == "yes":
			break

		if user == "0" or user == "No" or user == "no":
			print("\nNo Files have been created")
			return 0


def check_match_file_at_path(path: str, problem:str) -> None:
	if not problem.isnumeric():
		problem = "".join(
			[
				s.lower() if i == 0 else s.title()
				for i, s in enumerate(problem.split("-"))
			]
		)

	matchedFiles = list(
		filter(
			lambda f: problem in f[1],
			((fp, fn) for fp, fn in get_files_by_ext(path, ".py")),
		)
	)

	if matchedFiles:
		get_user_confirmation_for_file_exists(matchedFiles)


def cli():
	path = "/Users/asalam/vscode/LCTestSuit/problems"
	if args.path != None:
		path = args.path

	lang = "Python3"

	question_name: str = args.problem
	question_name = idToName(int(question_name)) if question_name.isnumeric() else nameParser(question_name)

	check_match_file_at_path(path, question_name)

	if args.writeType == 0:
		# to just write on file
		writeFile(question_name, path=path, language=lang)

	elif args.writeType == 1:
		# for separate creation and display of problem statement and function creation
		display(args.problem)
		writeFile(question_name, path=path, language=lang, separate=True)

	elif args.writeType == 2:
		# to just display on screen
		display(question_name)


cli()
