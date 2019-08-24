from collections import defaultdict 

# Shortest Path 
class Graph:
    def __init__(self, vertices):
        # set initial conditions
        self.V = vertices
        self.graph = defaultdict(list)

    def topologicalHelper(self, v, checked, stack):
            checked[v] == True
            if v in self.graph.keys():
                for node,weight in self.graph[v]:
                    if checked[node] == False:
                        self.topologicalHelper(node, checked, stack)
            stack.append(v)

    def shortestPath(self, start, end):
        stack = []
        checked = [False]*self.V
        for i in range(self.V):
            if checked[i] == False:
                self.topologicalHelper(start, checked, stack)
    
        dist = [float("Inf")]*(self.V)
        dist[start] = 0

        while stack:
            i = stack.pop()
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        
        if dist[end] != float("Inf"):
            print("%d" %dist[i])
        else:
            print("Undefined")


    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph[u].append((v,w)) 

g = Graph(6) 
g.addEdge(0, 1, 5) 
g.addEdge(0, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(2, 3, -1)
g.addEdge(3,4,9)
  
# source = 1 
start = 1
end = 4

g.shortestPath(start, end) 
    


#Longest Path
def DAGmaxdfs(node, graph, path, checked):
    # current node checked
    checked[node] = True
    # traverse all paths leaving current node
    for i in range(len(graph[node])):
        if checked[graph[node][i]] == False:
            # continue dfs if not checked
            DAGmaxdfs(graph[node][i], graph, path, checked)
        # set index to max of paths
        path[node] = max(path[node], 1+path[graph[node][i]])

def longestPath(graph, n):
    maxPath = 0
    # create an array to hold length of each path from node
    path = [0]*(n+1)
    # no nodes have been checked yet
    checked = [False]*(n+1)
    # perform dfs for unchecked nodes
    for node in range(1, n+1):
        if checked[node] == False:
            DAGmaxdfs(node, graph, path, checked)
    # compare maximums from each path to find overall max
    for i in range(1, n+1):
        maxPath = max(maxPath, path[i])

    return maxPath


# # Function to add an edge  
# def addEdge(graph, u, v):  
   
#     graph[u].append(v) 

# # Driver Code  
# if __name__ == "__main__":  
   
#     n = 5 
#     graph = [[] for i in range(n + 1)] 
    
#     # Example-1  
#     addEdge(graph, 1, 2)  
#     addEdge(graph, 1, 3)  
#     addEdge(graph, 3, 2)  
#     addEdge(graph, 2, 4)  
#     addEdge(graph, 3, 4)  
    
#     print(longestPath(graph, n)) 
