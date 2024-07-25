''''
Write a function to find the shortest path from a source vertex to all other vertices in a graph using Dijkstra's algorithm.
Sample Test Case
Input: graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}, source = 0 Output: {0: 0, 1: 3, 2: 1, 3: 4}
'''

graph={'0':{'1':4,'2':1},'1':{'3':1},'2':{'1':2,'3':5},'3':{}}

dp={'0':0,'1':float('inf'),'2':float('inf'),'3':float('inf')}

for v,i in graph.items():
    curr_weight=dp[v]
    for v1,w in i.items():
        if curr_weight+w < dp[v1]:
            dp[v1]=curr_weight+w

print(dp)


