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
This file contains all of the agents that can be selected to \
control Pacman.  To select an agent, use the '-p' option\
when running pacman.py.  Arguments can be passed to your agent\
using '-a'.  For example, to load a SearchAgent that uses\
depth first search (dfs), run the following command:\
\
> python pacman.py -p SearchAgent -a searchFunction=depthFirstSearch\
\
Commands to invoke other search strategies can be found in the \
project description.\
\
Please only change the parts of the file you are asked to.\
Look for the lines that say\
\
"*** YOUR CODE HERE ***"\
\
The parts you fill in start about 3/4 of the way down.  Follow the\
project description for details.\
\
Good luck and happy searching!\
"""\
\pard\pardeftab720\partightenfactor0

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Directions\

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Agent\

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Actions\

\f1\b \cf3 import 
\f0\b0 \cf0 util\

\f1\b \cf3 import 
\f0\b0 \cf0 time\

\f1\b \cf3 import 
\f0\b0 \cf0 search\

\f1\b \cf3 import 
\f0\b0 \cf0 searchAgents\
\

\f1\b \cf3 class 
\f0\b0 \cf0 GoWestAgent
\f1\b (
\f0\b0 Agent
\f1\b ):\
  
\f0\b0 \cf4 "An agent that goes West until it can't."\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getAction
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf4 "The agent receives a GameState (defined in pacman.py)."\
    
\f1\b \cf3 if 
\f0\b0 \cf0 Directions
\f1\b .
\f0\b0 WEST 
\f1\b \cf3 in 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 getLegalPacmanActions
\f1\b ():\
      \cf3 return 
\f0\b0 \cf0 Directions
\f1\b .
\f0\b0 WEST\
    
\f1\b \cf3 else\cf0 :\
      \cf3 return 
\f0\b0 \cf0 Directions
\f1\b .
\f0\b0 STOP\
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf5 #######################################################\
# This portion is written for you, but will only work #\
#       after you fill in parts of search.py          #\
#######################################################\
\
\pard\pardeftab720\partightenfactor0

\f1\i0\b \cf3 class 
\f0\b0 \cf0 SearchAgent
\f1\b (
\f0\b0 Agent
\f1\b ):\
  
\f0\b0 \cf2 """\
  This very general search agent finds a path using a supplied search algorithm for a\
  supplied search problem, then returns actions to follow that path.\
  \
  As a default, this agent runs DFS on a PositionSearchProblem to find location (1,1)\
  \
  Options for fn include:\
    depthFirstSearch or dfs\
    breadthFirstSearch or bfs\
    \
  \
  Note: You should NOT change any code in SearchAgent\
  """\
    \
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 fn
\f1\b =
\f0\b0 \cf4 'depthFirstSearch'
\f1\b \cf0 , 
\f0\b0 prob
\f1\b =
\f0\b0 \cf4 'PositionSearchProblem'
\f1\b \cf0 , 
\f0\b0 heuristic
\f1\b =
\f0\b0 \cf4 'nullHeuristic'
\f1\b \cf0 ):\
    
\f2\i\b0 \cf5 # Warning: some advanced Python magic is employed below to find the right functions and problems\
    \
    # Get the search function from the name and heuristic\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf0 fn 
\f1\b \cf3 not in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 search
\f1\b ): \
      \cf3 raise 
\f0\b0 \cf0 AttributeError
\f1\b , 
\f0\b0 fn 
\f1\b + 
\f0\b0 \cf4 ' is not a search function in search.py.'\
    \cf0 func 
\f1\b = 
\f0\b0 getattr
\f1\b (
\f0\b0 search
\f1\b , 
\f0\b0 fn
\f1\b )\
    \cf3 if 
\f0\b0 \cf4 'heuristic' 
\f1\b \cf3 not in 
\f0\b0 \cf0 func
\f1\b .
\f0\b0 func_code
\f1\b .
\f0\b0 co_varnames
\f1\b :\
      \cf3 print\cf0 (
\f0\b0 \cf4 '[SearchAgent] using function ' 
\f1\b \cf0 + 
\f0\b0 fn
\f1\b ) \
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = 
\f0\b0 func\
    
\f1\b \cf3 else\cf0 :\
      \cf3 if 
\f0\b0 \cf0 heuristic 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 searchAgents
\f1\b ):\
        
\f0\b0 heur 
\f1\b = 
\f0\b0 getattr
\f1\b (
\f0\b0 searchAgents
\f1\b , 
\f0\b0 heuristic
\f1\b )\
      \cf3 elif 
\f0\b0 \cf0 heuristic 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 search
\f1\b ):\
        
\f0\b0 heur 
\f1\b = 
\f0\b0 getattr
\f1\b (
\f0\b0 search
\f1\b , 
\f0\b0 heuristic
\f1\b )\
      \cf3 else\cf0 :\
        \cf3 raise 
\f0\b0 \cf0 AttributeError
\f1\b , 
\f0\b0 heuristic 
\f1\b + 
\f0\b0 \cf4 ' is not a function in searchAgents.py or search.py.'\
      
\f1\b \cf3 print\cf0 (
\f0\b0 \cf4 '[SearchAgent] using function %s and heuristic %s' 
\f1\b \cf0 % (
\f0\b0 fn
\f1\b , 
\f0\b0 heuristic
\f1\b )) \
      
\f2\i\b0 \cf5 # Note: this bit of Python trickery combines the search algorithm and the heuristic\
      
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 x
\f1\b : 
\f0\b0 func
\f1\b (
\f0\b0 x
\f1\b , 
\f0\b0 heuristic
\f1\b =
\f0\b0 heur
\f1\b )\
      \
    
\f2\i\b0 \cf5 # Get the search problem type from the name\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf0 prob 
\f1\b \cf3 not in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 searchAgents
\f1\b ) \cf3 or not 
\f0\b0 \cf0 prob
\f1\b .
\f0\b0 endswith
\f1\b (
\f0\b0 \cf4 'Problem'
\f1\b \cf0 ): \
      \cf3 raise 
\f0\b0 \cf0 AttributeError
\f1\b , 
\f0\b0 prob 
\f1\b + 
\f0\b0 \cf4 ' is not a search problem type in SearchAgents.py.'\
    \cf3 self
\f1\b \cf0 .
\f0\b0 searchType 
\f1\b = 
\f0\b0 getattr
\f1\b (
\f0\b0 searchAgents
\f1\b , 
\f0\b0 prob
\f1\b )\
    \cf3 print\cf0 (
\f0\b0 \cf4 '[SearchAgent] using problem type ' 
\f1\b \cf0 + 
\f0\b0 prob
\f1\b ) \
    \
  \cf3 def 
\f0\b0 \cf0 registerInitialState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf2 """\
    This is the first time that the agent sees the layout of the game board. Here, we\
    choose a path to the goal.  In this phase, the agent should compute the path to the\
    goal and store it in a local variable.  All of the work is done in this method!\
    \
    state: a GameState object (pacman.py)\
    """\
    
\f1\b \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b == 
\f0\b0 \cf3 None
\f1\b \cf0 : \cf3 raise 
\f0\b0 \cf0 Exception
\f1\b , 
\f0\b0 \cf4 "No search function provided for SearchAgent"\
    \cf0 starttime 
\f1\b = 
\f0\b0 time
\f1\b .
\f0\b0 time
\f1\b ()\
    
\f0\b0 problem 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchType
\f1\b (
\f0\b0 state
\f1\b ) 
\f2\i\b0 \cf5 # Makes a new search problem\
    
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions  
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction
\f1\b (
\f0\b0 problem
\f1\b ) 
\f2\i\b0 \cf5 # Find a path\
    
\f0\i0 \cf0 totalCost 
\f1\b = 
\f0\b0 problem
\f1\b .
\f0\b0 getCostOfActions
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions
\f1\b )\
    \cf3 print\cf0 (
\f0\b0 \cf4 'Path found with total cost of %d in %.1f seconds' 
\f1\b \cf0 % (
\f0\b0 totalCost
\f1\b , 
\f0\b0 time
\f1\b .
\f0\b0 time
\f1\b () - 
\f0\b0 starttime
\f1\b ))\
    \cf3 if 
\f0\b0 \cf4 '_expanded' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 problem
\f1\b ): \cf3 print\cf0 (
\f0\b0 \cf4 'Search nodes expanded: %d' 
\f1\b \cf0 % 
\f0\b0 problem
\f1\b .
\f0\b0 _expanded
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 getAction
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns the next action in the path chosen earlier (in registerInitialState).  Return\
    Directions.STOP if there is no further action to take.\
    \
    state: a GameState object (pacman.py)\
    """\
    
