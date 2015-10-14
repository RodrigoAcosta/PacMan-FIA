{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red118\green0\blue2;\red0\green0\blue255;\red15\green112\blue1;
\red251\green0\blue7;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \expnd0\expndtw0\kerning0
"""\
Pacman.py holds the logic for the classic pacman game along with the main \
code to run a game.  This file is divided into three sections:\
  \
  (i)  Your interface to the pacman world:\
          Pacman is a complex environment.  You probably don't want to \
          read through all of the code we wrote to make the game runs\
          correctly.  This section contains the parts of the code\
          that you will need to understand in order to complete the \
          project.  There is also some code in game.py that you should \
          understand.\
\
  (ii)  The hidden secrets of pacman:\
          This section contains all of the logic code that the pacman\
          environment uses to decide who can move where, who dies when\
          things collide, etc.  You shouldn't need to read this section\
          of code, but you can if you want.\
          \
  (iii) Framework to start a game:\
          The final section contains the code for reading the command\
          you use to set up the game, then starting up a new game, along with \
          linking in all the external parts (agent functions, graphics).\
          Check this section out to see all the options available to you.\
          \
To play your first game, type 'python pacman.py' from the command line.\
The keys are 'a', 's', 'd', and 'w' to move (or arrow keys).  Have fun!\
"""\
\pard\pardeftab720\partightenfactor0

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 GameStateData\

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Game\

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Directions\

\f1\b \cf3 from 
\f0\b0 \cf0 game 
\f1\b \cf3 import 
\f0\b0 \cf0 Actions\

\f1\b \cf3 from 
\f0\b0 \cf0 util 
\f1\b \cf3 import 
\f0\b0 \cf0 nearestPoint\

\f1\b \cf3 from 
\f0\b0 \cf0 util 
\f1\b \cf3 import 
\f0\b0 \cf0 manhattanDistance\

\f1\b \cf3 import 
\f0\b0 \cf0 util
\f1\b , 
\f0\b0 layout\

\f1\b \cf3 import 
\f0\b0 \cf0 sys
\f1\b , 
\f0\b0 types
\f1\b , 
\f0\b0 time
\f1\b , 
\f0\b0 random\
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf4 ###################################################\
# YOUR INTERFACE TO THE PACMAN WORLD: A GameState #\
###################################################\
\
\pard\pardeftab720\partightenfactor0

\f1\i0\b \cf3 class 
\f0\b0 \cf0 GameState
\f1\b :\
  
\f0\b0 \cf2 """\
  A GameState specifies the full game state, including the food, capsules, \
  agent configurations and score changes.\
  \
  GameStates are used by the Game object to capture the actual state of the game and\
  can be used by agents to reason about the game.\
  \
  Much of the information in a GameState is stored in a GameStateData object.  We \
  strongly suggest that you access that data via the accessor methods below rather\
  than referring to the GameStateData object directly.\
  \
  Note that in classic Pacman, Pacman is always agent 0.  \
  """\
  \
  
\f2\i \cf4 ####################################################\
  # Accessor methods: use these to access state data #\
  ####################################################\
  \
  
\f1\i0\b \cf3 def 
\f0\b0 \cf0 getLegalActions
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 agentIndex
\f1\b =
\f0\b0 \cf5 0 
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Returns the legal actions for the agent specified.\
    """\
    
\f1\b \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 isWin
\f1\b () \cf3 or 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 isLose
\f1\b (): \cf3 return \cf0 []\
    \
    \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0
\f1\b \cf0 :  
\f2\i\b0 \cf4 # Pacman is moving\
      
\f1\i0\b \cf3 return 
\f0\b0 \cf0 PacmanRules
\f1\b .
\f0\b0 getLegalActions
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 )\
    \cf3 else\cf0 :\
      \cf3 return 
\f0\b0 \cf0 GhostRules
\f1\b .
\f0\b0 getLegalActions
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 agentIndex 
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 generateSuccessor
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 agentIndex
\f1\b , 
\f0\b0 action
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns the successor state after the specified agent takes the action.\
    """\
    
\f2\i \cf4 # Check that successors exist\
    
\f1\i0\b \cf3 if 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 isWin
\f1\b () \cf3 or 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 isLose
\f1\b (): \cf3 raise 
\f0\b0 \cf0 Exception
\f1\b (
\f0\b0 \cf5 'Can\\'t generate a successor of a terminal state.'
\f1\b \cf0 )\
    \
    
\f2\i\b0 \cf4 # Copy current state\
    
\f0\i0 \cf0 state 
\f1\b = 
\f0\b0 GameState
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 )\
\
    
\f2\i\b0 \cf4 # Let agent's logic deal with its action's effects on the board\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0
\f1\b \cf0 :  
\f2\i\b0 \cf4 # Pacman is moving\
      
\f0\i0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _eaten 
\f1\b = [\cf3 False for 
\f0\b0 \cf0 i 
\f1\b \cf3 in 
\f0\b0 \cf0 range
\f1\b (
\f0\b0 state
\f1\b .
\f0\b0 getNumAgents
\f1\b ())]\
      
\f0\b0 PacmanRules
\f1\b .
\f0\b0 applyAction
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 action 
\f1\b )\
    \cf3 else\cf0 :                
\f2\i\b0 \cf4 # A ghost is moving\
      
\f0\i0 \cf0 GhostRules
\f1\b .
\f0\b0 applyAction
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 action
\f1\b , 
\f0\b0 agentIndex 
\f1\b )\
      \
    
\f2\i\b0 \cf4 # Time passes\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0
\f1\b \cf0 :\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange 
\f1\b += -
\f0\b0 TIME_PENALTY 
\f2\i \cf4 # Penalty for waiting around\
    
\f1\i0\b \cf3 else\cf0 :\
      
\f0\b0 GhostRules
\f1\b .
\f0\b0 decrementTimer
\f1\b ( 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 agentIndex
\f1\b ] )\
      \
    
\f2\i\b0 \cf4 # Resolve multi-agent effects\
    
\f0\i0 \cf0 GhostRules
\f1\b .
\f0\b0 checkDeath
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 agentIndex 
\f1\b )\
\
    
\f2\i\b0 \cf4 # Book keeping\
    
\f0\i0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _agentMoved 
\f1\b = 
\f0\b0 agentIndex\
    state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 score 
\f1\b += 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange\
    
\f1\b \cf3 return 
\f0\b0 \cf0 state\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getLegalPacmanActions
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 getLegalActions
\f1\b ( 
\f0\b0 \cf5 0 
\f1\b \cf0 )\
  \
  \cf3 def 
\f0\b0 \cf0 generatePacmanSuccessor
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 action 
\f1\b ):\
    
