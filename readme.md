DFS = ['University', 'Cafe', 'Airport', 'Museum', 'Bus Terminal', 'Cinema', 'Stadium', 'Shopping Mall', 'Library', 'Hospital']
BFS = ['University', 'Bus Terminal', 'Museum', 'Library', 'Cafe', 'Cinema', 'Airport', 'Shopping Mall', 'Hospital', 'Stadium']

Depth-First Search (DFS) and Breadth-First Search (BFS) are algorithms that traverse or search a graph or network and determine how one can reach other nodes from a particular starting node.

DFS prefers to go deeper into the graph by exploring from the first node it discovers, then it backtracks, whereas BFS aims to visit all nodes at the same level (i.e., equally distant from the starting node) first.

We can see these properties from their outputs.

DFS output: In this output, DFS will first try to reach the 'Stadium' which is deepest node from the 'University' node. Then it will backtrack and move to another deep node 'Hospital'. Again it will continue to visit all neighboring nodes of this node, skipping over nodes that have already been visited (since they have been visited already).

BFS output: In this output, BFS will first visit the neighboring nodes of 'University'. Then it will visit the neighbors of these neighbors and so on, moving to the next level only after it has visited all nodes at the same distance (i.e., nodes that are reached in the same number of steps from the starting node).

These kinds of outputs usually give us insights into understanding the connections in the network and how specific nodes are linked to each other.