\f1\b \cf3 if 
\f0\b0 \cf4 'actionIndex' 
\f1\b \cf3 not in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ): 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actionIndex 
\f1\b = 
\f0\b0 \cf4 0\
    \cf0 i 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actionIndex\
    \cf3 self
\f1\b \cf0 .
\f0\b0 actionIndex 
\f1\b += 
\f0\b0 \cf4 1\
    
\f1\b \cf3 if 
\f0\b0 \cf0 i 
\f1\b < 
\f0\b0 len
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions
\f1\b ):\
      \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 actions
\f1\b [
\f0\b0 i
\f1\b ]    \
    \cf3 else\cf0 :\
      \cf3 return 
\f0\b0 \cf0 Directions
\f1\b .
\f0\b0 STOP\
\

\f1\b \cf3 class 
\f0\b0 \cf0 PositionSearchProblem
\f1\b (
\f0\b0 search
\f1\b .
\f0\b0 SearchProblem
\f1\b ):\
  
\f0\b0 \cf2 """\
  A search problem defines the state space, start state, goal test,\
  successor function and cost function.  This search problem can be \
  used to find paths to a particular point on the pacman board.\
  \
  The state space consists of (x,y) positions in a pacman game.\
  \
  Note: this search problem is fully specified; you should NOT change it.\
  """\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 gameState