\f0\b0 \cf2 """\
    Generates the successor state after the specified pacman move\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 generateSuccessor
\f1\b ( 
\f0\b0 \cf5 0
\f1\b \cf0 , 
\f0\b0 action 
\f1\b )\
  \
  \cf3 def 
\f0\b0 \cf0 getPacmanState
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Returns an AgentState object for pacman (in game.py)\
    \
    state.pos gives the current position\
    state.direction gives the travel vector\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 \cf5 0
\f1\b \cf0 ].
\f0\b0 copy
\f1\b ()\
  \
  \cf3 def 
\f0\b0 \cf0 getPacmanPosition
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 \cf5 0
\f1\b \cf0 ].
\f0\b0 getPosition
\f1\b ()\
  \
  \cf3 def 
\f0\b0 \cf0 getGhostStates
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 \cf5 1
\f1\b \cf0 :]\
\
  \cf3 def 
\f0\b0 \cf0 getGhostState
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 agentIndex 
\f1\b ):\
    \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0 
\f1\b \cf3 or 
\f0\b0 \cf0 agentIndex 
\f1\b >= 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 getNumAgents
\f1\b ():\
      \cf3 raise 
\f0\b0 \cf5 "Invalid index passed to getGhostState"\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 agentIndex
\f1\b ]\
  \
  \cf3 def 
\f0\b0 \cf0 getGhostPosition
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 agentIndex 
\f1\b ):\
    \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0
\f1\b \cf0 :\
      \cf3 raise 
\f0\b0 \cf5 "Pacman's index passed to getGhostPosition"\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 agentIndex
\f1\b ].
\f0\b0 getPosition
\f1\b ()\
  \
  \cf3 def 
\f0\b0 \cf0 getNumAgents
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 \cf0 len
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 agentStates 
\f1\b )\
  \
  \cf3 def 
\f0\b0 \cf0 getScore
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 score\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getCapsules
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Returns a list of positions (x,y) of the remaining capsules.\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 capsules\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getNumFood
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 food
\f1\b .
\f0\b0 count
\f1\b ()\
  \
  \cf3 def 
\f0\b0 \cf0 getFood
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Returns a Grid of boolean food indicator variables.\
    \
    Grids can be accessed via list notation, so to check\
    if there is food at (x,y), just call\
    \
    currentFood = state.getFood()\
    if currentFood[x][y] == True: ...\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 food\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getWalls
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Returns a Grid of boolean wall indicator variables.\
    \
    Grids can be accessed via list notation, so to check\
    if there is food at (x,y), just call\
    \
    walls = state.getWalls()\
    if walls[x][y] == True: ...\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 layout
\f1\b .
\f0\b0 walls\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 hasFood
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 x
\f1\b , 
\f0\b0 y
\f1\b ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 food
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]\
  \
  \cf3 def 
\f0\b0 \cf0 hasWall
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 x
\f1\b , 
\f0\b0 y
\f1\b ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 layout
\f1\b .
\f0\b0 walls
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]\
\
  \cf3 def 
\f0\b0 \cf0 isLose
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 _lose\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 isWin
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 _win\
  \
  
\f2\i \cf4 #############################################\
  #             Helper methods:               #          \
  # You shouldn't need to call these directly #\
  #############################################\
  \
  
\f1\i0\b \cf3 def 
\f0\b0 \cf0 __init__
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 prevState 
\f1\b = 
\f0\b0 \cf3 None 
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """ \
    Generates a new state by copying information from its predecessor.\
    """\
    
\f1\b \cf3 if 
\f0\b0 \cf0 prevState 
\f1\b != 
\f0\b0 \cf3 None
\f1\b \cf0 : 
\f2\i\b0 \cf4 # Initial state\
      
\f0\i0 \cf3 self
\f1\b \cf0 .
\f0\b0 data 
\f1\b = 
\f0\b0 GameStateData
\f1\b (
\f0\b0 prevState
\f1\b .
\f0\b0 data
\f1\b )\
    \cf3 else\cf0 :\
      
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 data 
\f1\b = 
\f0\b0 GameStateData
\f1\b ()\
    \
  \cf3 def 
\f0\b0 \cf0 deepCopy
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    
\f0\b0 state 
\f1\b = 
\f0\b0 GameState
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 )\
    
\f0\b0 state
\f1\b .
\f0\b0 data 
\f1\b = 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 deepCopy
\f1\b ()\
    \cf3 return 
\f0\b0 \cf0 state\
    \
  
\f1\b \cf3 def 
\f0\b0 \cf0 __eq__
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 other 
\f1\b ):\
    
\f0\b0 \cf2 """\
    Allows two states to be compared.\
    """\
    
\f1\b \cf3 return 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 data 
\f1\b == 
\f0\b0 other
\f1\b .
\f0\b0 data\
                                                      \
  
\f1\b \cf3 def 
\f0\b0 \cf0 __hash__
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Allows states to be keys of dictionaries.\
    """\
    
\f1\b \cf3 return 
\f0\b0 \cf0 hash
\f1\b ( 
\f0\b0 str
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ) )\
\
  \cf3 def 
\f0\b0 \cf0 __str__
\f1\b ( 
\f0\b0 \cf3 self 
\f1\b \cf0 ):\
    \
    \cf3 return 
\f0\b0 \cf0 str
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 data
\f1\b )\
      \
  \cf3 def 
\f0\b0 \cf0 initialize
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 layout
\f1\b , 
\f0\b0 numGhostAgents
\f1\b =
\f0\b0 \cf5 1000 
\f1\b \cf0 ):\
    
\f0\b0 \cf2 """\
    Creates an initial game state from a layout array (see layout.py).\
    """\
    \cf3 self
\f1\b \cf0 .
\f0\b0 data
\f1\b .
\f0\b0 initialize
\f1\b (
\f0\b0 layout
\f1\b , 
\f0\b0 numGhostAgents
\f1\b )\
  \
\pard\pardeftab720\partightenfactor0

\f2\i\b0 \cf4 ############################################################################\
#                     THE HIDDEN SECRETS OF PACMAN                         #\
#                                                                          #\
# You shouldn't need to look through the code in this section of the file. #\
############################################################################  \
  \
\pard\pardeftab720\partightenfactor0

\f0\i0 \cf0 SCARED_TIME 
\f1\b = 
\f0\b0 \cf5 40    
\f2\i \cf4 # Moves ghosts are scared \

\f0\i0 \cf0 COLLISION_TOLERANCE 
\f1\b = 
\f0\b0 \cf5 0.7 
\f2\i \cf4 # How close ghosts must be to Pacman to kill\

\f0\i0 \cf0 TIME_PENALTY 
\f1\b = 
\f0\b0 \cf5 1 
\f2\i \cf4 # Number of points lost each round\
\

\f1\i0\b \cf3 class 
\f0\b0 \cf0 ClassicGameRules
\f1\b :\
  
\f0\b0 \cf2 """\
  These game rules manage the control flow of a game, deciding when\
  and how the game starts and ends.\
  """\
  \
  
\f1\b \cf3 def 
\f0\b0 \cf0 newGame
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 layout
\f1\b , 
\f0\b0 pacmanAgent
\f1\b , 
\f0\b0 ghostAgents
\f1\b , 
\f0\b0 display
\f1\b , 
\f0\b0 quiet 
\f1\b = \cf3 False \cf0 ):\
    
\f0\b0 agents 
\f1\b = [
\f0\b0 pacmanAgent
\f1\b ] + 
\f0\b0 ghostAgents
\f1\b [:
\f0\b0 layout
\f1\b .
\f0\b0 getNumGhosts
\f1\b ()]\
    
\f0\b0 initState 
\f1\b = 
\f0\b0 GameState
\f1\b ()\
    
\f0\b0 initState
\f1\b .
\f0\b0 initialize
\f1\b ( 
\f0\b0 layout
\f1\b , 
\f0\b0 len
\f1\b (
\f0\b0 ghostAgents
\f1\b ) )\
    
\f0\b0 game 
\f1\b = 
\f0\b0 Game
\f1\b (
\f0\b0 agents
\f1\b , 
\f0\b0 display
\f1\b , 
\f0\b0 \cf3 self
\f1\b \cf0 )\
    
\f0\b0 game
\f1\b .
\f0\b0 state 
\f1\b = 
\f0\b0 initState\
    \cf3 self
\f1\b \cf0 .
\f0\b0 quiet 
\f1\b = 
\f0\b0 quiet\
    
\f1\b \cf3 return 
\f0\b0 \cf0 game\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 process
\f1\b (
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b , 
\f0\b0 game
\f1\b ):\
    
\f0\b0 \cf2 """\
    Checks to see whether it is time to end the game.\
    """\
    
\f1\b \cf3 if 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 isWin
\f1\b (): 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 win
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 game
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 isLose
\f1\b (): 
\f0\b0 \cf3 self
\f1\b \cf0 .
\f0\b0 lose
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 game
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 win
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b , 
\f0\b0 game 
\f1\b ):\
    \cf3 if not 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 quiet
\f1\b : \cf3 print 
\f0\b0 \cf5 "Pacman emerges victorious! Score: %d" 
\f1\b \cf0 % 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 score\
    game
