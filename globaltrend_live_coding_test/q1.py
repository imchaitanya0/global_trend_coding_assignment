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
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a 2D table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # The length of LCS is stored in dp[m][n]
    return dp[m][n]

# Test the function
str1 = "abcde"
str2 = "ace"
result = longest_common_subsequence(str1, str2)
print(result)  # Output: 3