\f1\b , 
\f0\b0 costFn 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 x
\f1\b : 
\f0\b0 \cf4 1
\f1\b \cf0 , 
\f0\b0 goal
\f1\b =(
\f0\b0 \cf4 1
\f1\b \cf0 ,
\f0\b0 \cf4 1
\f1\b \cf0 )):\
    
\f0\b0 \cf2 """\
    Stores the start and goal.  \
    \
    gameState: A GameState object (pacman.py)\
    costFn: A function from a search state (tuple) to a non-negative number\
    goal: A position in the gameState\
    """\
    \cf3 self
\f1\b \cf0 .
\f0\b0 walls 
\f1\b = 
\f0\b0 gameState
\f1\b .
\f0\b0 getWalls
\f1\b ()\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 startState 
\f1\b = 
\f0\b0 gameState
\f1\b .
\f0\b0 getPacmanPosition
\f1\b ()\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 goal 
\f1\b = 
\f0\b0 goal\
    \cf3 self
\f1\b \cf0 .
\f0\b0 costFn 
\f1\b = 
\f0\b0 costFn\
    
\f1\b \cf3 if 
\f0\b0 \cf0 gameState
\f1\b .
\f0\b0 getNumFood
\f1\b () != 
\f0\b0 \cf4 1 
\f1\b \cf3 or not 
\f0\b0 \cf0 gameState
\f1\b .
\f0\b0 hasFood
\f1\b (*
\f0\b0 goal
\f1\b ):\
      \cf3 print 
\f0\b0 \cf4 'Warning: this does not look like a regular search maze'\
\
    
\f2\i \cf5 # For display purposes\
    
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 _visited
\f1\b , 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _visitedlist
\f1\b , 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b = \{\}, [], 
\f0\b0 \cf4 0\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getStartState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 startState\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 isGoalState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
     
\f0\b0 isGoal 
\f1\b = 
\f0\b0 state 
\f1\b == 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 goal \
     \
     
\f2\i \cf5 # For display purposes only\
     
\f1\i0\b \cf3 if 
\f0\b0 \cf0 isGoal
\f1\b :\
       
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _visitedlist
\f1\b .
\f0\b0 append
\f1\b (
\f0\b0 state
\f1\b )\
       \cf3 import 
\f0\b0 \cf0 __main__\
       
\f1\b \cf3 if 
\f0\b0 \cf4 '_display' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 __main__
\f1\b ):\
         \cf3 if 
\f0\b0 \cf4 'drawExpandedCells' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 __main__
\f1\b .
\f0\b0 _display
\f1\b ): 
\f2\i\b0 \cf5 #@UndefinedVariable\
           
\f0\i0 \cf0 __main__
\f1\b .
\f0\b0 _display
\f1\b .
\f0\b0 drawExpandedCells
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _visitedlist
\f1\b ) 
\f2\i\b0 \cf5 #@UndefinedVariable\
       \
     
