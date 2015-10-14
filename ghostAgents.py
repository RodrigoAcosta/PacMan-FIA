{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red15\green112\blue1;\red251\green0\blue7;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Agent\

\f0\b \cf2 import 
\f1\b0 \cf0 random\

\f0\b \cf2 from 
\f1\b0 \cf0 util 
\f0\b \cf2 import 
\f1\b0 \cf0 chooseFromDistribution\

\f0\b \cf2 from 
\f1\b0 \cf0 util 
\f0\b \cf2 import 
\f1\b0 \cf0 manhattanDistance\

\f0\b \cf2 from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Actions\
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 # John:  Change to a superclass (in pacman.py) that always chooses an action from a distribution, \
#        and let different policies be reflected in the distributions.\
#        Also, change pacman.py to search for ghost agents in all *Agents.py files.\
\
\pard\pardeftab720\partightenfactor0

\f0\i0\b \cf2 class 
\f1\b0 \cf0 RandomGhost
\f0\b ( 
\f1\b0 Agent 
\f0\b ):\
  \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 index 
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b = 
\f1\b0 index\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getAction
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state 
\f0\b ):\
    \cf2 return 
\f1\b0 \cf0 random
\f0\b .
\f1\b0 choice
\f0\b ( 
\f1\b0 state
\f0\b .
\f1\b0 getLegalActions
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b ) )\
  \
  \cf2 def 
\f1\b0 \cf0 getDistribution
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state 
\f0\b ):\
    
\f1\b0 actions 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getLegalActions
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b )\
    
\f1\b0 prob 
\f0\b = 
\f1\b0 \cf4 1.0 
\f0\b \cf0 / 
\f1\b0 len
\f0\b ( 
\f1\b0 actions 
\f0\b )\
    \cf2 return \cf0 [( 
\f1\b0 prob
\f0\b , 
\f1\b0 action 
\f0\b ) \cf2 for 
\f1\b0 \cf0 action 
\f0\b \cf2 in 
\f1\b0 \cf0 actions
\f0\b ]\
\
\cf2 class 
\f1\b0 \cf0 DirectionalGhost
\f0\b ( 
\f1\b0 Agent 
\f0\b ):\
  \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 index
\f0\b , 
\f1\b0 prob_attack
\f0\b =
\f1\b0 \cf4 0.8
\f0\b \cf0 , 
\f1\b0 prob_scaredFlee
\f0\b =
\f1\b0 \cf4 0.1 
\f0\b \cf0 ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b = 
\f1\b0 index\
    \cf2 self
\f0\b \cf0 .
\f1\b0 prob_attack 
\f0\b = 
\f1\b0 prob_attack\
    \cf2 self
\f0\b \cf0 .
\f1\b0 prob_scaredFlee 
\f0\b = 
\f1\b0 prob_scaredFlee\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getAction
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state 
\f0\b ):\
    
\f1\b0 dist 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDistribution
\f0\b ( 
\f1\b0 state 
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 chooseFromDistribution
\f0\b ( 
\f1\b0 dist 
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 getDistribution
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state 
\f0\b ):\
    
\f2\i\b0 \cf3 # Read variables from state\
    
\f1\i0 \cf0 ghostState 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getGhostState
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b )\
    
\f1\b0 legalActions 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getLegalActions
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b )\
    
\f1\b0 pos 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getGhostPosition
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b )\
    
\f1\b0 isScared 
\f0\b = 
\f1\b0 ghostState
\f0\b .
\f1\b0 scaredTimer 
\f0\b > 
\f1\b0 \cf4 0\
    \
    \cf0 speed 
\f0\b = 
\f1\b0 \cf4 1\
    
\f0\b \cf2 if 
\f1\b0 \cf0 isScared
\f0\b : 
\f1\b0 speed 
\f0\b = 
\f1\b0 \cf4 0.5\
    \
    \cf0 actionVectors 
\f0\b = [
\f1\b0 Actions
\f0\b .
\f1\b0 directionToVector
\f0\b ( 
\f1\b0 a
\f0\b , 
\f1\b0 speed 
\f0\b ) \cf2 for 
\f1\b0 \cf0 a 
\f0\b \cf2 in 
\f1\b0 \cf0 legalActions
\f0\b ]\
    
\f1\b0 newPositions 
\f0\b = [( 
\f1\b0 pos
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ]+
\f1\b0 a
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ], 
\f1\b0 pos
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ]+
\f1\b0 a
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] ) \cf2 for 
\f1\b0 \cf0 a 
\f0\b \cf2 in 
\f1\b0 \cf0 actionVectors
\f0\b ]\
    
\f1\b0 pacman_pos 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getPacmanPosition
\f0\b ()\
\
    
\f2\i\b0 \cf3 # Select best actions given the state\
    
\f1\i0 \cf0 distancesToPacman 
\f0\b = [
\f1\b0 manhattanDistance
\f0\b ( 
\f1\b0 pos
\f0\b , 
\f1\b0 pacman_pos 
\f0\b ) \cf2 for 
\f1\b0 \cf0 pos 
\f0\b \cf2 in 
\f1\b0 \cf0 newPositions
\f0\b ]\
    \cf2 if 
\f1\b0 \cf0 isScared
\f0\b :\
      
\f1\b0 bestScore 
\f0\b = 
\f1\b0 max
\f0\b ( 
\f1\b0 distancesToPacman 
\f0\b )\
      
\f1\b0 bestProb 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 prob_scaredFlee\
    
\f0\b \cf2 else\cf0 :\
      
\f1\b0 bestScore 
\f0\b = 
\f1\b0 min
\f0\b ( 
\f1\b0 distancesToPacman 
\f0\b )\
      
\f1\b0 bestProb 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 prob_attack\
    bestActions 
\f0\b = [
\f1\b0 action 
\f0\b \cf2 for 
\f1\b0 \cf0 action
\f0\b , 
\f1\b0 distance 
\f0\b \cf2 in 
\f1\b0 \cf0 zip
\f0\b ( 
\f1\b0 legalActions
\f0\b , 
\f1\b0 distancesToPacman 
\f0\b ) \cf2 if 
\f1\b0 \cf0 distance 
\f0\b == 
\f1\b0 bestScore
\f0\b ]\
    \
    
\f2\i\b0 \cf3 # Construct distribution\
    
\f1\i0 \cf0 numBest 
\f0\b = 
\f1\b0 len
\f0\b ( 
\f1\b0 bestActions 
\f0\b )\
    
\f1\b0 distribution 
\f0\b = [( 
\f1\b0 bestProb 
\f0\b / 
\f1\b0 numBest
\f0\b , 
\f1\b0 action 
\f0\b ) \cf2 for 
\f1\b0 \cf0 action 
\f0\b \cf2 in 
\f1\b0 \cf0 bestActions
\f0\b ]\
    
\f1\b0 numActions 
\f0\b = 
\f1\b0 len
\f0\b ( 
\f1\b0 legalActions 
\f0\b )\
    
\f1\b0 distribution 
\f0\b += [( ( 
\f1\b0 \cf4 1
\f0\b \cf0 -
\f1\b0 bestProb 
\f0\b ) / 
\f1\b0 numActions
\f0\b , 
\f1\b0 action 
\f0\b ) \cf2 for 
\f1\b0 \cf0 action 
\f0\b \cf2 in 
\f1\b0 \cf0 legalActions
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 distribution}