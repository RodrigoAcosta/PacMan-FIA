{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red118\green0\blue2;\red0\green0\blue255;\red251\green0\blue7;
\red15\green112\blue1;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \expnd0\expndtw0\kerning0
"""\
In search.py, you will implement generic search algorithms which are called \
by Pacman agents (in searchAgents.py).\
"""\
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf3 import 
\f0\b0 \cf0 util\
\

\f1\b \cf3 class 
\f0\b0 \cf0 SearchProblem
\f1\b :\
  
\f0\b0 \cf2 """\
  This class outlines the structure of a search problem, but doesn't implement\
  any of the methods (in object-oriented terminology: an abstract class).\
  \
  You do not need to change anything in this class, ever.\
  """\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getStartState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
     
\f0\b0 \cf2 """\
     Returns the start state for the search problem \
     """\
     \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
    \
  \cf3 def 
\f0\b0 \cf0 isGoalState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
     
\f0\b0 \cf2 """\
       state: Search state\
    \
     Returns True if and only if the state is a valid goal state\
     """\
     \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
\
  \cf3 def 
\f0\b0 \cf0 getSuccessors
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
     
\f0\b0 \cf2 """\
       state: Search state\
     \
     For a given state, this should return a list of triples, \
     (successor, action, stepCost), where 'successor' is a \
     successor to the current state, 'action' is the action\
     required to get there, and 'stepCost' is the incremental \
     cost of expanding to that successor\
     """\
     \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
\
  \cf3 def 
\f0\b0 \cf0 getCostOfActions
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 actions
\f1\b ):\
     
\f0\b0 \cf2 """\
      actions: A list of actions to take\
 \
     This method returns the total cost of a particular sequence of actions.  The sequence must\
     be composed of legal moves\
     """\
     \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
           \
\
\cf3 def 
\f0\b0 \cf0 tinyMazeSearch
\f1\b (
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf2 """\
  Returns a sequence of moves that solves tinyMaze.  For any other\
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze\
  """\
  
\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Directions\
  s 
\f1\b = 
\f0\b0 Directions
\f1\b .
\f0\b0 SOUTH\
  w 
\f1\b = 
\f0\b0 Directions
\f1\b .
\f0\b0 WEST\
  
\f1\b \cf3 return  \cf0 [
\f0\b0 s
\f1\b ,
\f0\b0 s
\f1\b ,
\f0\b0 w
\f1\b ,
\f0\b0 s
\f1\b ,
\f0\b0 w
\f1\b ,
\f0\b0 w
\f1\b ,
\f0\b0 s
\f1\b ,
\f0\b0 w
\f1\b ]\
\
\cf3 def 
\f0\b0 \cf0 depthFirstSearch
\f1\b (
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf2 """\
  Search the deepest nodes in the search tree first [p 74].\
  \
  Your search algorithm needs to return a list of actions that reaches\
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].\
  """\
  \cf4 "*** YOUR CODE HERE ***"\
  \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
\
\cf3 def 
\f0\b0 \cf0 breadthFirstSearch
\f1\b (
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf4 "Search the shallowest nodes in the search tree first. [p 74]"\
  "*** YOUR CODE HERE ***"\
  \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
      \
\cf3 def 
\f0\b0 \cf0 uniformCostSearch
\f1\b (
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf4 "Search the node of least total cost first. "\
  "*** YOUR CODE HERE ***"\
  \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
\
\cf3 def 
\f0\b0 \cf0 nullHeuristic
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 problem
\f1\b =
\f0\b0 \cf3 None
\f1\b \cf0 ):\
  
\f0\b0 \cf2 """\
  A heuristic function estimates the cost from the current state to the nearest\
  goal in the provided SearchProblem.  This heuristic is trivial.\
  """\
  
\f1\b \cf3 return 
\f0\b0 \cf4 0\
\

\f1\b \cf3 def 
\f0\b0 \cf0 aStarSearch
\f1\b (
\f0\b0 problem
\f1\b , 
\f0\b0 heuristic
\f1\b =
\f0\b0 nullHeuristic
\f1\b ):\
  
\f0\b0 \cf4 "Search the node that has the lowest combined cost and heuristic first."\
  "*** YOUR CODE HERE ***"\
  \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
    \
  \
\pard\pardeftab720\partightenfactor0

\f2\i\b0 \cf5 # Abbreviations\
\pard\pardeftab720\partightenfactor0

\f0\i0 \cf0 bfs 
\f1\b = 
\f0\b0 breadthFirstSearch\
dfs 
\f1\b = 
\f0\b0 depthFirstSearch\
astar 
\f1\b = 
\f0\b0 aStarSearch\
ucs 
\f1\b = 
\f0\b0 uniformCostSearch}