\f1\i0\b \cf3 return 
\f0\b0 \cf0 isGoal   \
   \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getSuccessors
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns successor states, the actions they require, and a cost of 1.\
    \
     As noted in search.py:\
         For a given state, this should return a list of triples, \
     (successor, action, stepCost), where 'successor' is a \
     successor to the current state, 'action' is the action\
     required to get there, and 'stepCost' is the incremental \
     cost of expanding to that successor\
    """\
    \
    \cf0 successors 
\f1\b = []\
    \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in \cf0 [
\f0\b0 Directions
\f1\b .
\f0\b0 NORTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 SOUTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 EAST
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 WEST
\f1\b ]:\
      
\f0\b0 x
\f1\b ,
\f0\b0 y 
\f1\b = 
\f0\b0 state\
      dx
\f1\b , 
\f0\b0 dy 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b (
\f0\b0 action
\f1\b )\
      
\f0\b0 nextx
\f1\b , 
\f0\b0 nexty 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 x 
\f1\b + 
\f0\b0 dx
\f1\b ), 
\f0\b0 int
\f1\b (
\f0\b0 y 
\f1\b + 
\f0\b0 dy
\f1\b )\
      \cf3 if not 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b [
\f0\b0 nextx
\f1\b ][
\f0\b0 nexty
\f1\b ]:\
        
\f0\b0 nextState 
\f1\b = (
\f0\b0 nextx
\f1\b , 
\f0\b0 nexty
\f1\b )\
        
\f0\b0 cost 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 costFn
\f1\b (
\f0\b0 nextState
\f1\b )\
        
\f0\b0 successors
\f1\b .
\f0\b0 append
\f1\b ( ( 
\f0\b0 nextState
\f1\b , 
\f0\b0 action
\f1\b , 
\f0\b0 cost
\f1\b ) )\
        \
    
\f2\i\b0 \cf5 # Bookkeeping for display purposes\
    
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b += 
\f0\b0 \cf4 1 \
    
\f1\b \cf3 if 
\f0\b0 \cf0 state 
\f1\b \cf3 not in 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 _visited
\f1\b :\
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _visited
\f1\b [
\f0\b0 state
\f1\b ] = \cf3 True\
      
\f0\b0 self
\f1\b \cf0 .
\f0\b0 _visitedlist
\f1\b .
\f0\b0 append
\f1\b (
\f0\b0 state
\f1\b )\
      \
    \cf3 return 
\f0\b0 \cf0 successors\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getCostOfActions
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 actions
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns the cost of a particular sequence of actions.  If those actions\
    include an illegal move, return 999999\
    """\
    
\f1\b \cf3 if 
\f0\b0 \cf0 actions 
\f1\b == 
\f0\b0 \cf3 None
\f1\b \cf0 : \cf3 return 
\f0\b0 \cf4 999999\
    \cf0 x
\f1\b ,
\f0\b0 y
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 getStartState
\f1\b ()\
    
\f0\b0 cost 
\f1\b = 
\f0\b0 \cf4 0\
    
\f1\b \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in 
\f0\b0 \cf0 actions
\f1\b :\
      
\f2\i\b0 \cf5 # Check figure out the next state and see whether its' legal\
      
\f0\i0 \cf0 dx
\f1\b , 
\f0\b0 dy 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b (
\f0\b0 action
\f1\b )\
      
\f0\b0 x
\f1\b , 
\f0\b0 y 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 x 
\f1\b + 
\f0\b0 dx
\f1\b ), 
\f0\b0 int
\f1\b (
\f0\b0 y 
\f1\b + 
\f0\b0 dy
\f1\b )\
      \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]: \cf3 return 
\f0\b0 \cf4 999999\
      \cf0 cost 
\f1\b += 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 costFn
\f1\b ((
\f0\b0 x
\f1\b ,
\f0\b0 y
\f1\b ))\
    \cf3 return 
\f0\b0 \cf0 cost\
\

\f1\b \cf3 class 
\f0\b0 \cf0 StayEastSearchAgent
\f1\b (
\f0\b0 SearchAgent
\f1\b ):\
  \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = 
\f0\b0 search
\f1\b .
\f0\b0 uniformCostSearch\
      costFn 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 pos
\f1\b : .
\f0\b0 \cf4 5 
\f1\b \cf0 ** 
\f0\b0 pos
\f1\b [
\f0\b0 \cf4 0
\f1\b \cf0 ] \
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchType 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 state
\f1\b : 
\f0\b0 PositionSearchProblem
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 costFn
\f1\b )\
      \
\cf3 class 
\f0\b0 \cf0 StayWestSearchAgent
\f1\b (
\f0\b0 SearchAgent
\f1\b ):\
  \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = 
\f0\b0 search
\f1\b .
\f0\b0 uniformCostSearch\
      costFn 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 pos
\f1\b : 
\f0\b0 \cf4 2 
\f1\b \cf0 ** 
\f0\b0 pos
\f1\b [
\f0\b0 \cf4 0
\f1\b \cf0 ] \
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchType 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 state
\f1\b : 
\f0\b0 PositionSearchProblem
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 costFn
\f1\b )\
\
\cf3 def 
\f0\b0 \cf0 manhattanHeuristic
\f1\b (
\f0\b0 position
\f1\b , 
\f0\b0 problem
\f1\b , 
\f0\b0 info
\f1\b =\{\}):\
  
\f0\b0 \cf4 "The Manhattan distance heuristic for a PositionSearchProblem"\
  \cf0 xy1 
