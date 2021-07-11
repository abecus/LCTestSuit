#%%
import collections
import pandas as pd


df = pd.read_csv('all_leetcode_questions_metadata.csv')
# print(df)

# sorting by like to dislike ratio______________________________
likes_ratio = df.likes / df.dislikes
df["likes_ratio"] = likes_ratio

#%%
sorted_df = df.sort_values(by=["difficulty", "likes", "likes_ratio"], ascending=False)[:100]
# sorted_df.to_csv('to_do.csv', index=False)
# sorted_df.to_csv('all_leetcode_questions_metadata.csv', index=False)

# # sorting by most-voted values______________________________
# votes =  df.likes + df.dislikes
# df["votes"] = votes

# sorted_df = df.sort_values(by=["votes", 'likes'], ascending=False)
# sorted_df.to_csv('most_voted_leetcode_problems.csv', index=False)

# # sorting by acceptance rate values______________________________
# votes =  df.likes + df.dislikes
# df["votes"] = votes

# sorted_df = df.sort_values(by=["accRate", "likes"], ascending=False)
# sorted_df.to_csv('most_acc_rate_leetcode_problems.csv', index=False)
# %%