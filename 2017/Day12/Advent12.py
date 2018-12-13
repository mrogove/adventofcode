#first time exploring networkx
#borrowed heavily from /u/sciyoshi
import networkx as nx

#ingest data
with open('Advent12input.txt') as input_file:
    textline = input_file.readlines()
#strip newlines from list
newlist = []
for i in textline:
    newlist.append(i.strip())

# Create a graph of "programs"
graph = nx.Graph()

for line in newlist:
    # Parse the line
    node, neighbors = line.split(' <-> ')

    # Add edges defined by this line
    graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))

print('Part 1:', len(nx.node_connected_component(graph, '0'))) #number of components in graph that includes 0
print('Part 2:', nx.number_connected_components(graph)) #total number of connected components for the graph