\f1\b = 
\f0\b0 position\
  xy2 
\f1\b = 
\f0\b0 problem
\f1\b .
\f0\b0 goal\
  
\f1\b \cf3 return 
\f0\b0 \cf0 abs
\f1\b (
\f0\b0 xy1
\f1\b [
\f0\b0 \cf4 0
\f1\b \cf0 ] - 
\f0\b0 xy2
\f1\b [
\f0\b0 \cf4 0
\f1\b \cf0 ]) + 
\f0\b0 abs
\f1\b (
\f0\b0 xy1
\f1\b [
\f0\b0 \cf4 1
\f1\b \cf0 ] - 
\f0\b0 xy2
\f1\b [
\f0\b0 \cf4 1
\f1\b \cf0 ])\
\
\pard\pardeftab720\partightenfactor0

\f2\i\b0 \cf5 #####################################################\
# This portion is incomplete.  Time to write code!  #\
#####################################################\
\
\pard\pardeftab720\partightenfactor0

\f1\i0\b \cf3 class 
\f0\b0 \cf0 CornersProblem
\f1\b (
\f0\b0 search
\f1\b .
\f0\b0 SearchProblem
\f1\b ):\
  
\f0\b0 \cf2 """\
  This search problem finds paths through all four corners of a layout.\
\
  You must select a suitable state space and successor function\
  """\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 startingGameState
\f1\b ):\
    
\f0\b0 \cf4 "Stores the walls and corners. Hint: you'll also want to store a starting state"\
    \cf3 self
\f1\b \cf0 .
\f0\b0 walls 
\f1\b = 
\f0\b0 startingGameState
\f1\b .
\f0\b0 getWalls
\f1\b ()\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 startingGameState 
\f1\b = 
\f0\b0 startingGameState\
    top
\f1\b , 
\f0\b0 right 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b .
\f0\b0 height
\f1\b -
\f0\b0 \cf4 2
\f1\b \cf0 , 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b .
\f0\b0 width
\f1\b -
\f0\b0 \cf4 2 \
    \cf3 self
\f1\b \cf0 .
\f0\b0 corners 
\f1\b = ((
\f0\b0 \cf4 1
\f1\b \cf0 ,
\f0\b0 \cf4 1
\f1\b \cf0 ), (
\f0\b0 \cf4 1
\f1\b \cf0 ,
\f0\b0 top
\f1\b ), (
\f0\b0 right
\f1\b , 
\f0\b0 \cf4 1
\f1\b \cf0 ), (
\f0\b0 right
\f1\b , 
\f0\b0 top
\f1\b ))\
    \cf3 for 
\f0\b0 \cf0 corner 
\f1\b \cf3 in 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 corners
\f1\b :\
      \cf3 if not 
\f0\b0 \cf0 startingGameState
\f1\b .
\f0\b0 hasFood
\f1\b (*
\f0\b0 corner
\f1\b ): \cf3 print 
\f0\b0 \cf4 'Warning: no food in corner ' 
\f1\b \cf0 + 
\f0\b0 str
\f1\b (
\f0\b0 corner
\f1\b )\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b = 
\f0\b0 \cf4 0 
\f2\i \cf5 # Number of search nodes expanded\
    \
    
\f0\i0 \cf4 "*** YOUR CODE HERE ***"\
    \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getStartState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf4 "Returns the start state (in your state space, not the full Pacman state space)"\
    "*** YOUR CODE HERE ***"\
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
    
\f0\b0 \cf4 "Returns whether this search state is a goal state of the problem"\
    "*** YOUR CODE HERE ***"\
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
    Returns successor states, the actions they require, and a cost of 1.\
    \
     As noted in search.py:\
         For a given state, this should return a list of triples, \
     (successor, action, stepCost), where 'successor' is a \
     successor to the current state, 'action' is the action\
     required to get there, and 'stepCost' is the incremental \
     cost of expanding to that successor\
    """\
    \
    \cf0 successors 
\f1\b = []\
    \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in \cf0 [
\f0\b0 Directions
\f1\b .
\f0\b0 NORTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 SOUTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 EAST
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 WEST
\f1\b ]:\
      
\f2\i\b0 \cf5 # Add a successor state to the successor list if the action is legal\
      # Here's a code snippet for figuring out whether a new position hits a wall:\
      #   x,y = currentPosition\
      #   dx, dy = Actions.directionToVector(action)\
      #   nextx, nexty = int(x + dx), int(y + dy)\
      #   hitsWall = self.walls[nextx][nexty]\
      \
      
\f0\i0 \cf4 "*** YOUR CODE HERE ***"\
      \
    \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b += 
\f0\b0 \cf4 1\
    
\f1\b \cf3 return 
\f0\b0 \cf0 successors\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getCostOfActions
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 actions
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns the cost of a particular sequence of actions.  If those actions\
    include an illegal move, return 999999.  This is implemented for you.\
    """\
    
