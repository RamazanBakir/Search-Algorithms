import Heap as hill
COST = 0
PATH = 2
NODE= 1
class Graph:
    def __init__(self, initialNode=None):
        self.nodeStart = set(initialNode)
        self.connections = {}
        self.isDirected = True
        if (initialNode is not None):
            self.connections[initialNode] = list()
    def addConection(self, NodeOrigin, NodeDest, cost):
        if (NodeOrigin in self.nodeStart and self.isDirected == False):
            self.connections[NodeOrigin].append((cost,NodeDest ))
        elif (self.isDirected == True):
            self.connections[NodeOrigin].append((cost,NodeDest))
            self.connections[NodeDest].append((cost,NodeOrigin ))
        else:
            raise Exception('error creating a connection: the node does not exist in the graph')
    def addNode(self, nodes):
        if (nodes in self.nodeStart):
            raise Exception('error adding node: the node already exists in the graph')
        else:
            self.nodeStart.add(nodes)
            self.connections[nodes] = list()
    def visitedNode(self):
        self.visitedNodes = dict.fromkeys(self.nodeStart, False)
    def VisitedNode(self, node):
        self.visitedNodes[node] = True
    def __str__(self):
        return str(self.connections)
    def UCS(self, initialNode, nodeFinal):
        Priority = hill.PriorityQueue()
        Priority.insertElement((0, initialNode, initialNode))  
        while (not (Priority.empty())): 
            node = Priority.removeElement()
            if (node[NODE] in nodeFinal):
                print("Final Node is : " + node[PATH] + " Cost is : " + str(node[COST]))
                break
            elif(self.visitedNodes[node[NODE]]):
                continue
            else:
                self.VisitedNode(node[NODE])
                childNodes = self.connections[node[NODE]]
                for nodeChild in childNodes:
                    if (self.visitedNodes[nodeChild[NODE]] is not True):
                        Priority.insertElement((nodeChild[COST] + node[COST], nodeChild[NODE], node[PATH] + "->" + str(nodeChild[NODE]))) 
                    else:
                        continue