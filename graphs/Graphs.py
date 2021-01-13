#Graph using adjacent list

class Graph:
    def __init__(self):
        self.nodes = 0
        self.__adjacent_list__ = {}
        self.__node_list = []
    
    def add_node(self,value):
        if(not value  in self.__node_list):
            self.nodes = self.nodes + 1
            self.__node_list.append(value)
            self.__adjacent_list__[value] = []

    def add_edges(self,node1,node2):
        if(node1 in self.__node_list and node2 in self.__node_list):
            if( node1 in self.__adjacent_list__.keys()):
                self.__adjacent_list__[node1].append(node2)
            else:
                self.__adjacent_list__[node1] = [node2]
            
            if( node2 in self.__adjacent_list__.keys()):
                self.__adjacent_list__[node2].append(node1)
            else:
                self.__adjacent_list__[node2] = [node1]
        else:
            raise Exception("No matching node")

    def print(self):
        for item in self.__adjacent_list__:
            print(item,"-->",self.__adjacent_list__[item])


gr = Graph()

gr.add_node(0)
gr.add_node(1)
gr.add_node(2)
gr.add_node(3)
gr.add_node(4)
gr.add_node(5)
gr.add_node(6)

gr.add_edges(0,1)
gr.add_edges(0,2)
gr.add_edges(2,1)
gr.add_edges(1,3)
gr.add_edges(3,4)
gr.add_edges(4,2)
gr.add_edges(4,5)
gr.add_edges(5,6)

gr.print()