\f1\b .
\f0\b0 gameOver 
\f1\b = \cf3 True\
\
  def 
\f0\b0 \cf0 lose
\f1\b ( 
\f0\b0 \cf3 self
\f1\b \cf0 , 
\f0\b0 state
\f1\b , 
\f0\b0 game 
\f1\b ):\
    \cf3 if not 
\f0\b0 self
\f1\b \cf0 .
\f0\b0 quiet
\f1\b : \cf3 print 
\f0\b0 \cf5 "Pacman died! Score: %d" 
\f1\b \cf0 % 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 score\
    game
\f1\b .
\f0\b0 gameOver 
\f1\b = \cf3 True\
    \
class 
\f0\b0 \cf0 PacmanRules
\f1\b :\
  
\f0\b0 \cf2 """\
  These functions govern how pacman interacts with his environment under\
  the classic game rules.\
  """\
  \cf0 PACMAN_SPEED
\f1\b =
\f0\b0 \cf5 1\
\
  
\f1\b \cf3 def 
\f0\b0 \cf0 getLegalActions
\f1\b ( 
\f0\b0 state 
\f1\b ):\
    
\f0\b0 \cf2 """\
    Returns a list of possible actions.\
    """\
    
\f1\b \cf3 return 
\f0\b0 \cf0 Actions
\f1\b .
\f0\b0 getPossibleActions
\f1\b ( 
\f0\b0 state
\f1\b .
\f0\b0 getPacmanState
\f1\b ().
\f0\b0 configuration
\f1\b , 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 layout
\f1\b .
\f0\b0 walls 
\f1\b )\
  
\f0\b0 getLegalActions 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 getLegalActions 
\f1\b )\
  \
  \cf3 def 
\f0\b0 \cf0 applyAction
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 action 
\f1\b ):\
    
\f0\b0 \cf2 """\
    Edits the state to reflect the results of the action.\
    """\
    \cf0 legal 
\f1\b = 
\f0\b0 PacmanRules
\f1\b .
\f0\b0 getLegalActions
\f1\b ( 
\f0\b0 state 
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 action 
\f1\b \cf3 not in 
\f0\b0 \cf0 legal
\f1\b :\
      \cf3 raise 
\f0\b0 \cf5 "Illegal action"
\f1\b \cf0 , 
\f0\b0 action\
    \
    pacmanState 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 \cf5 0
\f1\b \cf0 ]\
    \
    
\f2\i\b0 \cf4 # Update Configuration\
    
\f0\i0 \cf0 vector 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b ( 
\f0\b0 action
\f1\b , 
\f0\b0 PacmanRules
\f1\b .
\f0\b0 PACMAN_SPEED 
\f1\b )\
    
\f0\b0 pacmanState
\f1\b .
\f0\b0 configuration 
\f1\b = 
\f0\b0 pacmanState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 generateSuccessor
\f1\b ( 
\f0\b0 vector 
\f1\b )\
    \
    
\f2\i\b0 \cf4 # Eat\
    
\f0\i0 \cf0 next 
\f1\b = 
\f0\b0 pacmanState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 getPosition
\f1\b ()\
    
\f0\b0 nearest 
\f1\b = 
\f0\b0 nearestPoint
\f1\b ( 
\f0\b0 next 
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 manhattanDistance
\f1\b ( 
\f0\b0 nearest
\f1\b , 
\f0\b0 next 
\f1\b ) <= 
\f0\b0 \cf5 0.5 
\f1\b \cf0 :\
      
\f2\i\b0 \cf4 # Remove food\
      
\f0\i0 \cf0 PacmanRules
\f1\b .
\f0\b0 consume
\f1\b ( 
\f0\b0 nearest
\f1\b , 
\f0\b0 state 
\f1\b )\
  
\f0\b0 applyAction 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 applyAction 
\f1\b )\
\
  \cf3 def 
\f0\b0 \cf0 consume
\f1\b ( 
\f0\b0 position
\f1\b , 
\f0\b0 state 
\f1\b ):\
    
\f0\b0 x
\f1\b ,
\f0\b0 y 
\f1\b = 
\f0\b0 position\
    
\f2\i \cf4 # Eat food\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 food
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ]:\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange 
\f1\b += 
\f0\b0 \cf5 10\
      \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 food 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 food
\f1\b .
\f0\b0 copy
\f1\b ()\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 food
\f1\b [
\f0\b0 x
\f1\b ][
\f0\b0 y
\f1\b ] = \cf3 False\
      
\f0\b0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _foodEaten 
\f1\b = 
\f0\b0 position\
      
\f2\i \cf4 # TODO: cache numFood?\
      
\f0\i0 \cf0 numFood 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 getNumFood
\f1\b ()\
      \cf3 if 
\f0\b0 \cf0 numFood 
\f1\b == 
\f0\b0 \cf5 0 
\f1\b \cf3 and not 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _lose
\f1\b :\
        
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange 
\f1\b += 
\f0\b0 \cf5 500\
        \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _win 
\f1\b = \cf3 True\
    
\f2\i\b0 \cf4 # Eat capsule\
    
\f1\i0\b \cf3 if\cf0 ( 
\f0\b0 position 
\f1\b \cf3 in 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 getCapsules
\f1\b () ):\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 capsules
\f1\b .
\f0\b0 remove
\f1\b ( 
\f0\b0 position 
\f1\b )\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _capsuleEaten 
\f1\b = 
\f0\b0 position\
      
\f2\i \cf4 # Reset all ghosts' scared timers\
      
\f1\i0\b \cf3 for 
\f0\b0 \cf0 index 
\f1\b \cf3 in 
\f0\b0 \cf0 range
\f1\b ( 
\f0\b0 \cf5 1
\f1\b \cf0 , 
\f0\b0 len
\f1\b ( 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates 
\f1\b ) ):\
        
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 index
\f1\b ].
\f0\b0 scaredTimer 
\f1\b = 
\f0\b0 SCARED_TIME\
  consume 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 consume 
\f1\b )\
\
\cf3 class 
\f0\b0 \cf0 GhostRules
\f1\b : \
  
\f0\b0 \cf2 """\
  These functions dictate how ghosts interact with their environment.\
  """     \
  \cf0 GHOST_SPEED
\f1\b =
\f0\b0 \cf5 1.0               \
  
\f1\b \cf3 def 
\f0\b0 \cf0 getLegalActions
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 ghostIndex 
\f1\b ):\
    
\f0\b0 \cf2 """\
    Ghosts cannot stop, and cannot turn around unless they \
    reach a dead end, but can turn 90 degrees at intersections.\
    """\
    \cf0 conf 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 getGhostState
\f1\b ( 
\f0\b0 ghostIndex 
\f1\b ).
\f0\b0 configuration\
    possibleActions 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 getPossibleActions
\f1\b ( 
\f0\b0 conf
\f1\b , 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 layout
\f1\b .
\f0\b0 walls 
\f1\b )\
    
\f0\b0 reverse 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 reverseDirection
\f1\b ( 
\f0\b0 conf
\f1\b .
\f0\b0 direction 
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 Directions
\f1\b .
\f0\b0 STOP 
\f1\b \cf3 in 
\f0\b0 \cf0 possibleActions
\f1\b :\
      
\f0\b0 possibleActions
\f1\b .
\f0\b0 remove
\f1\b ( 
\f0\b0 Directions
\f1\b .
\f0\b0 STOP 
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 reverse 
\f1\b \cf3 in 
\f0\b0 \cf0 possibleActions 
\f1\b \cf3 and 
\f0\b0 \cf0 len
\f1\b ( 
\f0\b0 possibleActions 
\f1\b ) > 
\f0\b0 \cf5 1
\f1\b \cf0 :\
      
\f0\b0 possibleActions
\f1\b .
\f0\b0 remove
\f1\b ( 
\f0\b0 reverse 
\f1\b )\
    \cf3 return 
\f0\b0 \cf0 possibleActions\
  getLegalActions 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 getLegalActions 
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 applyAction
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 action
\f1\b , 
\f0\b0 ghostIndex
\f1\b ):\
\
    
\f0\b0 legal 
\f1\b = 
\f0\b0 GhostRules
\f1\b .
\f0\b0 getLegalActions
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 ghostIndex 
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 action 
\f1\b \cf3 not in 
\f0\b0 \cf0 legal
\f1\b :\
      \cf3 raise 
\f0\b0 \cf5 "Illegal ghost action"
\f1\b \cf0 , 
\f0\b0 action\
    \
    ghostState 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 ghostIndex
\f1\b ]\
    