\f1\b \cf3 if 
\f0\b0 \cf0 actions 
\f1\b == 
\f0\b0 \cf3 None
\f1\b \cf0 : \cf3 return 
\f0\b0 \cf4 999999\
    \cf0 x
\f1\b ,
\f0\b0 y
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 startingGameState
\f1\b .
\f0\b0 getPacmanPosition
\f1\b ()\
    \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in 
\f0\b0 \cf0 actions
\f1\b :\
      
\f0\b0 dx
\f1\b , 
\f0\b0 dy 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b (
\f0\b0 action
\f1\b )\
      
\f0\b0 x
\f1\b , 
\f0\b0 y 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 x 
\f1\b + 
\f0\b0 dx
\f1\b ), 
\f0\b0 int
\f1\b (
\f0\b0 y 
\f1\b + 
\f0\b0 dy
\f1\b )\
      \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]: \cf3 return 
\f0\b0 \cf4 999999\
    
\f1\b \cf3 return 
\f0\b0 \cf0 len
\f1\b (
\f0\b0 actions
\f1\b )\
\
\
\cf3 def 
\f0\b0 \cf0 cornersHeuristic
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf2 """\
  A heuristic for the CornersProblem that you defined.\
  \
    state:   The current search state \
             (a data structure you chose in your search problem)\
    \
    problem: The CornersProblem instance for this layout.  \
    \
  This function should always return a number that is a lower bound\
  on the shortest path from the state to a goal of the problem.\
  """\
  \cf0 corners 
\f1\b = 
\f0\b0 problem
\f1\b .
\f0\b0 corners 
\f2\i \cf5 # These are the corner coordinates\
  
\f0\i0 \cf0 walls 
\f1\b = 
\f0\b0 problem
\f1\b .
\f0\b0 walls 
\f2\i \cf5 # These are the walls of the maze, as a Grid (game.py)\
  \
  
\f0\i0 \cf4 "*** YOUR CODE HERE ***"\
  
\f1\b \cf3 return 
\f0\b0 \cf4 0 
\f2\i \cf5 # Default to trivial solution\
\

\f1\i0\b \cf3 class 
\f0\b0 \cf0 AStarCornersAgent
\f1\b (
\f0\b0 SearchAgent
\f1\b ):\
  
\f0\b0 \cf4 "A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"\
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 prob
\f1\b : 
\f0\b0 search
\f1\b .
\f0\b0 aStarSearch
\f1\b (
\f0\b0 prob
\f1\b , 
\f0\b0 cornersHeuristic
\f1\b )\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchType 
\f1\b = 
\f0\b0 CornersProblem\
\

\f1\b \cf3 class 
\f0\b0 \cf0 FoodSearchProblem
\f1\b :\
  
\f0\b0 \cf2 """\
  A search problem associated with finding the a path that collects all of the \
  food (dots) in a Pacman game.\
  \
  A search state in this problem is a tuple ( pacmanPosition, foodGrid ) where\
    pacmanPosition: a tuple (x,y) of integers specifying Pacman's position\
    foodGrid:       a Grid (see game.py) of either True or False, specifying remaining food \
  """\
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 startingGameState
\f1\b ):\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 start 
\f1\b = (
\f0\b0 startingGameState
\f1\b .
\f0\b0 getPacmanPosition
\f1\b (), 
\f0\b0 startingGameState
\f1\b .
\f0\b0 getFood
\f1\b ())\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 walls 
\f1\b = 
\f0\b0 startingGameState
\f1\b .
\f0\b0 getWalls
\f1\b ()\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 startingGameState 
\f1\b = 
\f0\b0 startingGameState\
    \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b = 
\f0\b0 \cf4 0\
    \cf3 self
\f1\b \cf0 .
\f0\b0 heuristicInfo 
\f1\b = \{\} 
\f2\i\b0 \cf5 # A dictionary for the heuristic to store information\
      \
  
\f1\i0\b \cf3 def 
\f0\b0 \cf0 getStartState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 start\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 isGoalState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    \cf3 return 
\f0\b0 \cf0 state
\f1\b [
\f0\b0 \cf4 1
\f1\b \cf0 ].
\f0\b0 count
\f1\b () == 
\f0\b0 \cf4 0\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getSuccessors
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf4 "Returns successor states, the actions they require, and a cost of 1."\
    \cf0 successors 
