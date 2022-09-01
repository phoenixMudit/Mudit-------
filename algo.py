

nodes = ["BGI","CDG","DEL","DOH","DSM","EWR","EWY","HND","ICN","JFK","LGA","LHR","ORD","SAN","SFO","SIN","TLV","BUD"]
ro = [
    ["DSM","ORD"],
    ["ORD","BGI"],
    ["BGI","LGA"],
    ["SIN","CDG"],
    ["CDG","BUD"],
    ["DEL","DOH"],
    ["TLV","DEL"],
    ["EWR","HND"],
    ["HND","ICN"],
    ["HND","JFK"],
    ["ICN","JFK"],
    ["JFK","LGA"],
    ["EWY","LHR"],
    ["LHR","SFO"],
    ["SFO","SAN"],
    ["SFO","DSM"],
    ["SAN","EWY"]
]
from ast import Continue
from logging import error
import sys
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value+11020291020121290192
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]




def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}

    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)
    
    
    return(",".join(reversed(path)))


init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["DSM"]["ORD"]=1
init_graph["ORD"]["BGI"]=1
init_graph["BGI"]["LGA"]=1
init_graph["SIN"]["CDG"]=1
init_graph["CDG"]["BUD"]=1
init_graph["DEL"]["DOH"]=1
init_graph["TLV"]["DEL"]=1
init_graph["EWR"]["HND"]=1
init_graph["HND"]["ICN"]=1
init_graph["HND"]["JFK"]=1
init_graph["ICN"]["JFK"]=1
init_graph["JFK"]["LGA"]=1
init_graph["EWY"]["LHR"]=1
init_graph["LHR"]["SFO"]=1
init_graph["SFO"]["SAN"]=1
init_graph["SFO"]["DSM"]=1
init_graph["SAN"]["EWY"]=1

graph = Graph(nodes, init_graph)



brewer=[]
for i in nodes:
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=i)
    
    for j in ro:
        try:
            brewer.append(print_result(previous_nodes, shortest_path, start_node=i, target_node=j[1]))
        except:
            pass



result = [el.split(',') for el in brewer]


l2 = result[:]
l1 = l2[:]

for m in result:
    for n in result:
        if set(m).issubset(set(n)) and m != n:
            l2.remove(m)
            break

res = []
[res.append(x) for x in l2 if x not in res]

for k in res:
    for i in res:
        if i[0] in k and i<k:
            res.remove(i)
            break
for i in res:
    for j in res:
        for k in i:
            try:
                if k in j and i<j:
                    res.remove(j)
                    
            except:
                pass
jizz=[]

for i in res:
    jizz.append(i[0])
print("the minimum number of airports required to be conncted to LGA to give it accessss to all airports is: ",len(jizz))
print("and the airports are: ", jizz)