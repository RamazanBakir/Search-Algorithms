graph = {'S': ['A', 'G'],
         'A': ['S','B', 'C'],
         'B': ['A', 'D'],
         'C': ['A','D','G'],
         'D': ['B','C','G'],
         'G': ['D']}
def bfs(graph, start):
    explored = []
    queue = [start]
    levels = {} 
    levels[start]= 0
    visited= [start]     
    
    while queue:
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour]= levels[node]+1

    print(explored)

visited = [] 
def dfs(visited, graph, node):
    if node not in visited:
        print (node,end=",")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
print("\n Depth First Search ")
dfs(visited, graph, 'S')
print("\n \n Breadth First Search ")
ans = bfs(graph,'S')
print("\n Uniform Cost Search ")
import Graph as graph
graphic = graph.Graph('S')
graphic.addNode('A')
graphic.addNode('B')
graphic.addNode('C')
graphic.addNode('D')
graphic.addNode('D1')
graphic.addNode('G')
graphic.addNode('G1')
graphic.addNode('G2')
graphic.addNode('G3')
graphic.addConection('S','A',1)
graphic.addConection('S','G',12)
graphic.addConection('A','B',3)
graphic.addConection('A','C',1)
graphic.addConection('B','D',3)
graphic.addConection('C','G2',2)
graphic.addConection('C','D1',1)
graphic.addConection('D1','G',3)

graphic.visitedNode()
graphic.UCS('S', ('G'))
print("\n")