from utils.utils import *
from utils.textJustification import textJustification
from bs4 import BeautifulSoup
from pathlib import Path


def __prettifyExamples(examples):
    for line in examples.split("\n"):
        line.strip()
        if line and line[0].isupper():
            if "Example" in line:
                yield "\n" + line
            elif line.find(":") < 10:
                yield line + "\n"
        else:
            yield line


def __justifycontent(content):
    startIdx = content.find("Example")
    return (
        "\n".join(
            "\n".join(textJustification(s, 80)) for s in content[:startIdx].split("\n")
        )
        + "\n\n"
        + " ".join(__prettifyExamples(content[startIdx:]))
        + "\n"
    )


def __prettifyContent(content):
    # returns html without tags with indentation
    soup = BeautifulSoup(content, "html.parser").text
    try:
        return __justifycontent(soup)
    except:
        return soup


def __strToObject(string):
    # evaluates the string to python object
    return eval(string.replace("null", "None"))


def __findAttr(s, i):
    """gone back till a namespace and returns the word in between"""
    l = ""
    i -= 1
    while s[i] != " ":
        l = "".join((l, s[i]))
        i -= 1
    # print(l)
    return l[::-1]


def __pyDefinition(s):
    return
    """extracts def line with no extra types hints or types for Python
    unlike how leetcode does"""
    # print(s)
    l = ""
    attr = []
    i = 0
    length = len(s)
    while i < length and i != ")":
        if s[i] == "(":
            defName = __findAttr(s, i)  # get func name

        if s[i] == ":":
            # get a attribute form going back-ward
            attr.append(__findAttr(s, i))

            while s[i] != "," and s[i] != ")":
                i += 1
                if i >= length:
                    break

        l = "".join((l, s[i]))
        if s[i] == ")":
            break
        i += 1

    l = "".join((l, ":"))
    return l, attr, defName


def __CppDefinition(s):
    """solution class def line"""
    # TODO above for cpp
    l = ""
    attr = []
    i = 0
    length = len(s)
    while i < length and i != ")":
        if s[i] == "(":
            defName = __findAttr(s, i)  # get func name

        if s[i] == ":":
            # get a attribute form going back-ward
            attr.append(__findAttr(s, i))

            while s[i] != "," and s[i] != ")":
                i += 1
                if i >= length:
                    break

        l = "".join((l, s[i]))
        if s[i] == ")":
            break
        i += 1

    l = "".join((l, ":"))
    return l.replace("self, ", ""), attr, defName


def get_file_name(title: str, id: int, ext: str) -> str:
    s = f"{title} {id}"
    return nameParser(s) + "." + ext


def get_code():
    pass


def __quesToText(ProblemName, language="Python3", forWhat="write"):

    ext = extensions[language]

    # get all raw contents
    raw, flag = getContents(ProblemName)
    if not flag:
        return

    # getting file name for script file
    questionId = raw.get("questionFrontendId", -1)
    title = raw.get("title", "")
    fileName = get_file_name(title, questionId, ext)
    # preprocessing for future calls (dependent variables) e.g. accRate depends on stats

    codeSnippets_raw = next(
        filter(lambda x: x["lang"] == language, raw["codeSnippets"])
    ).get("code", "")

    stats = __strToObject(raw["stats"])
    topicTags = set(i["name"] for i in raw["topicTags"])
    solution = "Available" if raw["solution"] else None

    # main sections are created here
    similarQuestions = list(
        map(
            lambda i: (i["title"], i["difficulty"]),
            __strToObject(raw["similarQuestions"]),
        )
    )

    sampleTestCase = raw.get("sampleTestCase", []).split("\n")

    definition = codeSnippets_raw

    titleAndId = "_" * 25 + questionId + ". " + title + "_" * 25 + "\n"
    meta_def = __pyDefinition(codeSnippets_raw)

    content = __prettifyContent(raw.get("content", ""))

    metaData = (
        "Difficulty: "
        + raw["difficulty"]
        + "\t\tLikes: "
        + str(raw["likes"])
        + "\t\tDislikes: "
        + str(raw["dislikes"])
        + "\t\tSolution: "
        + str(solution)
        + "\n"
    )
    accRate = (
        "Total Accepted: "
        + stats["totalAccepted"]
        + "\t\tTotal Submission: "
        + stats["totalSubmission"]
        + "\t\tAcceptance Rate: "
        + stats["acRate"]
        + "\n"
    )
    tags = "Tags:  " + ", ".join(i for i in topicTags) + "\n"

    print("*" * 20, ProblemName)
    if forWhat == "write":
        return (
            fileName,
            titleAndId,
            metaData,
            accRate,
            tags,
            content,
            meta_def,
            definition,
            sampleTestCase,
            similarQuestions,
        )
    else:
        return (
            titleAndId,
            metaData,
            accRate,
            tags,
            content,
            meta_def,
            definition,
            sampleTestCase,
            similarQuestions,
        )


