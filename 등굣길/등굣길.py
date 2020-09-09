# directs = [[0,1],[1,0]]
# count = 0

# def solution(m, n, puddles):
#     checkList = [[True for _ in range(m)] for _ in range(n)]
#     for p in puddles:
#         checkList[p[1]-1][p[0]-1] = False
#     DFS([0,0], [n-1,m-1], checkList, n, m)
#     return count%1000000007

# def DFS(currentState, finish, checkList, n, m):
#     global count, directs
#     if currentState == finish:
#         count+=1
#         return
#     checkList[currentState[0]][currentState[1]] = False
#     nextState = []
#     for direct in directs:
#         if direct[0] + currentState[0] >= n or direct[1] + currentState[1] >= m or not checkList[direct[0] + currentState[0]][direct[1] + currentState[1]] : continue
#         nextState.append([direct[0] + currentState[0], direct[1] + currentState[1]])
#     for state in nextState:
#         DFS(state, finish, checkList, n, m)
#         checkList[state[0]][state[1]] = True

# import sys
# m,n = map(int, sys.stdin.readline().strip().split())
# puddles = [[3,2]]
# checkList = [[False for _ in range(m)] for _ in range(n)]
# print(solution(m,n,puddles))
'''===============================================================================================================================1'''
# from collections import deque

# def solution(m, n, puddles):
#     #외곽지역을 None로 설정
#     mapList=[[0 if i !=0 and j != 0 else None for i in range(m+1)] for j in range(n+1)] 
#     mapList[1][1] = 1 #집       
#     for i in puddles: #웅덩이 None로 설정'
#         mapList[i[1]][i[0]] = None
#     # 윗칸과 왼쪽칸까지의 최적 경로의 수 합이 현재칸까지의 최적 경로의 수   
#     for k in range(1,n+1):
#         for j in range(1,m+1):
#             if mapList[k][j] is None: #웅덩이를 만났을때    
#                 continue
#             if mapList[k][j-1] is None and mapList[k-1][j] is None: #윗쪽과 왼쪽이 None라면 현재칸도 None
#                 mapList[k][j] is None
#             elif mapList[k-1][j] is None: #위쪽칸이 None일때 왼쪽칸이 현재칸의 경로의 수
#                 mapList[k][j] = mapList[k][j-1]
#             elif mapList[k][j-1] is None: #왼쪽칸이 None일때 위쪽칸이 현재칸의 경로의 수
#                 mapList[k][j] = mapList[k-1][j]
#             else:
#                 mapList[k][j] = mapList[k-1][j] + mapList[k][j-1] # 현재칸의 경로 = 윗칸과 왼쪽칸까지의 최적 경로의 수 합
#     return mapList[-1][-1] % 1000000007
'''===============================================================================================================================1'''
# import sys
# m,n = map(int, sys.stdin.readline().strip().split())
# puddles = [[3,2]]
# checkList = [[False for _ in range(m)] for _ in range(n)]
# print(solution(m,n,puddles))

# from collections import deque

# def BFS(m, n, puddles):
#     mapList=[[0 if i !=0 or j != 0 else None for i in range(m+1)] for j in range(n+1)] 
#     mapList[1][1] = 1       
#     directs = [[0,1],[1,0]]
#     for i in puddles:
#         mapList[i[1]][i[0]] = None

#     queue = deque([[1,1]])
#     while queue:
#         state = queue.popleft()
#         for direct in directs:
#             if direct[0] + state[0] <= n and direct[1] + state[1] <= m and mapList[direct[0] + state[0]][direct[1] + state[1]] is not None :
#                 queue.append([direct[0] + state[0], direct[1] + state[1]])
#                 mapList[direct[0] + state[0]][direct[1] + state[1]] += mapList[state[0]][state[1]]
#                 if len(queue)>1 and queue[-1] == queue[-2] : queue.pop()
#     return mapList[-1][-1] % 1000000007

# import sys
# m,n = map(int, sys.stdin.readline().strip().split())
# puddles = [[3,2]]
# checkList = [[False for _ in range(m)] for _ in range(n)]
# print(BFS(m,n,puddles))
'''===============================================================================================================================1'''

# import sys
# from collections import deque

# def solution(m, n, puddles):
#     directs = [[0,1],[1,0]]
#     count = 0
#     queue = deque([[0,0]])

#     checkList = [[True for _ in range(m)] for _ in range(n)]
#     for p in puddles:
#         checkList[p[1]-1][p[0]-1] = False
    
#     while queue : 
#         state = queue.popleft()
#         if state == [n-1,m-1]:
#             count += 1
#             continue
#         for direct in directs:
#             if state[0] + direct[0]< n and state[1] + direct[1] < m and checkList[state[0] + direct[0]][state[1] + direct[1]] :
#                 queue.append([state[0] + direct[0] , state[1] + direct[1]])
    
#     return count%1000000007

# m,n = map(int, sys.stdin.readline().strip().split())
# puddles = [[3,2]]
# print(solution(m,n,puddles))