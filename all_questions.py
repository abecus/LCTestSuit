from utils.scriptWriter import *
from utils.utils import *
import pandas as pd
import threading


def __strToObject(string):
    # evaluates the string to python object
    return eval(string.replace('null', 'None'))


def get_row(i):
    problem = idToName(i)

    raw, flag = getContents(problem)
    if not flag:
        return

    stats: dict = __strToObject(raw['stats'])

    questionId: int = raw['questionFrontendId']
    title: str = raw["title"]
    difficulty: str = raw['difficulty']
    dislikes: int = raw['dislikes']
    likes: int = raw['likes']
    topicTags: list = sorted(set(i['name'] for i in raw['topicTags']))

    similarQuestions: list = sorted(
        [(q['title'], q['difficulty'])
         for q in __strToObject(raw['similarQuestions'])],
        key=lambda x: x[0]
    )

    nAccepted: int = stats['totalAccepted']
    nSubmissions: int = stats['totalSubmission']
    accRate: float = stats['acRate']

    df.loc[i] = [questionId, title, difficulty, dislikes, likes,
                 nAccepted, nSubmissions, accRate, topicTags, similarQuestions]


cols = ["questionId", "title", "difficulty", "dislikes", "likes",
        "nAccepted", "nSubmissions", "accRate", "topicTags", "similarQuestions"]

df = pd.DataFrame(columns=cols)

# threads = []
# for i in range(1, 200):
#     threads.append(
#         threading.Thread(target=get_row, args=(i,))
#     )

# for i in threads:
#     i.start()

# for i in threads:
#     i.join()

# for i in range(1, 11):
for i in range(1, 1925):
    print(i)
    get_row(i)

# print()
df.to_csv('all_leetcode_questions_metadata.csv', index=False)
df.to_csv('new.csv', index=False)