class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connection = self.adjacent_list[node]
            connections = ""
            for vertex in node_connection:
                connections += vertex + " "
            print(node + " --> " + connections)

myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1') 
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')

myGraph.show_connections()
