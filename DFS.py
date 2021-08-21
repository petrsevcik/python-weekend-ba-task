import csv
import datetime as dt
import json

graph = {'WUE-JBN': ['JBN-EZO'], 'WUE-NNB': ['NNB-VVH', 'NNB-BPZ', 'NNB-EZO'], 'EZO-JBN': ['JBN-WUE', 'JBN-WUE', 'JBN-WTN', 'JBN-WTN'], 'NNB-ZRW': ['ZRW-BPZ', 'ZRW-VVH', 'ZRW-JBN'], 'EZO-VVH': [], 'NNB-VVH': ['VVH-BPZ'], 'VVH-BPZ': [], 'BPZ-VVH': [], 'ZRW-BPZ': [], 'NNB-BPZ': [], 'JBN-NNB': [], 'EZO-WUE': [], 'ZRW-NNB': [], 'NNB-EZO': [], 'ZRW-VVH': [], 'WUE-VVH': [], 'NNB-WUE': ['WUE-VVH'], 'BPZ-EZO': [], 'ZRW-JBN': [], 'JBN-ZRW': ['ZRW-BPZ', 'ZRW-NNB', 'ZRW-VVH', 'ZRW-NNB', 'ZRW-WTN'], 'VVH-NNB': [], 'BPZ-ZRW': ['ZRW-NNB', 'ZRW-VVH', 'ZRW-WTN', 'ZRW-NNB', 'ZRW-WTN'], 'EZO-NNB': ['NNB-VVH', 'NNB-BPZ', 'NNB-WUE', 'NNB-WTN'], 'WUE-EZO': ['EZO-VVH'], 'JBN-WUE': ['WUE-VVH'], 'NNB-JBN': ['JBN-WTN', 'JBN-WTN', 'JBN-WTN'], 'VVH-ZRW': ['ZRW-BPZ', 'ZRW-NNB', 'ZRW-JBN', 'ZRW-WTN'], 'VVH-WTN': [], 'WUE-ZRW': ['ZRW-VVH', 'ZRW-JBN'], 'JBN-EZO': ['EZO-VVH', 'EZO-WUE', 'EZO-WUE'], 'BPZ-NNB': ['NNB-WUE'], 'ZRW-WTN': [], 'NNB-WTN': [], 'JBN-WTN': []}
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
y = ['WUE-JBN', 'WUE-NNB', 'EZO-JBN', 'NNB-ZRW', 'EZO-VVH', 'NNB-VVH', 'VVH-BPZ', 'BPZ-VVH', 'ZRW-BPZ', 'NNB-BPZ', 'JBN-NNB', 'EZO-WUE', 'ZRW-NNB', 'NNB-EZO', 'ZRW-VVH', 'WUE-VVH', 'NNB-WUE', 'BPZ-EZO', 'ZRW-JBN', 'JBN-ZRW', 'VVH-NNB', 'BPZ-ZRW', 'EZO-NNB', 'WUE-EZO', 'JBN-WUE', 'NNB-JBN', 'VVH-ZRW', 'VVH-WTN', 'WUE-ZRW', 'JBN-EZO', 'BPZ-NNB', 'ZRW-WTN', 'NNB-WTN', 'JBN-WTN']

dfs(visited, graph, 'WUE-JBN')