\f0\b0 speed 
\f1\b = 
\f0\b0 GhostRules
\f1\b .
\f0\b0 GHOST_SPEED\
    
\f1\b \cf3 if 
\f0\b0 \cf0 ghostState
\f1\b .
\f0\b0 scaredTimer 
\f1\b > 
\f0\b0 \cf5 0
\f1\b \cf0 : 
\f0\b0 speed 
\f1\b /= 
\f0\b0 \cf5 2.0\
    \cf0 vector 
\f1\b = 
\f0\b0 Actions
\f1\b .
\f0\b0 directionToVector
\f1\b ( 
\f0\b0 action
\f1\b , 
\f0\b0 speed 
\f1\b )\
    
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration 
\f1\b = 
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 generateSuccessor
\f1\b ( 
\f0\b0 vector 
\f1\b )\
  
\f0\b0 applyAction 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 applyAction 
\f1\b )\
    \
  \cf3 def 
\f0\b0 \cf0 decrementTimer
\f1\b ( 
\f0\b0 ghostState
\f1\b ):\
    
\f0\b0 timer 
\f1\b = 
\f0\b0 ghostState
\f1\b .
\f0\b0 scaredTimer\
    
\f1\b \cf3 if 
\f0\b0 \cf0 timer 
\f1\b == 
\f0\b0 \cf5 1
\f1\b \cf0 : \
      
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 pos 
\f1\b = 
\f0\b0 nearestPoint
\f1\b ( 
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 pos 
\f1\b )\
    
\f0\b0 ghostState
\f1\b .
\f0\b0 scaredTimer 
\f1\b = 
\f0\b0 max
\f1\b ( 
\f0\b0 \cf5 0
\f1\b \cf0 , 
\f0\b0 timer 
\f1\b - 
\f0\b0 \cf5 1 
\f1\b \cf0 )\
  
\f0\b0 decrementTimer 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 decrementTimer 
\f1\b )\
      \
  \cf3 def 
\f0\b0 \cf0 checkDeath
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 agentIndex
\f1\b ):\
    
\f0\b0 pacmanPosition 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 getPacmanPosition
\f1\b ()\
    \cf3 if 
\f0\b0 \cf0 agentIndex 
\f1\b == 
\f0\b0 \cf5 0
\f1\b \cf0 : 
\f2\i\b0 \cf4 # Pacman just moved; Anyone can kill him\
      
\f1\i0\b \cf3 for 
\f0\b0 \cf0 index 
\f1\b \cf3 in 
\f0\b0 \cf0 range
\f1\b ( 
\f0\b0 \cf5 1
\f1\b \cf0 , 
\f0\b0 len
\f1\b ( 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates 
\f1\b ) ):\
        
\f0\b0 ghostState 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 index
\f1\b ]\
        
\f0\b0 ghostPosition 
\f1\b = 
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 getPosition
\f1\b ()\
        \cf3 if 
\f0\b0 \cf0 GhostRules
\f1\b .
\f0\b0 canKill
\f1\b ( 
\f0\b0 pacmanPosition
\f1\b , 
\f0\b0 ghostPosition 
\f1\b ):\
          
\f0\b0 GhostRules
\f1\b .
\f0\b0 collide
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 ghostState
\f1\b , 
\f0\b0 index 
\f1\b )\
    \cf3 else\cf0 :\
      
\f0\b0 ghostState 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 agentStates
\f1\b [
\f0\b0 agentIndex
\f1\b ]\
      
\f0\b0 ghostPosition 
\f1\b = 
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration
\f1\b .
\f0\b0 getPosition
\f1\b ()\
      \cf3 if 
\f0\b0 \cf0 GhostRules
\f1\b .
\f0\b0 canKill
\f1\b ( 
\f0\b0 pacmanPosition
\f1\b , 
\f0\b0 ghostPosition 
\f1\b ):\
        
\f0\b0 GhostRules
\f1\b .
\f0\b0 collide
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 ghostState
\f1\b , 
\f0\b0 agentIndex 
\f1\b )  \
  
\f0\b0 checkDeath 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 checkDeath 
\f1\b )\
  \
  \cf3 def 
\f0\b0 \cf0 collide
\f1\b ( 
\f0\b0 state
\f1\b , 
\f0\b0 ghostState
\f1\b , 
\f0\b0 agentIndex
\f1\b ):\
    \cf3 if 
\f0\b0 \cf0 ghostState
\f1\b .
\f0\b0 scaredTimer 
\f1\b > 
\f0\b0 \cf5 0
\f1\b \cf0 :\
      
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange 
\f1\b += 
\f0\b0 \cf5 200\
      \cf0 GhostRules
\f1\b .
\f0\b0 placeGhost
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 ghostState
\f1\b )\
      
\f0\b0 ghostState
\f1\b .
\f0\b0 scaredTimer 
\f1\b = 
\f0\b0 \cf5 0\
      
\f2\i \cf4 # Added for first-person\
      
\f0\i0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _eaten
\f1\b [
\f0\b0 agentIndex
\f1\b ] = \cf3 True\
    else\cf0 :\
      \cf3 if not 
\f0\b0 \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _win
\f1\b :\
        
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 scoreChange 
\f1\b -= 
\f0\b0 \cf5 500\
        \cf0 state
\f1\b .
\f0\b0 data
\f1\b .
\f0\b0 _lose 
\f1\b = \cf3 True\
  
\f0\b0 \cf0 collide 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 collide 
\f1\b )\
\
  \cf3 def 
\f0\b0 \cf0 canKill
\f1\b ( 
\f0\b0 pacmanPosition
\f1\b , 
\f0\b0 ghostPosition 
\f1\b ):\
    \cf3 return 
\f0\b0 \cf0 manhattanDistance
\f1\b ( 
\f0\b0 ghostPosition
\f1\b , 
\f0\b0 pacmanPosition 
\f1\b ) <= 
\f0\b0 COLLISION_TOLERANCE\
  canKill 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 canKill 
\f1\b )\
  \
  \cf3 def 
\f0\b0 \cf0 placeGhost
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 ghostState
\f1\b ):\
    
\f0\b0 ghostState
\f1\b .
\f0\b0 configuration 
\f1\b = 
\f0\b0 ghostState
\f1\b .
\f0\b0 start\
  placeGhost 
\f1\b = 
\f0\b0 staticmethod
\f1\b ( 
\f0\b0 placeGhost 
\f1\b )\
\
\pard\pardeftab720\partightenfactor0

\f2\i\b0 \cf4 #############################\
# FRAMEWORK TO START A GAME #\
#############################\
\
\pard\pardeftab720\partightenfactor0

\f1\i0\b \cf3 def 
\f0\b0 \cf0 default
\f1\b (
\f0\b0 str
\f1\b ):\
  \cf3 return 
\f0\b0 \cf0 str 
\f1\b + 
\f0\b0 \cf5 ' [Default: %default]'\
  \

\f1\b \cf3 def 
\f0\b0 \cf0 parseAgentArgs
\f1\b (
\f0\b0 str
\f1\b ):\
  \cf3 if 
\f0\b0 \cf0 str 
\f1\b == 
\f0\b0 \cf3 None
\f1\b \cf0 : \cf3 return \cf0 \{\}\
  