\f1\b = []\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 _expanded 
\f1\b += 
\f0\b0 \cf4 1\
    
\f1\b \cf3 for 
\f0\b0 \cf0 direction 
\f1\b \cf3 in \cf0 [
\f0\b0 Directions
\f1\b .
\f0\b0 NORTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 SOUTH
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 EAST
\f1\b , 
\f0\b0 Directions
\f1\b .
\f0\b0 WEST
\f1\b ]:\
      
\f0\b0 x
\f1\b ,
\f0\b0 y 
\f1\b = 
\f0\b0 state
\f1\b [
\f0\b0 \cf4 0
\f1\b \cf0 ]\
      
\f0\b0 dx
\f1\b , 
\f0\b0 dy 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b (
\f0\b0 direction
\f1\b )\
      
\f0\b0 nextx
\f1\b , 
\f0\b0 nexty 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 x 
\f1\b + 
\f0\b0 dx
\f1\b ), 
\f0\b0 int
\f1\b (
\f0\b0 y 
\f1\b + 
\f0\b0 dy
\f1\b )\
      \cf3 if not 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b [
\f0\b0 nextx
\f1\b ][
\f0\b0 nexty
\f1\b ]:\
        
\f0\b0 nextFood 
\f1\b = 
\f0\b0 state
\f1\b [
\f0\b0 \cf4 1
\f1\b \cf0 ].
\f0\b0 copy
\f1\b ()\
        
\f0\b0 nextFood
\f1\b [
\f0\b0 nextx
\f1\b ][
\f0\b0 nexty
\f1\b ] = \cf3 False\
        
\f0\b0 \cf0 successors
\f1\b .
\f0\b0 append
\f1\b ( ( ((
\f0\b0 nextx
\f1\b , 
\f0\b0 nexty
\f1\b ), 
\f0\b0 nextFood
\f1\b ), 
\f0\b0 direction
\f1\b , 
\f0\b0 \cf4 1
\f1\b \cf0 ) )\
    \cf3 return 
\f0\b0 \cf0 successors\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getCostOfActions
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 actions
\f1\b ):\
    
\f0\b0 \cf2 """Returns the cost of a particular sequence of actions.  If those actions\
    include an illegal move, return 999999"""\
    \cf0 x
\f1\b ,
\f0\b0 y
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 getStartState
\f1\b ()[
\f0\b0 \cf4 0
\f1\b \cf0 ]\
    
\f0\b0 cost 
\f1\b = 
\f0\b0 \cf4 0\
    
\f1\b \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in 
\f0\b0 \cf0 actions
\f1\b :\
      
\f2\i\b0 \cf5 # figure out the next state and see whether it's legal\
      
\f0\i0 \cf0 dx
\f1\b , 
\f0\b0 dy 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b (
\f0\b0 action
\f1\b )\
      
\f0\b0 x
\f1\b , 
\f0\b0 y 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 x 
\f1\b + 
\f0\b0 dx
\f1\b ), 
\f0\b0 int
\f1\b (
\f0\b0 y 
\f1\b + 
\f0\b0 dy
\f1\b )\
      \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 walls
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]:\
        \cf3 return 
\f0\b0 \cf4 999999\
      \cf0 cost 
\f1\b += 
\f0\b0 \cf4 1\
    
\f1\b \cf3 return 
\f0\b0 \cf0 cost\
\

\f1\b \cf3 class 
\f0\b0 \cf0 AStarFoodSearchAgent
\f1\b (
\f0\b0 SearchAgent
\f1\b ):\
  
\f0\b0 \cf4 "A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"\
  
\f1\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchFunction 
\f1\b = \cf3 lambda 
\f0\b0 \cf0 prob
\f1\b : 
\f0\b0 search
\f1\b .
\f0\b0 aStarSearch
\f1\b (
\f0\b0 prob
\f1\b , 
\f0\b0 foodHeuristic
\f1\b )\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 searchType 
\f1\b = 
\f0\b0 FoodSearchProblem\
\

\f1\b \cf3 def 
\f0\b0 \cf0 foodHeuristic
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 problem
\f1\b ):\
  
\f0\b0 \cf2 """\
  Your heuristic for the FoodSearchProblem goes here.\
  \
  This heuristic must be admissible.  If using A* ever finds a solution that is \
  longer than running uniform cost search, your heuristic is *not* admissible!  \
  \
  The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a \
  Grid (see game.py) of either True or False.\
  \
  If you want access to info like walls, capsules, etc., you can query the problem.\
  For example, problem.walls gives you a Grid of where the walls are.\
  \
  If you want to *store* information to be reused in other calls to the heuristic,\
  there is a dictionary called problem.heuristicInfo that you can use. For example,\
  if you only want to count the walls once and store that value, try:\
    problem.heuristicInfo['wallCount'] = problem.walls.count()\
  Subsequent calls to this heuristic can access problem.heuristicInfo['wallCount']\
  """\
  \cf0 position
