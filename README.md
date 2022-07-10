# About repository
A algorithmic solution to a problem with Python. The problem is called the Trapeze problem. The solution involves the use of graph theory.

 Libraries used:
 * [Pynode](https://alexsocha.github.io/pynode/)
 
# Trapeze Problem
There are 7 trapezes in a row. There are two families each with three member. All of the members of both family has on exactly one of the trapezes at any given time. Initally all the members of one family are on one side and the other family are on the other with a empty trapeze in the middle.

It would look:

1 1 1 _ 2 2 2 where 1 represents a member from family one, 2 represents members from family 2 and _ is an empty Trapeze.

Members in family one can only move to the right and members in family 2 can only move to the right. They are able to swap with another member or move into an empty trapeze. The goal of is end up in the initial position, but the two family are swap

It would look like:

2 2 2 _ 1 1 1 where 1 represents a member from family one, 2 represents members from family 2 and _ is an empty Trapeze.

# My solution
```
Let: 
* 0 signify the empty swing
* 1 signify a member of family 1
* 2 signify a member of family 2

Therefore the starting positions are: 1 1 1 0 2 2 2 
Therefore the ending positions are: 2 2 2 0 1 1 1

Generate all possible permutations with one 0, three 1s and three 2s.
Use these permutations to produce nodes, with the permutations as their name, which are displayed on the screen. 

Color the node with the starting postions as it's name as yellow.
Color the node with the ending positons as it's name as blue.

For each node, determine the possible people that can move into the empty position. 
* The fact that members of family 1 can only move left and members of family 2 can only move right need to be taken in to account when determining all the possible moves.
For each move, the resultant positions should be determined and an directed edge should be drawn from the node with the original positons as its name to the node with the resultant postions 
as its name
NOTE: counting of the positon number start from the left.

Remove all nodes that do not have atleat one edge directed inwards, unless the node has the either the starting positions or the ending positions as its name.
Repeat the process of removing nodes that don't meet the condiitons mentioned above until all nodes meet the condiitons mentioned above

Start from the node with the starting positions as it name and go through all the possible paths inorder to find the path that leads to the node with the ending positions as 
its name. 
Eliminate the paths that lead to dead ends as all the possible paths are tested.
If the node or edge had been tested, color it red.
After the path that leads from the node with the starting positions as its name to the node with the ending postion as its name is found, color the edges and node along it green.
```