\f0\b0 pieces 
\f1\b = 
\f0\b0 str
\f1\b .
\f0\b0 split
\f1\b (
\f0\b0 \cf5 ','
\f1\b \cf0 )\
  
\f0\b0 opts 
\f1\b = \{\}\
  \cf3 for 
\f0\b0 \cf0 p 
\f1\b \cf3 in 
\f0\b0 \cf0 pieces
\f1\b :\
    \cf3 if 
\f0\b0 \cf5 '=' 
\f1\b \cf3 in 
\f0\b0 \cf0 p
\f1\b :      \
      
\f0\b0 key
\f1\b , 
\f0\b0 val 
\f1\b = 
\f0\b0 p
\f1\b .
\f0\b0 split
\f1\b (
\f0\b0 \cf5 '='
\f1\b \cf0 )\
    \cf3 else\cf0 :\
      
\f0\b0 key
\f1\b ,
\f0\b0 val 
\f1\b = 
\f0\b0 p
\f1\b , 
\f0\b0 \cf5 1\
    \cf0 opts
\f1\b [
\f0\b0 key
\f1\b ] = 
\f0\b0 val\
  
\f1\b \cf3 return 
\f0\b0 \cf0 opts\
  \

\f1\b \cf3 def 
\f0\b0 \cf0 readCommand
\f1\b ( 
\f0\b0 argv 
\f1\b ):\
  
\f0\b0 \cf2 """\
  Processes the command used to run pacman from the command line.\
  """\
  
\f1\b \cf3 from 
\f0\b0 \cf0 optparse 
\f1\b \cf3 import 
\f0\b0 \cf0 OptionParser\
  usageStr 
\f1\b = 
\f0\b0 \cf2 """\
  USAGE:      python pacman.py <options>\
  EXAMPLES:   (1) python pacman.py\
                  - starts an interactive game\
              (2) python pacman.py --layout smallClassic --zoom 2\
              OR  python pacman.py -l smallClassic -z 2\
                  - starts an interactive game on a smaller board, zoomed in\
  """\
  \cf0 parser 
\f1\b = 
\f0\b0 OptionParser
\f1\b (
\f0\b0 usageStr
\f1\b )\
  \
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-n'
\f1\b \cf0 , 
\f0\b0 \cf5 '--numGames'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'numGames'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'int'
\f1\b \cf0 ,\
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'the number of GAMES to play'
\f1\b \cf0 ), 
\f0\b0 metavar
\f1\b =
\f0\b0 \cf5 'GAMES'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 1
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-l'
\f1\b \cf0 , 
\f0\b0 \cf5 '--layout'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'layout'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'the LAYOUT_FILE from which to load the map layout'
\f1\b \cf0 ), \
                    
\f0\b0 metavar
\f1\b =
\f0\b0 \cf5 'LAYOUT_FILE'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 'mediumClassic'
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-p'
\f1\b \cf0 , 
\f0\b0 \cf5 '--pacman'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'pacman'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'the agent TYPE in the pacmanAgents module to use'
\f1\b \cf0 ), \
                    
\f0\b0 metavar
\f1\b =
\f0\b0 \cf5 'TYPE'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 'KeyboardAgent'
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-d'
\f1\b \cf0 , 
\f0\b0 \cf5 '--depth'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'depth'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'int'
\f1\b \cf0 ,\
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'the search DEPTH passed to the agent'
\f1\b \cf0 ), 
\f0\b0 metavar
\f1\b =
\f0\b0 \cf5 'DEPTH'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 2
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-b'
\f1\b \cf0 , 
\f0\b0 \cf5 '--betterEvaluation'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'betterEval'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'Use the betterEvaluationFunction instead of scoreEvaluationFunction'
\f1\b \cf0 ), \
                    
\f0\b0 action
\f1\b =
\f0\b0 \cf5 'store_true'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =\cf3 False\cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-t'
\f1\b \cf0 , 
\f0\b0 \cf5 '--textGraphics'
\f1\b \cf0 , 
\f0\b0 action
\f1\b =
\f0\b0 \cf5 'store_true'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'textGraphics'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Display output as text only'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =\cf3 False\cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-q'
\f1\b \cf0 , 
\f0\b0 \cf5 '--quietTextGraphics'
\f1\b \cf0 , 
\f0\b0 action
\f1\b =
\f0\b0 \cf5 'store_true'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'quietGraphics'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Generate minimal output and no graphics'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =\cf3 False\cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '--textGraphicsDelay'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'float'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'delay'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Pause length between moves in the text display'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 0.1
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-g'
\f1\b \cf0 , 
\f0\b0 \cf5 '--ghosts'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'ghost'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'the ghost agent TYPE in the ghostAgents module to use'
\f1\b \cf0 ), \
                    
\f0\b0 metavar 
\f1\b = 
\f0\b0 \cf5 'TYPE'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 'RandomGhost'
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-k'
\f1\b \cf0 , 
\f0\b0 \cf5 '--numghosts'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'int'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'numGhosts'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'The maximum number of ghosts to use'
\f1\b \cf0 ), 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 4
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-z'
\f1\b \cf0 , 
\f0\b0 \cf5 '--zoom'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'float'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'zoom'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'Zoom the size of the graphics window'
\f1\b \cf0 ), 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 1.0
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-f'
\f1\b \cf0 , 
\f0\b0 \cf5 '--fixRandomSeed'
\f1\b \cf0 , 
\f0\b0 action
\f1\b =
\f0\b0 \cf5 'store_true'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'fixRandomSeed'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Fixes the random seed to always play the same game'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =\cf3 False\cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-r'
\f1\b \cf0 , 
\f0\b0 \cf5 '--recordActions'
\f1\b \cf0 , 
\f0\b0 action
\f1\b =
\f0\b0 \cf5 'store_true'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'record'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Writes game histories to a file (named by the time they were played)'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =\cf3 False\cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '--replay'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'gameToReplay'
\f1\b \cf0 , \
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'A recorded game file (pickle) to replay'
\f1\b \cf0 , 
\f0\b0 default
\f1\b =
\f0\b0 \cf3 None
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-a'
\f1\b \cf0 ,
\f0\b0 \cf5 '--agentArgs'
\f1\b \cf0 ,
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'agentArgs'
\f1\b \cf0 ,\
                    
\f0\b0 help
\f1\b =
\f0\b0 \cf5 'Comma seperated values sent to agent. e.g. "opt1=val1,opt2,opt3=val3"'
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-x'
\f1\b \cf0 , 
\f0\b0 \cf5 '--numQuiet'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'numQuiet'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'int'
\f1\b \cf0 ,\
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'How many episodes to suppress GUI for'
\f1\b \cf0 ), 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 0
\f1\b \cf0 )\
  
\f0\b0 parser
\f1\b .
\f0\b0 add_option
\f1\b (
\f0\b0 \cf5 '-i'
\f1\b \cf0 , 
\f0\b0 \cf5 '--numIgnore'
\f1\b \cf0 , 
\f0\b0 dest
\f1\b =
\f0\b0 \cf5 'numIgnore'
\f1\b \cf0 , 
\f0\b0 type
\f1\b =
\f0\b0 \cf5 'int'
\f1\b \cf0 ,\
                    
\f0\b0 help
\f1\b =
\f0\b0 default
\f1\b (
\f0\b0 \cf5 'How many games to ignore for reporting average'
\f1\b \cf0 ), 
\f0\b0 default
\f1\b =
\f0\b0 \cf5 0
\f1\b \cf0 )\
\
  
\f0\b0 options
\f1\b , 
\f0\b0 otherjunk 
\f1\b = 
\f0\b0 parser
\f1\b .
\f0\b0 parse_args
\f1\b ()\
  \cf3 if 
\f0\b0 \cf0 len
\f1\b (
\f0\b0 otherjunk
\f1\b ) != 
\f0\b0 \cf5 0
\f1\b \cf0 : \
    \cf3 raise 