def writeFile(problemName, language, path, separate=False):
    text = __quesToText(problemName, language)
    if not text:
        return

    (
        fileName,
        titleAndId,
        metaData,
        accRate,
        tags,
        content,
        meta_def,
        definition,
        sampleTestCase,
        similarQuestions,
    ) = text

    path = os.path.join(path, fileName)

    with open(path, "w") as f:
        # if user just want to solve problem not with definition
        if not separate:
            f.write('"""\n')

            # title and id
            f.write(titleAndId)

            # metadata and solution
            f.write(metaData)

            # acceptance rates
            f.write(accRate)

            # tags type
            f.write(tags)
            f.write("\n\n")

    with open(path, "ab") as f:
        if not separate:
            # contents
            f.write(content.encode("utf-8"))
            f.write('"""\n\n\n'.encode("utf-8"))

    with open(path, "a") as f:
        f.write("import functools, itertools, operator, bisect, array, collections \n")
        f.write("from typing import * \n\n")

        f.write(definition + "\n" * 3)

        # testFunction
        f.write('if __name__ == "__main__":\n')
        f.write("\tpass")

        f.write("\n" * 3)

        # Similar Questions
        if not separate:
            f.write('"""\n')
            if similarQuestions:
                f.write("similarQuestions::\n")
                for q, d in similarQuestions:
                    f.write("\t\t" + q + ": " + d + "\n")
            f.write('"""\n')

    print("File has been created, at " + '"' + path + '"')


def display(problemName):
    text = __quesToText(problemName, forWhat="show")
    if not text:
        return

    (
        titleAndId,
        metaData,
        accRate,
        tags,
        content,
        meta_def,
        definition,
        sampleTestCase,
        similarQuestions,
    ) = text

    print('"""\n')

    # title and id
    print(titleAndId)

    # metadata and solution
    print(metaData)

    # acceptance rates
    print(accRate)

    # tags type
    print(tags)
    print("\n\n")

    # contents
    print(content)
    # print('\n')

    # Similar Questions
    if similarQuestions:
        print("similarQuestions::\n")
        for q, d in similarQuestions:
            print("\t\t" + q + ": " + d + "\n")
    print('"""\n')


if __name__ == "__main__":
    # display("same tree")
    # __quesToText("word break")
    # __quesToText("rectangle area")
    # __quesToText("same tree")
    # __quesToText("two sum")
    # pass

    import threading, time

    threads = []
    for i in range(1, 1925):
        # creating thread
        s = idToName(i)
        # print(i)
        __quesToText(s)
        # threads.append(
        #     threading.Thread(target=__quesToText, args=(s,))
        # )

    # count = 1
    # for i in threads:
    #     i.start()
    #     # i.join()
    #     # if count%25==0:
    #     #     time.sleep(1)
    #     # count+=1

    # for i in threads:
    #     i.join()

    print("Done!")
