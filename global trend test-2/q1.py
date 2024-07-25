'''Problem Statement
Write a function to find the longest common subsequence of two given strings.
Sample Test Case
Input: str1 = "abcde", str2 = "ace" Output: 3 (The LCS is "ace")
 Problem Statement
Write a function to find the shortest path from a source vertex to all other vertices in a graph using Dijkstra's algorithm.
Sample Test Case
Input: graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}, source = 0 Output: {0: 0, 1: 3, 2: 1, 3: 4}
Problem Statement
Write a function to solve the 0/1 Knapsack problem using dynamic programming.
Sample Test Case
Input: weights = [1, 2, 3], values = [10, 15, 40], capacity = 6 Output: 55 (Maximum value that can be obtained)




'''
str1="abcde"
str2="ace"

dp=[[0 for i in range(len(str2)+1)]for j in range(len(str1)+1)]

for i in range(len(str1)-1,-1,-1):
    for j in range(len(str2)-1,-1,-1):
        if str1[i] == str2[j]:
            dp[i][j]=1+dp[1+1][j+1]
        else:
            dp[i][j]=max(dp[i+1][j],dp[i][j+1])

print("longest subsequence is",dp[0][0])