\f0\b0 \cf0 Exception
\f1\b (
\f0\b0 \cf5 'Command line input not understood: ' 
\f1\b \cf0 + 
\f0\b0 str
\f1\b (
\f0\b0 otherjunk
\f1\b ))\
  
\f0\b0 args 
\f1\b = 
\f0\b0 dict
\f1\b ()\
  
\f2\i\b0 \cf4 # Fix the random seed\
  
\f1\i0\b \cf3 if 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 fixRandomSeed
\f1\b : 
\f0\b0 random
\f1\b .
\f0\b0 seed
\f1\b (
\f0\b0 \cf5 'cs188'
\f1\b \cf0 )  \
  
\f2\i\b0 \cf4 # Choose a layout\
  
\f0\i0 \cf0 args
\f1\b [
\f0\b0 \cf5 'layout'
\f1\b \cf0 ] = 
\f0\b0 layout
\f1\b .
\f0\b0 getLayout
\f1\b ( 
\f0\b0 options
\f1\b .
\f0\b0 layout 
\f1\b )\
  \cf3 if 
\f0\b0 \cf0 args
\f1\b [
\f0\b0 \cf5 'layout'
\f1\b \cf0 ] == 
\f0\b0 \cf3 None
\f1\b \cf0 : \cf3 raise 
\f0\b0 \cf5 "The layout " 
\f1\b \cf0 + 
\f0\b0 options
\f1\b .
\f0\b0 layout 
\f1\b + 
\f0\b0 \cf5 " cannot be found"\
  \
  
\f2\i \cf4 # Choose a pacman agent\
  
\f0\i0 \cf0 noKeyboard 
\f1\b = 
\f0\b0 options
\f1\b .
\f0\b0 gameToReplay 
\f1\b == 
\f0\b0 \cf3 None 
\f1\b and \cf0 (
\f0\b0 options
\f1\b .
\f0\b0 textGraphics 
\f1\b \cf3 or 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 quietGraphics
\f1\b )\
  
\f0\b0 pacmanType 
\f1\b = 
\f0\b0 loadAgent
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 pacman
\f1\b , 
\f0\b0 noKeyboard
\f1\b )\
  
\f0\b0 agentOpts 
\f1\b = 
\f0\b0 parseAgentArgs
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 agentArgs
\f1\b )\
  
\f0\b0 pacman 
\f1\b = 
\f0\b0 pacmanType
\f1\b (**
\f0\b0 agentOpts
\f1\b ) 
\f2\i\b0 \cf4 # Instantiate pacman with agentArgs\
  
\f1\i0\b \cf3 if 
\f0\b0 \cf5 'setDepth' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 pacman
\f1\b ): 
\f0\b0 pacman
\f1\b .
\f0\b0 setDepth
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 depth
\f1\b )\
  \cf3 if 
\f0\b0 \cf5 'useBetterEvaluation' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 pacman
\f1\b ) \cf3 and 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 betterEval
\f1\b : 
\f0\b0 pacman
\f1\b .
\f0\b0 useBetterEvaluation
\f1\b ()\
  \cf3 if 
\f0\b0 \cf5 'setOptions' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 pacman
\f1\b ) \cf3 and 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 agentArgs
\f1\b : \
    
\f0\b0 pacman
\f1\b .
\f0\b0 setOptions
\f1\b ()\
    
\f2\i\b0 \cf4 # HACK for reinforcement project\
    
\f1\i0\b \cf3 if 
\f0\b0 \cf5 'numTrain' 
\f1\b \cf3 in 
\f0\b0 \cf0 agentOpts
\f1\b :\
      
\f0\b0 options
\f1\b .
\f0\b0 numQuiet 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 agentOpts
\f1\b [
\f0\b0 \cf5 'numTrain'
\f1\b \cf0 ])\
      
\f0\b0 options
\f1\b .
\f0\b0 numIgnore 
\f1\b = 
\f0\b0 int
\f1\b (
\f0\b0 agentOpts
\f1\b [
\f0\b0 \cf5 'numTrain'
\f1\b \cf0 ])\
  \cf3 try\cf0 :\
    \cf3 import 
\f0\b0 \cf0 evaluation\
    
\f1\b \cf3 if 
\f0\b0 \cf5 'setEvaluation' 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 pacman
\f1\b ):\
      
\f0\b0 evalFn 
\f1\b = 
\f0\b0 getattr
\f1\b (
\f0\b0 evaluation
\f1\b , 
\f0\b0 options
\f1\b .
\f0\b0 evaluationFn
\f1\b ) \
      
\f0\b0 pacman
\f1\b .
\f0\b0 setEvaluation
\f1\b (
\f0\b0 evalFn
\f1\b )\
  \cf3 except 
\f0\b0 \cf0 ImportError
\f1\b : \
    \cf3 pass\
  
\f0\b0 \cf0 args
\f1\b [
\f0\b0 \cf5 'pacman'
\f1\b \cf0 ] = 
\f0\b0 pacman\
    \
  
\f2\i \cf4 # Choose a ghost agent\
  
\f1\i0\b \cf3 import 
\f0\b0 \cf0 ghostAgents\
  ghostType 
\f1\b = 
\f0\b0 loadAgent
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 ghost
\f1\b , 
\f0\b0 noKeyboard
\f1\b )\
  
\f2\i\b0 \cf4 #getattr(ghostAgents, options.ghost)\
  
\f0\i0 \cf0 args
\f1\b [
\f0\b0 \cf5 'ghosts'
\f1\b \cf0 ] = [
\f0\b0 ghostType
\f1\b ( 
\f0\b0 i
\f1\b +
\f0\b0 \cf5 1 
\f1\b \cf0 ) \cf3 for 
\f0\b0 \cf0 i 
\f1\b \cf3 in 
\f0\b0 \cf0 range
\f1\b ( 
\f0\b0 options
\f1\b .
\f0\b0 numGhosts 
\f1\b )]\
  
\f2\i\b0 \cf4 # Choose a display format\
  
\f1\i0\b \cf3 if 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 quietGraphics
\f1\b :\
      \cf3 import 
\f0\b0 \cf0 textDisplay\
      args
\f1\b [
\f0\b0 \cf5 'display'
\f1\b \cf0 ] = 
\f0\b0 textDisplay
\f1\b .
\f0\b0 NullGraphics
\f1\b ()\
  \cf3 elif 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 textGraphics
\f1\b :\
    \cf3 import 
\f0\b0 \cf0 textDisplay\
    textDisplay
\f1\b .
\f0\b0 SLEEP_TIME 
\f1\b = 
\f0\b0 options
\f1\b .
\f0\b0 delay\
    args
\f1\b [
\f0\b0 \cf5 'display'
\f1\b \cf0 ] = 
\f0\b0 textDisplay
\f1\b .
\f0\b0 PacmanGraphics
\f1\b ()      \
  \cf3 else\cf0 :\
    \cf3 import 
\f0\b0 \cf0 graphicsDisplay\
    args
\f1\b [
\f0\b0 \cf5 'display'
\f1\b \cf0 ] = 
\f0\b0 graphicsDisplay
\f1\b .
\f0\b0 PacmanGraphics
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 zoom
\f1\b )\
  
\f0\b0 args
\f1\b [
\f0\b0 \cf5 'numGames'
\f1\b \cf0 ] = 
\f0\b0 options
\f1\b .
\f0\b0 numGames\
  args
\f1\b [
\f0\b0 \cf5 'record'
\f1\b \cf0 ] = 
\f0\b0 options
\f1\b .
\f0\b0 record\
  \
  
\f2\i \cf4 # Special case: recorded games don't use the runGames method or args structure\
  
\f1\i0\b \cf3 if 
\f0\b0 \cf0 options
\f1\b .
\f0\b0 gameToReplay 
\f1\b != 
\f0\b0 \cf3 None
\f1\b \cf0 :\
    \cf3 print 
\f0\b0 \cf5 'Replaying recorded game %s.' 
\f1\b \cf0 % 
\f0\b0 options
\f1\b .
\f0\b0 gameToReplay\
    
