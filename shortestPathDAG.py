# Shortest paths from starting nodes to ending nodes
# Parts of code taken from https://www.geeksforgeeks.org/topological-sorting/
# Note: DAGs must have zero-based indexing. Number of vertices must be known.


from collections import defaultdict 

# Shortest Path 
class Graph:
    def __init__(self, vertices):
        # set initial conditions
        self.V = vertices
        self.graph = defaultdict(list)

     # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph[u].append([v,w]) 

    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 

        # Mark the current node as visited. 
        visited[v] = True
  
        # Recurse for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i[0]] == False: 
                self.topologicalSortUtil(i[0],visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
        source = []
        end = []
    
        # Find all nodes with parent nodes
        children = []
        for node in self.graph:
            for subNode in self.graph[node]:
                if subNode[0] not in children:
                    children.append(subNode[0])

        # All non-children have no input (source)
        for node in self.graph:
            if node not in children:
                source.append(node)

        # Find nodes that have no output (end)
        for i in range(self.V):
            if i not in self.graph:
                end.append(i)

        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for v in range(self.V): 
            if visited[v] == False: 
                self.topologicalSortUtil(v,visited,stack) 
  
        # Print contents of the stack 
        print(source,end)
        return source, end

    def topologicalHelper(self, v, checked, stack, source):
            # Value has now been checked
            checked[v] == True
            source.append(v)
            if v in self.graph.keys():
                for node,weight in self.graph[v]:
                    if checked[node] == False:
                        self.topologicalHelper(node, checked, stack, source)
            stack.append(v)
            

    def shortestPath(self, start, end):
        stack = []
        # Source is not being used right now (?)
        source = []
        checked = [False]*self.V
        for i in range(self.V):
            if checked[i] == False:
                self.topologicalHelper(start, checked, stack, source)
    
        # Initialize all distances as 'infinite'
        dist = [float("Inf")]*(self.V)
        # Distance begins at 0 from start
        dist[start] = 0
        while stack:
            i = stack.pop()
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        
        # If end is reachable, return distance to end
        if dist[end] != float("Inf"):
            return dist[end]
        # Else, end is unreachable
        else:
            return "Undefined"

# dijkstra function code taken from https://github.com/minsuk-heo/problemsolving/blob/master/graph/dijkstra.py

    def dijkstra(self, initial_node):
        visited = []*self.V
        current_node = initial_node
        path = {}

        nodes = set(range(self.V))
        

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            cur_wt = visited[min_node]

            for edge in self.graph[min_node]:
                wt = cur_wt + edge[1]
                if edge[0] not in visited or wt < visited[edge[1]]:
                    visited[edge[1]] = wt
                    path[edge[0]] = min_node
        return path

    def findAllPaths(self):
        # Find all 0-in and 0-out nodes
        source, end = self.topologicalSort()
        # Examine each 0-in
        for s in source:
            # paths = self.dijkstra(s)
            endNodes = []
            # allRoutes = []
            pathLengths = []
            # Find path lengths to all reachable 0-out
            for e in end:
                pathResult = g.shortestPath(s,e)
                if pathResult != "Undefined":
                    endNodes.append(e)
                    pathLengths.append(pathResult)
                    # thisRoute = [e]
                    # while e != s:
                    #     thisRoute.append(paths[e])
                    #     e = paths[e]
                    # thisRoute.reverse()
                    # allRoutes.append(thisRoute)
            if len(pathLengths) > 0:
                # For every 0-in, find the shortest path to any reachable 0-out
                shortestLen = min(pathLengths)
                shortestEnd = endNodes[pathLengths.index(shortestLen)]
                # shortestRoute = allRoutes[pathLengths.index(shortestLen)]
                print("Shortest path starting at node ", s, " ends at node ", shortestEnd, " with length ", shortestLen)
                #print("The shortest route is ", shortestRoute)
                

#Example 1
g = Graph(13) 
g.addEdge(0, 1, 4) 
g.addEdge(0, 2, 3) 
g.addEdge(0, 4,11)
g.addEdge(0,11, 2)
g.addEdge(1, 3, 7) 
g.addEdge(1, 4, 1) 
g.addEdge(2, 5, 9) 
g.addEdge(3, 6, 2)
g.addEdge(4, 6, 2)
g.addEdge(5, 4, 1)
g.addEdge(5, 6, 5)    
g.addEdge(7, 5, 5)
g.addEdge(7, 8, 1) 
g.addEdge(9, 8, 4)
g.addEdge(10,6, 6)
g.addEdge(10,8,12)
g.addEdge(10,12,5)
#print(g.graph)
#g.findAllPaths()

h = Graph(10)
h.addEdge(0, 1, 1)
h.addEdge(0, 2, 2)
h.addEdge(0, 5, 3)
h.addEdge(1, 2, 0)
h.addEdge(1, 3, 8)
h.addEdge(2, 3, 4)
h.addEdge(2, 7, 5)
h.addEdge(3, 4,-2)
h.addEdge(6, 5, 3)
h.addEdge(7, 9, 2)
h.addEdge(8, 1, 7)
# print(h.graph)
#h.findAllPaths()

i = Graph(8)
i.addEdge(0, 2, 1)
i.addEdge(0, 4, 1)
i.addEdge(0, 6, 1)
i.addEdge(2, 1, 1)
i.addEdge(4, 3, 1)
i.addEdge(1, 7, 2)
i.addEdge(1, 5, 2)
i.addEdge(3, 5, 3)
i.addEdge(7, 5, 1)
#print(i.graph)
#i.findAllPaths()

j = Graph(6)
j.addEdge(0, 1, 7)
j.addEdge(0, 2, 9)
j.addEdge(0, 5,14)
j.addEdge(1, 2,10)
j.addEdge(1, 3,15)
j.addEdge(2, 3,11)
j.addEdge(2, 5, 2)
j.addEdge(3, 4, 6)
j.addEdge(4, 5, 9)
#print(j.graph)
j.topologicalSort
#j.findAllPaths