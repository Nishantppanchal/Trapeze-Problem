from pynode.main import *

# Function to generate all the nodes.
def generatreAllNode():
    listOfNodes = []
    node = [0, 0, 0, 0, 0, 0, 0]
    # Note:
    #   In a node, the values mean:
    #       0 - Empty postion
    #       1 - A member of the family with Mother, Father and Daugther. They can only move right.
    #       2 - A member of the family with Sister, Younger brother and Older brother. They can only move left.

    # This block of code generates all possible permutations with one 0, three 1s and three 2s.
    for i in range(0, 7):
        node[i] = 0

        for j in range(0, 7):
            if j != i:
                node[j] = 1

                for k in range(0, 7):
                    if k != i and k != j:
                        node[k] = 1

                        for l in range(0, 7):
                            if l != i and l != j and l != k:
                                node[l] = 1

                                for m in range(0, 7):
                                    if m != i and m != j and m != k and m != l:
                                        node[m] = 2

                                        for n in range(0, 7):
                                            if n != i and n != j and n != k and n != l and n != m:
                                                node[n] = 2

                                                for o in range(0, 7):
                                                    if o != i and o != j and o != k and o != l and o != m and o != n:
                                                        node[o] = 2

                                                        if [node[0], node[1], node[2], node[3], node[4], node[5], node[6]] not in listOfNodes:
                                                            listOfNodes.append([node[0], node[1], node[2], node[3], node[4], node[5], node[6]])
                                                            # The line of code below uses these permutations to produce nodes, with the permutations as their name, which are displayed on the 
                                                            # screen. 
                                                            graph.add_node(str(node))
                                                         
    # The two lines of code below make the color of the node with the starting postions as it's name yellow.
    startNode = graph.node(str([1, 1, 1, 0, 2, 2, 2]))
    startNode.set_color(color=Color.YELLOW)

    # The two lines of code below make the color of the node with the ending postions as it's name blue.
    endNode = graph.node(str([2, 2, 2, 0, 1, 1, 1]))
    endNode.set_color(color=Color.BLUE)

    return listOfNodes

def addEdges(listOfNodes):
    for node in listOfNodes:
        # The block below determines the possible people that can move into the empty position.
        emptyPostion = node.index(0)

        startPosition = emptyPostion - 2
        if startPosition < 0:
            startPosition = 0
        
        endPosition = emptyPostion + 2
        if endPosition > 6:
            endPosition = 6

        # The block of code determines the resultant postions for each move and then draw the directed arrow from the node with the original positons as its name to the node with the 
        # resultant postions as its name
        for p in range(startPosition, (endPosition+1)):
            if p != emptyPostion:
                otherNode = node.copy()
                # The if statement below makes sure that only people from family 1 can move right
                if p < emptyPostion and node[p] == 1:
                    otherNode[emptyPostion] = 1
                    otherNode[p] = 0
                    # The line of code below adds the edge to the graph
                    graph.add_edge(str(node), str(otherNode), directed=True)

                # The if statement below makes sure that only people from family 2 can move left.
                elif p > emptyPostion and node[p] == 2:
                    otherNode[emptyPostion] = 2
                    otherNode[p] = 0        
                    # The line of code below adds the edge to the graph
                    graph.add_edge(str(node), str(otherNode), directed=True)

    pause(1000)

def removeUnlessNodes(listOfNodes):
    nodesRemoved = None
    # The block of code below allow removing of node to repeat until there is no node left to remove.
    while nodesRemoved != 0:
        nodesRemoved = 0
        for node in listOfNodes:
            currentNode = graph.node(str(node))
            
            # The code below removes nodes that don't have any incoming edges and are neither the node with the starting postions as its name and the node with the ending positons as it name. 
            if currentNode.indegree() == 0 and node != [1, 1, 1, 0, 2, 2, 2] and node != [2, 2, 2, 0, 1, 1, 1]:
                graph.remove_node(currentNode)
                listOfNodes.remove(node)
                nodesRemoved += 1
                # pause(500)

def pathFinder():
    # The code below test all possible paths inorder to the find the paths that leads from the node with the starting positions as its name to the ending positions.
    paths1 = []
    paths2 = []
    
    startNode = graph.node(str([1, 1, 1, 0, 2, 2, 2]))
    nextNodes = startNode.successor_nodes()
    for node in nextNodes:
        paths1.append([startNode, node])
        edge = graph.edges_between(startNode, node, directed=True)
        edge[0].traverse(initial_node=startNode, color=Color.RED, keep_path=True)  
        node.highlight(color=Color.RED, size=node.size()*1.5)
        node.set_color(color=Color.RED)  

    pause(500)

    done = False
    while done == False:
        paths2 = []
        for a in paths1:
            nextNodes = a[-1].successor_nodes()
            # The if statement below eliminate any paths that lead to dead ends.
            if len(nextNodes) == 0:
                pass
            else:
                for b in nextNodes:
                    c = a.copy()
                    c.append(b)
                    paths2.append(c)
                    # The two lines of code below made a edge red it has been tested
                    edge = graph.edges_between(a[-1], b, directed=True)
                    edge[0].traverse(initial_node=a[-1], color=Color.RED, keep_path=True)
                    
                    if b.id() == str([2, 2, 2, 0, 1, 1, 1]):
                        done = True
                        break

                    elif b.id() != str([1, 1, 1, 0, 2, 2, 2]):
                        # The two lines of code below make a node red it has been tested
                        b.highlight(color=Color.RED, size=node.size()*1.5)
                        b.set_color(color=Color.RED)
                    
                    pause(500)
        
        paths1 = paths2.copy()
        
        if done == True:
            break

    # The block code below colors the nodes and edges along the paths that leads from the node with the starting positions as its name to the ending positions green. 
    for path in paths1:
        for i in range(0, len(path)-1):
            edge = graph.edges_between(path[i], path[i+1], directed=True)
            edge[0].traverse(initial_node=path[i], color=Color.GREEN, keep_path=True)
            
            if path[i].id() != str([1, 1, 1, 0, 2, 2, 2]):
                path[i].highlight(color=Color.GREEN, size=node.size()*1.5)
                path[i].set_color(color=Color.GREEN)
            
            pause(500)

def run(): 
    listOfNodes = generatreAllNode()

    addEdges(listOfNodes)    

    removeUnlessNodes(listOfNodes)

    pause(30000)

    pathFinder()

begin_pynode(run)