\f1\b \cf3 import 
\f0\b0 \cf0 cPickle\
    recorded 
\f1\b = 
\f0\b0 cPickle
\f1\b .
\f0\b0 load
\f1\b (
\f0\b0 open
\f1\b (
\f0\b0 options
\f1\b .
\f0\b0 gameToReplay
\f1\b ))\
    
\f0\b0 recorded
\f1\b [
\f0\b0 \cf5 'display'
\f1\b \cf0 ] = 
\f0\b0 args
\f1\b [
\f0\b0 \cf5 'display'
\f1\b \cf0 ]\
    
\f0\b0 replayGame
\f1\b (**
\f0\b0 recorded
\f1\b )\
    
\f0\b0 sys
\f1\b .
\f0\b0 exit
\f1\b (
\f0\b0 \cf5 0
\f1\b \cf0 )\
\
  
\f0\b0 args
\f1\b [
\f0\b0 \cf5 'numQuiet'
\f1\b \cf0 ] = 
\f0\b0 options
\f1\b .
\f0\b0 numQuiet\
  
\f1\b \cf3 return 
\f0\b0 \cf0 args\
\

\f1\b \cf3 def 
\f0\b0 \cf0 loadAgent
\f1\b (
\f0\b0 pacman
\f1\b , 
\f0\b0 nographics
\f1\b ):\
  \cf3 import 
\f0\b0 \cf0 os\
  
\f2\i \cf4 # Changed to look at all pythonPath Directories for the right module,\
  # as well as the current directory\
  # moduleNames = [f for f in os.listdir('.') if f.endswith('gents.py')]\
  # moduleNames += ['searchAgents.py', 'multiAgents.py']\
  # Check PYTHONPATH for directories\
  
\f0\i0 \cf0 pythonPathStr 
\f1\b = 
\f0\b0 os
\f1\b .
\f0\b0 path
\f1\b .
\f0\b0 expandvars
\f1\b (
\f0\b0 \cf5 "$PYTHONPATH"
\f1\b \cf0 )\
  \cf3 if 
\f0\b0 \cf0 pythonPathStr
\f1\b .
\f0\b0 find
\f1\b (
\f0\b0 \cf5 ';'
\f1\b \cf0 ) == -
\f0\b0 \cf5 1
\f1\b \cf0 :\
    
\f0\b0 pythonPathDirs 
\f1\b = 
\f0\b0 pythonPathStr
\f1\b .
\f0\b0 split
\f1\b (
\f0\b0 \cf5 ':'
\f1\b \cf0 )\
  \cf3 else\cf0 :\
    
\f0\b0 pythonPathDirs 
\f1\b = 
\f0\b0 pythonPathStr
\f1\b .
\f0\b0 split
\f1\b (
\f0\b0 \cf5 ';'
\f1\b \cf0 )\
  
\f2\i\b0 \cf4 #print pythonPathDirs\
  # And Current Directory\
  
\f0\i0 \cf0 pythonPathDirs
\f1\b .
\f0\b0 append
\f1\b (
\f0\b0 \cf5 '.'
\f1\b \cf0 )\
  \cf3 for 
\f0\b0 \cf0 moduleDir 
\f1\b \cf3 in 
\f0\b0 \cf0 pythonPathDirs
\f1\b :\
    \cf3 if not 
\f0\b0 \cf0 os
\f1\b .
\f0\b0 path
\f1\b .
\f0\b0 isdir
\f1\b (
\f0\b0 moduleDir
\f1\b ): \cf3 continue\
    
\f0\b0 \cf0 moduleNames 
\f1\b = [
\f0\b0 f 
\f1\b \cf3 for 
\f0\b0 \cf0 f 
\f1\b \cf3 in 
\f0\b0 \cf0 os
\f1\b .
\f0\b0 listdir
\f1\b (
\f0\b0 moduleDir
\f1\b ) \cf3 if 
\f0\b0 \cf0 f
\f1\b .
\f0\b0 endswith
\f1\b (
\f0\b0 \cf5 'gents.py'
\f1\b \cf0 )]\
    \cf3 for 
\f0\b0 \cf0 modulename 
\f1\b \cf3 in 
\f0\b0 \cf0 moduleNames
\f1\b :\
      \cf3 try\cf0 :\
        
\f0\b0 module 
\f1\b = 
\f0\b0 __import__
\f1\b (
\f0\b0 modulename
\f1\b [:-
\f0\b0 \cf5 3
\f1\b \cf0 ])\
      \cf3 except 
\f0\b0 \cf0 ImportError
\f1\b : \
        \cf3 continue\
      if 
\f0\b0 \cf0 pacman 
\f1\b \cf3 in 
\f0\b0 \cf0 dir
\f1\b (
\f0\b0 module
\f1\b ):\
        \cf3 if 
\f0\b0 \cf0 nographics 
\f1\b \cf3 and 
\f0\b0 \cf0 modulename 
\f1\b == 
\f0\b0 \cf5 'keyboardAgents.py'
\f1\b \cf0 :\
          \cf3 raise 
\f0\b0 \cf5 'Using the keyboard requires graphics (not text display)'\
        
\f1\b \cf3 return 
\f0\b0 \cf0 getattr
\f1\b (
\f0\b0 module
\f1\b , 
\f0\b0 pacman
\f1\b )\
  \cf3 raise 
\f0\b0 \cf5 'The agent ' 
\f1\b \cf0 + 
\f0\b0 pacman 
\f1\b + 
\f0\b0 \cf5 ' is not specified in any *Agents.py.'\
    \
  \
\

\f1\b \cf3 def 
\f0\b0 \cf0 replayGame
\f1\b ( 
\f0\b0 layout
\f1\b , 
\f0\b0 agents
\f1\b , 
\f0\b0 actions
\f1\b , 
\f0\b0 display 
\f1\b ):\
    
\f0\b0 rules 
\f1\b = 
\f0\b0 ClassicGameRules
\f1\b ()\
    
\f0\b0 game 
\f1\b = 
\f0\b0 rules
\f1\b .
\f0\b0 newGame
\f1\b ( 
\f0\b0 layout
\f1\b , 
\f0\b0 agents
\f1\b [
\f0\b0 \cf5 0
\f1\b \cf0 ], 
\f0\b0 agents
\f1\b [
\f0\b0 \cf5 1
\f1\b \cf0 :], 
\f0\b0 display 
\f1\b )   \
    
\f0\b0 state 
\f1\b = 
\f0\b0 game
\f1\b .
\f0\b0 state\
    display
\f1\b .
\f0\b0 initialize
\f1\b (
\f0\b0 state
\f1\b .
\f0\b0 data
\f1\b )\
    \
    \cf3 for 
\f0\b0 \cf0 action 
\f1\b \cf3 in 
\f0\b0 \cf0 actions
\f1\b :\
      
\f2\i\b0 \cf4 # Execute the action\
      
\f0\i0 \cf0 state 
\f1\b = 
\f0\b0 state
\f1\b .
\f0\b0 generateSuccessor
\f1\b ( *
\f0\b0 action 
\f1\b )\
      
\f2\i\b0 \cf4 # Change the display\
      
\f0\i0 \cf0 display
\f1\b .
\f0\b0 update
\f1\b ( 
\f0\b0 state
\f1\b .
\f0\b0 data 
\f1\b )\
      
\f2\i\b0 \cf4 # Allow for game specific conditions (winning, losing, etc.)\
      
\f0\i0 \cf0 rules
\f1\b .
\f0\b0 process
\f1\b (
\f0\b0 state
\f1\b , 
\f0\b0 game
\f1\b )\
    \
    
