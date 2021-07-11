#%%
import requests
from functools import lru_cache
from slugify import slugify
import os

from utils.namesQuery import questionNamesQuery
from utils.dataQuery import questionDataQuery

extensions = {"Python3": "py", "C++": "cpp"}

DATABASE_LANG = ("Oracle", "MySQL")
SHELL_LANGS = ("BASH",)

#%%
def get_files_by_ext(path: str, extention: str):
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(extention):
                yield (dirpath, file)


def nameParser(s: str) -> str:
    return slugify(s)


@lru_cache(None)
def getData(query: str) -> dict:
    json_query = eval(query)
    queryUrl = "https://leetcode.com/graphql"

    responce = requests.post(queryUrl, json=json_query)
    if responce.status_code < 400:
        return responce.json()
    else:
        return {}


def nameToId(problemName: str) -> int:
    # it is slow due hashed string matching
    hashedProblem = hash(problemName)
    raw = getData(str(questionNamesQuery))

    filteredList = raw["data"]["allQuestions"]

    # loopthrough all the questions title and
    # match the hashes and then string
    for ques in filteredList:
        if hash(ques["title"]) == hashedProblem and ques["title"] == problemName:
            return int(ques["questionFrontendId"])


def idToName(problemId: int) -> str:
    # it is slow due hashed string matching
    raw = getData(str(questionNamesQuery))
    filteredList = raw["data"]["allQuestions"]

    # print(max(map(lambda x: int(x["questionFrontendId"]), filteredList)))

    # loopthrough all the questions questionFrontendId and match
    for ques in filteredList:
        if int(ques["questionFrontendId"]) == problemId:
            return ques["title"]


#%%
def getContents(problemName: str = "two sum") -> dict:
    problemName = nameParser(problemName)
    query = str(questionDataQuery(problemName))
    raw = getData(query)

    data = raw.get("data") or {}
    filteredDict = data.get("question") or {}
    is_available = True

    if raw.get("errors", False):
        print(raw["errors"][0]["message"])
        is_available = False

    elif filteredDict.get("isPaidOnly", False):
        print("PaidContaint: Can not get problem description")
        is_available = False

    elif any(
        filter(
            lambda x: x.get("lang") in DATABASE_LANG,
            filteredDict.get("codeSnippets", []),
        )
    ):
        print("Code not supported: Skipping as its a DB question")
        is_available = False

    elif any(
        filter(
            lambda x: x.get("lang") in SHELL_LANGS, 
            filteredDict.get("codeSnippets", [])
        )
    ):
        print("Code not supported: Skipping as its a shell question")
        is_available = False

    return filteredDict, is_available or (not filteredDict=={})


#%%
if __name__ == "__main__":
    # print(nameToId("two sum"))
    s = idToName(432)
    print(getContents(s))