\f1\b , 
\f0\b0 foodGrid 
\f1\b = 
\f0\b0 state\
  \cf4 "*** YOUR CODE HERE ***"\
  
\f1\b \cf3 return 
\f0\b0 \cf4 0\
  \

\f1\b \cf3 class 
\f0\b0 \cf0 ClosestDotSearchAgent
\f1\b (
\f0\b0 SearchAgent
\f1\b ):\
  
\f0\b0 \cf4 "Search for all food using a sequence of searches"\
  
\f1\b \cf3 def 
\f0\b0 \cf0 registerInitialState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions 
\f1\b = []\
    
\f0\b0 currentState 
\f1\b = 
\f0\b0 state\
    
\f1\b \cf3 while\cf0 (
\f0\b0 currentState
\f1\b .
\f0\b0 getFood
\f1\b ().
\f0\b0 count
\f1\b () > 
\f0\b0 \cf4 0
\f1\b \cf0 ): \
      
\f0\b0 nextPathSegment 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 findPathToClosestDot
\f1\b (
\f0\b0 currentState
\f1\b ) 
\f2\i\b0 \cf5 # The missing piece\
      
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions 
\f1\b += 
\f0\b0 nextPathSegment\
      
\f1\b \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in 
\f0\b0 \cf0 nextPathSegment
\f1\b : \
        
\f0\b0 legal 
\f1\b = 
\f0\b0 currentState
\f1\b .
\f0\b0 getLegalActions
\f1\b ()\
        \cf3 if 
\f0\b0 \cf0 action 
\f1\b \cf3 not in 
\f0\b0 \cf0 legal
\f1\b : \
          
\f0\b0 t 
\f1\b = (
\f0\b0 str
\f1\b (
\f0\b0 action
\f1\b ), 
\f0\b0 str
\f1\b (
\f0\b0 currentState
\f1\b ))\
          \cf3 raise 
\f0\b0 \cf0 Exception
\f1\b , 
\f0\b0 \cf4 'findPathToClosestDot returned an illegal move: %s!\\n%s' 
\f1\b \cf0 % 
\f0\b0 t\
        currentState 
\f1\b = 
\f0\b0 currentState
\f1\b .
\f0\b0 generateSuccessor
\f1\b (
\f0\b0 \cf4 0
\f1\b \cf0 , 
\f0\b0 action
\f1\b )\
    
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actionIndex 
\f1\b = 
\f0\b0 \cf4 0\
    
\f1\b \cf3 print 
\f0\b0 \cf4 'Path found with cost %d.' 
\f1\b \cf0 % 
\f0\b0 len
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 actions
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 findPathToClosestDot
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 startState
\f1\b ):\
    
\f0\b0 \cf4 "Returns a path (a list of actions) to the closest dot, starting in startState"\
    
\f2\i \cf5 # Here are some useful elements of the startState\
    
\f0\i0 \cf0 startPosition 
\f1\b = 
\f0\b0 startState
\f1\b .
\f0\b0 getPacmanPosition
\f1\b ()\
    
\f0\b0 food 
\f1\b = 
\f0\b0 startState
\f1\b .
\f0\b0 getFood
\f1\b ()\
    
\f0\b0 walls 
\f1\b = 
\f0\b0 startState
\f1\b .
\f0\b0 getWalls
\f1\b ()\
\
    
\f0\b0 \cf4 "*** YOUR CODE HERE ***"\
    \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()\
  \
\cf3 class 
\f0\b0 \cf0 ApproximateSearchAgent
\f1\b (
\f0\b0 Agent
\f1\b ):\
  
\f0\b0 \cf4 "Implement your contest entry here.  Change anything but the name."\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 registerInitialState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf4 "This method is called before any moves are made."\
    "*** YOUR CODE HERE ***"\
    \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getAction
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b ):\
    
\f0\b0 \cf2 """\
    From game.py: \
    The Agent will receive a GameState (from either \{pacman, capture, sonar\}.py) and\
    must return an action from Directions.\{North, South, East, West, Stop\}\
    """ \
    \cf4 "*** YOUR CODE HERE ***"\
    \cf0 util
\f1\b .
\f0\b0 raiseNotDefined
\f1\b ()}