\f0\b0 display
\f1\b .
\f0\b0 finish
\f1\b ()\
\
\
\cf3 def 
\f0\b0 \cf0 runGames
\f1\b ( 
\f0\b0 layout
\f1\b , 
\f0\b0 pacman
\f1\b , 
\f0\b0 ghosts
\f1\b , 
\f0\b0 display
\f1\b , 
\f0\b0 numGames
\f1\b , 
\f0\b0 record
\f1\b , 
\f0\b0 numQuiet 
\f1\b = 
\f0\b0 \cf5 0
\f1\b \cf0 , 
\f0\b0 numIgnore 
\f1\b = 
\f0\b0 \cf5 0 
\f1\b \cf0 ):\
  \cf3 import 
\f0\b0 \cf0 __main__\
  __main__
\f1\b .
\f0\b0 __dict__
\f1\b [
\f0\b0 \cf5 '_display'
\f1\b \cf0 ] = 
\f0\b0 display\
    \
  rules 
\f1\b = 
\f0\b0 ClassicGameRules
\f1\b ()\
  
\f0\b0 games 
\f1\b = []\
  \
  \cf3 for 
\f0\b0 \cf0 i 
\f1\b \cf3 in 
\f0\b0 \cf0 range
\f1\b ( 
\f0\b0 numGames 
\f1\b ):\
    
\f2\i\b0 \cf4 # Supress GUI if < numQuiet\
    
\f0\i0 \cf0 beQuiet 
\f1\b = 
\f0\b0 i 
\f1\b < 
\f0\b0 numQuiet\
    
\f1\b \cf3 if 
\f0\b0 \cf0 beQuiet
\f1\b :\
        \cf3 import 
\f0\b0 \cf0 textDisplay        \
        gameDisplay 
\f1\b = 
\f0\b0 textDisplay
\f1\b .
\f0\b0 NoGraphics
\f1\b ()\
        
\f0\b0 rules
\f1\b .
\f0\b0 quiet 
\f1\b = \cf3 True\
    else\cf0 :\
        
\f0\b0 gameDisplay 
\f1\b = 
\f0\b0 display\
        rules
\f1\b .
\f0\b0 quiet 
\f1\b = \cf3 False    \
    
\f0\b0 \cf0 game 
\f1\b = 
\f0\b0 rules
\f1\b .
\f0\b0 newGame
\f1\b ( 
\f0\b0 layout
\f1\b , 
\f0\b0 pacman
\f1\b , 
\f0\b0 ghosts
\f1\b , 
\f0\b0 gameDisplay
\f1\b , 
\f0\b0 beQuiet 
\f1\b )              \
    
\f0\b0 game
\f1\b .
\f0\b0 run
\f1\b ()\
    \cf3 if 
\f0\b0 \cf0 i 
\f1\b >= 
\f0\b0 numIgnore
\f1\b : 
\f0\b0 games
\f1\b .
\f0\b0 append
\f1\b (
\f0\b0 game
\f1\b )\
    \cf3 if 
\f0\b0 \cf0 record
\f1\b :\
      \cf3 import 
\f0\b0 \cf0 time
\f1\b , 
\f0\b0 cPickle\
      fname 
\f1\b = (
\f0\b0 \cf5 'recorded-game-%d' 
\f1\b \cf0 % (
\f0\b0 i 
\f1\b + 
\f0\b0 \cf5 1
\f1\b \cf0 )) +  
\f0\b0 \cf5 '-'
\f1\b \cf0 .
\f0\b0 join
\f1\b ([
\f0\b0 str
\f1\b (
\f0\b0 t
\f1\b ) \cf3 for 
\f0\b0 \cf0 t 
\f1\b \cf3 in 
\f0\b0 \cf0 time
\f1\b .
\f0\b0 localtime
\f1\b ()[
\f0\b0 \cf5 1
\f1\b \cf0 :
\f0\b0 \cf5 6
\f1\b \cf0 ]])\
      
\f0\b0 f 
\f1\b = 
\f0\b0 file
\f1\b (
\f0\b0 fname
\f1\b , 
\f0\b0 \cf5 'w'
\f1\b \cf0 )\
      
\f0\b0 components 
\f1\b = \{
\f0\b0 \cf5 'layout'
\f1\b \cf0 : 
\f0\b0 layout
\f1\b , 
\f0\b0 \cf5 'agents'
\f1\b \cf0 : 
\f0\b0 game
\f1\b .
\f0\b0 agents
\f1\b , 
\f0\b0 \cf5 'actions'
\f1\b \cf0 : 
\f0\b0 game
\f1\b .
\f0\b0 moveHistory
\f1\b \}\
      
\f0\b0 cPickle
\f1\b .
\f0\b0 dump
\f1\b (
\f0\b0 components
\f1\b , 
\f0\b0 f
\f1\b )\
      
\f0\b0 f
\f1\b .
\f0\b0 close
\f1\b ()\
      \
  \cf3 if 
\f0\b0 \cf0 numGames 
\f1\b > 
\f0\b0 \cf5 1
\f1\b \cf0 :\
    
\f0\b0 scores 
\f1\b = [
\f0\b0 game
\f1\b .
\f0\b0 state
\f1\b .
\f0\b0 getScore
\f1\b () \cf3 for 
\f0\b0 \cf0 game 
\f1\b \cf3 in 
\f0\b0 \cf0 games
\f1\b ]\
    
\f0\b0 wins 
\f1\b = [
\f0\b0 game
\f1\b .
\f0\b0 state
\f1\b .
\f0\b0 isWin
\f1\b () \cf3 for 
\f0\b0 \cf0 game 
\f1\b \cf3 in 
\f0\b0 \cf0 games
\f1\b ]\
    \cf3 print 
\f0\b0 \cf5 'Average Score:'
\f1\b \cf0 , 
\f0\b0 sum
\f1\b (
\f0\b0 scores
\f1\b ) / 
\f0\b0 float
\f1\b (
\f0\b0 len
\f1\b (
\f0\b0 scores
\f1\b )) \
    \cf3 print 
\f0\b0 \cf5 'Scores:       '
\f1\b \cf0 , 
\f0\b0 \cf5 ', '
\f1\b \cf0 .
\f0\b0 join
\f1\b ([
\f0\b0 str
\f1\b (
\f0\b0 score
\f1\b ) \cf3 for 
\f0\b0 \cf0 score 
\f1\b \cf3 in 
\f0\b0 \cf0 scores
\f1\b ])\
    \cf3 print 
\f0\b0 \cf5 'Win Rate:     '
\f1\b \cf0 , 
\f0\b0 wins
\f1\b .
\f0\b0 count
\f1\b (\cf3 True\cf0 ) / 
\f0\b0 float
\f1\b (
\f0\b0 len
\f1\b (
\f0\b0 wins
\f1\b ))\
    \cf3 print 
\f0\b0 \cf5 'Record:       '
\f1\b \cf0 , 
\f0\b0 \cf5 ', '
\f1\b \cf0 .
\f0\b0 join
\f1\b ([ [
\f0\b0 \cf5 'Loss'
\f1\b \cf0 , 
\f0\b0 \cf5 'Win'
\f1\b \cf0 ][
\f0\b0 int
\f1\b (
\f0\b0 w
\f1\b )] \cf3 for 
\f0\b0 \cf0 w 
\f1\b \cf3 in 
\f0\b0 \cf0 wins
\f1\b ])\
    \
  \cf3 return 
\f0\b0 \cf0 games\
  \

\f1\b \cf3 if 
\f0\b0 \cf0 __name__ 
\f1\b == 
\f0\b0 \cf5 '__main__'
\f1\b \cf0 :\
  
\f0\b0 \cf2 """\
  The main function called when pacman.py is run\
  from the command line:\
\
  > python pacman.py\
\
  See the usage string for more details.\
\
  > python pacman.py --help\
  """\
  \cf0 args 
\f1\b = 
\f0\b0 readCommand
\f1\b ( 
\f0\b0 sys
\f1\b .
\f0\b0 argv
\f1\b [
\f0\b0 \cf5 1
\f1\b \cf0 :] ) 
\f2\i\b0 \cf4 # Get game components based on input\
  
\f0\i0 \cf0 runGames
\f1\b ( **
\f0\b0 args 
\f1\b ) }