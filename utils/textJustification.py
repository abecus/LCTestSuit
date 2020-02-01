from functools import lru_cache
from itertools import accumulate, islice


m = float("inf")
def textJustification(text, lineWidth=80):
	textList = text.split(' ')
	lineWidth = max(lineWidth, *map(len, textList))
	accLength = [*accumulate(map(len, textList))]
	n = len(accLength)

	def cost(x,y):
		# calculates the cost of words in a line 
		# from index x to y inclusive
		if x==0:	lw = accLength[y]+y-x
		else:	lw = accLength[y]-accLength[x-1]+y-x
		return float('inf') if lw>lineWidth else (lineWidth-lw)**3
	
	dp=[[float("inf")]*n for _ in range(n)]

	# creates dp matrix
	for i in range(n):
		for j in range(0, n-i):
			dp[j][i+j] = cost(j,i+j)
 
	# for i in dp:	print(i)

	breakPoints = [0]*n
	costs = [float('inf')]*n

	# main loop to recreate the break-points from the dp matrix
	for i in reversed(range(n)):
		for j in reversed(range(i, n)):
			if j==n-1 and dp[i][j]!=float('inf'):
				costs[i]=dp[i][j]
				breakPoints[i]=j+1
				break

			if j+1<n and costs[i]>dp[i][j]+costs[j+1]:
				costs[i]=dp[i][j]+costs[j+1]
				breakPoints[i]=j+1

	i=0
	while i<len(textList):
		yield " ".join(islice(textList, i, breakPoints[i]))
		i=breakPoints[i]


if __name__ == "__main__":
	file = "test.txt"
	def getText(file):
		with open(file, "r") as f:
			return f.read()
	# text = """I am the one, the one who don't need no gun to get respect upon the street"""
	for t in textJustification(getText(file).replace("\n", " "), lineWidth=80):
		print(t)
