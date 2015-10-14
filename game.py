{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red15\green112\blue1;\red118\green0\blue2;
\red251\green0\blue7;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
from 
\f1\b0 \cf0 util 
\f0\b \cf2 import \cf0 *\
\cf2 from 
\f1\b0 \cf0 util 
\f0\b \cf2 import 
\f1\b0 \cf0 raiseNotDefined\

\f0\b \cf2 import 
\f1\b0 \cf0 time\
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 #######################\
# Parts worth reading #\
#######################\
\
\pard\pardeftab720\partightenfactor0

\f0\i0\b \cf2 class 
\f1\b0 \cf0 Agent
\f0\b :\
  
\f1\b0 \cf4 """\
  An agent must define a getAction method, but may also define the\
  following methods which will be called if they exist:\
  \
  def registerInitialState(self, state): # inspects the starting state\
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 index
\f0\b =
\f1\b0 \cf5 0
\f0\b \cf0 ):\
    
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
    
\f1\b0 \cf4 """\
    The Agent will receive a GameState (from either \{pacman, capture, sonar\}.py) and\
    must return an action from Directions.\{North, South, East, West, Stop\}\
    """\
    \cf0 raiseNotDefined
\f0\b ()\
\
\cf2 class 
\f1\b0 \cf0 Directions
\f0\b :\
  
\f1\b0 NORTH 
\f0\b = 
\f1\b0 \cf5 'North'\
  \cf0 SOUTH 
\f0\b = 
\f1\b0 \cf5 'South'\
  \cf0 EAST 
\f0\b = 
\f1\b0 \cf5 'East'\
  \cf0 WEST 
\f0\b = 
\f1\b0 \cf5 'West'\
  \cf0 STOP 
\f0\b = 
\f1\b0 \cf5 'Stop'\
  \
  \cf0 LEFT 
\f0\b =       \{
\f1\b0 NORTH
\f0\b : 
\f1\b0 WEST
\f0\b ,\
                 
\f1\b0 SOUTH
\f0\b : 
\f1\b0 EAST
\f0\b ,\
                 
\f1\b0 EAST
\f0\b :  
\f1\b0 NORTH
\f0\b ,\
                 
\f1\b0 WEST
\f0\b :  
\f1\b0 SOUTH
\f0\b ,\
                 
\f1\b0 STOP
\f0\b :  
\f1\b0 STOP
\f0\b \}\
  \
  
\f1\b0 RIGHT 
\f0\b =      
\f1\b0 dict
\f0\b ([(
\f1\b0 y
\f0\b ,
\f1\b0 x
\f0\b ) \cf2 for 
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 LEFT
\f0\b .
\f1\b0 items
\f0\b ()])\
\
\cf2 class 
\f1\b0 \cf0 Configuration
\f0\b :\
  
\f1\b0 \cf4 """\
  A Configuration holds the (x,y) coordinate of a character, along with its \
  traveling direction.\
  \
  The convention for positions, like a graph, is that (0,0) is the lower left corner, x increases \
  horizontally and y increases vertically.  Therefore, north is the direction of increasing y, or (0,1).\
  """\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pos
\f0\b , 
\f1\b0 direction
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos 
\f0\b = 
\f1\b0 pos\
    \cf2 self
\f0\b \cf0 .
\f1\b0 direction 
\f0\b = 
\f1\b0 direction\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 getDirection
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 direction\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __eq__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 other
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 other 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return False\
    return \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 pos 
\f0\b \cf2 and 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 direction 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 direction
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 __hash__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 x 
\f0\b = 
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos
\f0\b )\
    
\f1\b0 y 
\f0\b = 
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 direction
\f0\b )\
    
\f2\i\b0 \cf3 #return int(x + 13 * y)\
    
\f0\i0\b \cf2 return 
\f1\b0 \cf0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 __str__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf5 "(x,y)="
\f0\b \cf0 +
\f1\b0 str
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos
\f0\b )+
\f1\b0 \cf5 ", "
\f0\b \cf0 +
\f1\b0 str
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 direction
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 generateSuccessor
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 vector
\f0\b ):\
    
\f1\b0 \cf4 """\
    Generates a new configuration reached by translating the current\
    configuration by the action vector.  This is a low-level call and does\
    not attempt to respect the legality of the movement.\
    \
    Actions are movement vectors.\
    """\
    \cf0 x
\f0\b , 
\f1\b0 y
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pos\
    dx
\f0\b , 
\f1\b0 dy 
\f0\b = 
\f1\b0 vector\
    direction 
\f0\b = 
\f1\b0 Actions
\f0\b .
\f1\b0 vectorToDirection
\f0\b (
\f1\b0 vector
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 direction 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP
\f0\b : \
      
\f1\b0 direction 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 direction 
\f2\i \cf3 # There is no stop direction\
    
\f0\i0\b \cf2 return 
\f1\b0 \cf0 Configuration
\f0\b ((
\f1\b0 x 
\f0\b + 
\f1\b0 dx
\f0\b , 
\f1\b0 y
\f0\b +
\f1\b0 dy
\f0\b ), 
\f1\b0 direction
\f0\b )\
\
\cf2 class 
\f1\b0 \cf0 AgentState
\f0\b :\
  
\f1\b0 \cf4 """\
  AgentStates hold the state of an agent (configuration, speed, scared, etc).\
  """\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 startConfiguration
\f0\b , 
\f1\b0 isPacman 
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 start 
\f0\b = 
\f1\b0 startConfiguration\
    \cf2 self
\f0\b \cf0 .
\f1\b0 configuration 
\f0\b = 
\f1\b0 startConfiguration\
    \cf2 self
\f0\b \cf0 .
\f1\b0 isPacman 
\f0\b = 
\f1\b0 isPacman\
    \cf2 self
\f0\b \cf0 .
\f1\b0 scaredTimer 
\f0\b = 
\f1\b0 \cf5 0\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __str__
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ):\
    \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 isPacman
\f0\b : \
      \cf2 return 
\f1\b0 \cf5 "Pacman: " 
\f0\b \cf0 + 
\f1\b0 str
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 configuration 
\f0\b )\
    \cf2 else\cf0 :\
      \cf2 return 
\f1\b0 \cf5 "Ghost: " 
\f0\b \cf0 + 
\f1\b0 str
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 configuration 
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 __eq__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 other 
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 other 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      \cf2 return False\
    return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 configuration 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 configuration 
\f0\b \cf2 and 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 scaredTimer 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 scaredTimer\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __hash__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf0 int
\f0\b (
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 configuration
\f0\b ) + 
\f1\b0 \cf5 13
\f0\b \cf0 * 
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 scaredTimer
\f0\b ))\
  \
  \cf2 def 
\f1\b0 \cf0 copy
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ):\
    
\f1\b0 state 
\f0\b = 
\f1\b0 AgentState
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 start
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isPacman 
\f0\b )\
    
\f1\b0 state
\f0\b .
\f1\b0 configuration 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 configuration\
    state
\f0\b .
\f1\b0 scaredTimer 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 scaredTimer\
    
\f0\b \cf2 return 
\f1\b0 \cf0 state\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 configuration 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return 
\f1\b0 None\
    
\f0\b return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 configuration
\f0\b .
\f1\b0 getPosition
\f0\b ()\
\
  \cf2 def 
\f1\b0 \cf0 getDirection
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 configuration
\f0\b .
\f1\b0 getDirection
\f0\b ()\
  \
\cf2 class 
\f1\b0 \cf0 Grid
\f0\b :\
  
\f1\b0 \cf4 """\
  A 2-dimensional array of objects backed by a list of lists.  Data is accessed\
  via grid[x][y] where (x,y) are positions on a Pacman map with x horizontal,\
  y vertical and the origin (0,0) in the bottom left corner.  \
  \
  The __str__ method constructs an output that is oriented like a pacman board.\
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 width
\f0\b , 
\f1\b0 height
\f0\b , 
\f1\b0 initialValue
\f0\b =\cf2 False\cf0 , 
\f1\b0 bitRepresentation
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    \cf2 if 
\f1\b0 \cf0 initialValue 
\f0\b \cf2 not in \cf0 [\cf2 False\cf0 , \cf2 True\cf0 ]: \cf2 raise 
\f1\b0 \cf0 Exception
\f0\b (
\f1\b0 \cf5 'Grids can only contain booleans'
\f0\b \cf0 )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT 
\f0\b = 
\f1\b0 \cf5 30\
\
    \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b = 
\f1\b0 width\
    \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b = 
\f1\b0 height\
    \cf2 self
\f0\b \cf0 .
\f1\b0 data 
\f0\b = [[
\f1\b0 initialValue 
\f0\b \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 height
\f0\b )] \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 width
\f0\b )]\
    \cf2 if 
\f1\b0 \cf0 bitRepresentation
\f0\b :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _unpackBits
\f0\b (
\f1\b0 bitRepresentation
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 __getitem__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 i
\f0\b ):\
    \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 data
\f0\b [
\f1\b0 i
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 __setitem__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 key
\f0\b , 
\f1\b0 item
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 data
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 item\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __str__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 out 
\f0\b = [[
\f1\b0 str
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 data
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ])[
\f1\b0 \cf5 0
\f0\b \cf0 ] \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b )] \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b )]\
    
\f1\b0 out
\f0\b .
\f1\b0 reverse
\f0\b ()\
    \cf2 return 
\f1\b0 \cf5 '\\n'
\f0\b \cf0 .
\f1\b0 join
\f0\b ([
\f1\b0 \cf5 ''
\f0\b \cf0 .
\f1\b0 join
\f0\b (
\f1\b0 x
\f0\b ) \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 out
\f0\b ])\
  \
  \cf2 def 
\f1\b0 \cf0 __eq__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 other
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 other 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return False\
    return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 data 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 data\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __hash__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf0 hash
\f0\b (
\f1\b0 str
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ))\
    
\f1\b0 base 
\f0\b = 
\f1\b0 \cf5 1\
    \cf0 h 
\f0\b = 
\f1\b0 \cf5 0\
    
\f0\b \cf2 for 
\f1\b0 \cf0 l 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 data
\f0\b :\
      \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 l
\f0\b :\
        \cf2 if 
\f1\b0 \cf0 i
\f0\b :\
          
\f1\b0 h 
\f0\b += 
\f1\b0 base\
        base 
\f0\b *= 
\f1\b0 \cf5 2\
    
\f0\b \cf2 return 
\f1\b0 \cf0 hash
\f0\b (
\f1\b0 h
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 copy
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 g 
\f0\b = 
\f1\b0 Grid
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b )\
    
\f1\b0 g
\f0\b .
\f1\b0 data 
\f0\b = [
\f1\b0 x
\f0\b [:] \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 data
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 g\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 deepCopy
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 copy
\f0\b ()\
  \
  \cf2 def 
\f1\b0 \cf0 shallowCopy
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 g 
\f0\b = 
\f1\b0 Grid
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b )\
    
\f1\b0 g
\f0\b .
\f1\b0 data 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 data\
    
\f0\b \cf2 return 
\f1\b0 \cf0 g\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 count
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 item 
\f0\b =\cf2 True \cf0 ):\
    \cf2 return 
\f1\b0 \cf0 sum
\f0\b ([
\f1\b0 x
\f0\b .
\f1\b0 count
\f0\b (
\f1\b0 item
\f0\b ) \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 data
\f0\b ])\
    \
  \cf2 def 
\f1\b0 \cf0 asList
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 key 
\f0\b = \cf2 True\cf0 ):\
    
\f1\b0 list 
\f0\b = []\
    \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b ):\
      \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b ):\
        \cf2 if 
\f1\b0 self
\f0\b \cf0 [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] == 
\f1\b0 key
\f0\b : 
\f1\b0 list
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 x
\f0\b ,
\f1\b0 y
\f0\b ) )\
    \cf2 return 
\f1\b0 \cf0 list\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 packBits
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf4 """\
    Returns an efficient int list representation\
    \
    (width, height, bitPackedInts...)\
    """\
    \cf0 bits 
\f0\b = [
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b ]\
    
\f1\b0 currentInt 
\f0\b = 
\f1\b0 \cf5 0\
    
\f0\b \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b ):\
      
\f1\b0 bit 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT 
\f0\b - (
\f1\b0 i 
\f0\b % 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT
\f0\b ) - 
\f1\b0 \cf5 1\
      \cf0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _cellIndexToPosition
\f0\b (
\f1\b0 i
\f0\b )\
      \cf2 if 
\f1\b0 self
\f0\b \cf0 [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ]:\
        
\f1\b0 currentInt 
\f0\b += 
\f1\b0 \cf5 2 
\f0\b \cf0 ** 
\f1\b0 bit\
      
\f0\b \cf2 if \cf0 (
\f1\b0 i 
\f0\b + 
\f1\b0 \cf5 1
\f0\b \cf0 ) % 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT 
\f0\b == 
\f1\b0 \cf5 0
\f0\b \cf0 :\
        
\f1\b0 bits
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 currentInt
\f0\b )\
        
\f1\b0 currentInt 
\f0\b = 
\f1\b0 \cf5 0\
    \cf0 bits
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 currentInt
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 tuple
\f0\b (
\f1\b0 bits
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 _cellIndexToPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 index
\f0\b ):\
    
\f1\b0 x 
\f0\b = 
\f1\b0 index 
\f0\b / 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height\
    y 
\f0\b = 
\f1\b0 index 
\f0\b % 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height\
    
\f0\b \cf2 return 
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 _unpackBits
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 bits
\f0\b ):\
    
\f1\b0 \cf4 """\
    Fills in data from a bit-level representation\
    """\
    \cf0 cell 
\f0\b = 
\f1\b0 \cf5 0\
    
\f0\b \cf2 for 
\f1\b0 \cf0 packed 
\f0\b \cf2 in 
\f1\b0 \cf0 bits
\f0\b :\
      \cf2 for 
\f1\b0 \cf0 bit 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 _unpackInt
\f0\b (
\f1\b0 packed
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT
\f0\b ):\
        \cf2 if 
\f1\b0 \cf0 cell 
\f0\b == 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b : \cf2 break\
        
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _cellIndexToPosition
\f0\b (
\f1\b0 cell
\f0\b )\
        
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = 
\f1\b0 bit\
        cell 
\f0\b += 
\f1\b0 \cf5 1\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 _unpackInt
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 packed
\f0\b , 
\f1\b0 size
\f0\b ):\
    
\f1\b0 bools 
\f0\b = []\
    \cf2 if 
\f1\b0 \cf0 packed 
\f0\b < 
\f1\b0 \cf5 0
\f0\b \cf0 : \cf2 raise 
\f1\b0 \cf0 ValueError
\f0\b , 
\f1\b0 \cf5 "must be a positive integer"\
    
\f0\b \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 size
\f0\b ):\
      
\f1\b0 n 
\f0\b = 
\f1\b0 \cf5 2 
\f0\b \cf0 ** (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 CELLS_PER_INT 
\f0\b - 
\f1\b0 i 
\f0\b - 
\f1\b0 \cf5 1
\f0\b \cf0 )\
      \cf2 if 
\f1\b0 \cf0 packed 
\f0\b >= 
\f1\b0 n
\f0\b :\
        
\f1\b0 bools
\f0\b .
\f1\b0 append
\f0\b (\cf2 True\cf0 )\
        
\f1\b0 packed 
\f0\b -= 
\f1\b0 n\
      
\f0\b \cf2 else\cf0 :\
        
\f1\b0 bools
\f0\b .
\f1\b0 append
\f0\b (\cf2 False\cf0 )\
    \cf2 return 
\f1\b0 \cf0 bools    \
\

\f0\b \cf2 def 
\f1\b0 \cf0 reconstituteGrid
\f0\b (
\f1\b0 bitRep
\f0\b ):\
  \cf2 if 
\f1\b0 \cf0 type
\f0\b (
\f1\b0 bitRep
\f0\b ) \cf2 is not 
\f1\b0 \cf0 type
\f0\b ((
\f1\b0 \cf5 1
\f0\b \cf0 ,
\f1\b0 \cf5 2
\f0\b \cf0 )):\
    \cf2 return 
\f1\b0 \cf0 bitRep\
  width
\f0\b , 
\f1\b0 height 
\f0\b = 
\f1\b0 bitRep
\f0\b [:
\f1\b0 \cf5 2
\f0\b \cf0 ]\
  \cf2 return 
\f1\b0 \cf0 Grid
\f0\b (
\f1\b0 width
\f0\b , 
\f1\b0 height
\f0\b , 
\f1\b0 bitRepresentation
\f0\b = 
\f1\b0 bitRep
\f0\b [
\f1\b0 \cf5 2
\f0\b \cf0 :])\
\
\pard\pardeftab720\partightenfactor0

\f2\i\b0 \cf3 ####################################\
# Parts you shouldn't have to read #\
####################################\
  \
\pard\pardeftab720\partightenfactor0

\f0\i0\b \cf2 class 
\f1\b0 \cf0 Actions
\f0\b :\
  
\f1\b0 \cf4 """\
  A collection of static methods for manipulating move actions.\
  """\
  
\f2\i \cf3 # Directions\
  
\f1\i0 \cf0 _directions 
\f0\b = \{
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b : (
\f1\b0 \cf5 0
\f0\b \cf0 , 
\f1\b0 \cf5 1
\f0\b \cf0 ), \
                 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b : (
\f1\b0 \cf5 0
\f0\b \cf0 , -
\f1\b0 \cf5 1
\f0\b \cf0 ), \
                 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST
\f0\b :  (
\f1\b0 \cf5 1
\f0\b \cf0 , 
\f1\b0 \cf5 0
\f0\b \cf0 ), \
                 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b :  (-
\f1\b0 \cf5 1
\f0\b \cf0 , 
\f1\b0 \cf5 0
\f0\b \cf0 ), \
                 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP
\f0\b :  (
\f1\b0 \cf5 0
\f0\b \cf0 , 
\f1\b0 \cf5 0
\f0\b \cf0 )\}\
\
  
\f1\b0 _directionsAsList 
\f0\b = 
\f1\b0 _directions
\f0\b .
\f1\b0 items
\f0\b ()\
\
  
\f1\b0 TOLERANCE 
\f0\b = .
\f1\b0 \cf5 001\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 reverseDirection
\f0\b (
\f1\b0 action
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 action 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 SOUTH\
    
\f0\b \cf2 if 
\f1\b0 \cf0 action 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 NORTH\
    
\f0\b \cf2 if 
\f1\b0 \cf0 action 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST
\f0\b :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 WEST\
    
\f0\b \cf2 if 
\f1\b0 \cf0 action 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 EAST\
    
\f0\b \cf2 return 
\f1\b0 \cf0 action\
  reverseDirection 
\f0\b = 
\f1\b0 staticmethod
\f0\b (
\f1\b0 reverseDirection
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 vectorToDirection
\f0\b (
\f1\b0 vector
\f0\b ):\
    
\f1\b0 dx
\f0\b , 
\f1\b0 dy 
\f0\b = 
\f1\b0 vector\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dy 
\f0\b > 
\f1\b0 \cf5 0
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 NORTH\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dy 
\f0\b < 
\f1\b0 \cf5 0
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 SOUTH\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dx 
\f0\b < 
\f1\b0 \cf5 0
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 WEST\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dx 
\f0\b > 
\f1\b0 \cf5 0
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 EAST\
    
\f0\b \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 STOP\
  vectorToDirection 
\f0\b = 
\f1\b0 staticmethod
\f0\b (
\f1\b0 vectorToDirection
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 directionToVector
\f0\b (
\f1\b0 direction
\f0\b , 
\f1\b0 speed 
\f0\b = 
\f1\b0 \cf5 1.0
\f0\b \cf0 ):\
    
\f1\b0 dx
\f0\b , 
\f1\b0 dy 
\f0\b =  
\f1\b0 Actions
\f0\b .
\f1\b0 _directions
\f0\b [
\f1\b0 direction
\f0\b ]\
    \cf2 return \cf0 (
\f1\b0 dx 
\f0\b * 
\f1\b0 speed
\f0\b , 
\f1\b0 dy 
\f0\b * 
\f1\b0 speed
\f0\b )\
  
\f1\b0 directionToVector 
\f0\b = 
\f1\b0 staticmethod
\f0\b (
\f1\b0 directionToVector
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 getPossibleActions
\f0\b (
\f1\b0 config
\f0\b , 
\f1\b0 walls
\f0\b ):\
    
\f1\b0 possible 
\f0\b = []\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 config
\f0\b .
\f1\b0 getPosition
\f0\b ()\
    
\f1\b0 x_int
\f0\b , 
\f1\b0 y_int 
\f0\b = 
\f1\b0 int
\f0\b (
\f1\b0 x 
\f0\b + 
\f1\b0 \cf5 0.5
\f0\b \cf0 ), 
\f1\b0 int
\f0\b (
\f1\b0 y 
\f0\b + 
\f1\b0 \cf5 0.5
\f0\b \cf0 )\
    \
    
\f2\i\b0 \cf3 # In between grid points, all agents must continue straight\
    
\f0\i0\b \cf2 if \cf0 (
\f1\b0 abs
\f0\b (
\f1\b0 x 
\f0\b - 
\f1\b0 x_int
\f0\b ) + 
\f1\b0 abs
\f0\b (
\f1\b0 y 
\f0\b - 
\f1\b0 y_int
\f0\b )  > 
\f1\b0 Actions
\f0\b .
\f1\b0 TOLERANCE
\f0\b ):\
      \cf2 return \cf0 [
\f1\b0 config
\f0\b .
\f1\b0 getDirection
\f0\b ()]\
    \
    \cf2 for 
\f1\b0 \cf0 dir
\f0\b , 
\f1\b0 vec 
\f0\b \cf2 in 
\f1\b0 \cf0 Actions
\f0\b .
\f1\b0 _directionsAsList
\f0\b :\
      
\f1\b0 dx
\f0\b , 
\f1\b0 dy 
\f0\b = 
\f1\b0 vec\
      next_y 
\f0\b = 
\f1\b0 y_int 
\f0\b + 
\f1\b0 dy\
      next_x 
\f0\b = 
\f1\b0 x_int 
\f0\b + 
\f1\b0 dx\
      
\f0\b \cf2 if not 
\f1\b0 \cf0 walls
\f0\b [
\f1\b0 next_x
\f0\b ][
\f1\b0 next_y
\f0\b ]: 
\f1\b0 possible
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 dir
\f0\b )\
\
    \cf2 return 
\f1\b0 \cf0 possible\
\
  getPossibleActions 
\f0\b = 
\f1\b0 staticmethod
\f0\b (
\f1\b0 getPossibleActions
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 getLegalNeighbors
\f0\b (
\f1\b0 position
\f0\b , 
\f1\b0 walls
\f0\b ):\
    
\f1\b0 x
\f0\b ,
\f1\b0 y 
\f0\b = 
\f1\b0 position\
    x_int
\f0\b , 
\f1\b0 y_int 
\f0\b = 
\f1\b0 int
\f0\b (
\f1\b0 x 
\f0\b + 
\f1\b0 \cf5 0.5
\f0\b \cf0 ), 
\f1\b0 int
\f0\b (
\f1\b0 y 
\f0\b + 
\f1\b0 \cf5 0.5
\f0\b \cf0 )\
    
\f1\b0 neighbors 
\f0\b = []\
    \cf2 for 
\f1\b0 \cf0 dir
\f0\b , 
\f1\b0 vec 
\f0\b \cf2 in 
\f1\b0 \cf0 Actions
\f0\b .
\f1\b0 _directionsAsList
\f0\b :\
      
\f1\b0 dx
\f0\b , 
\f1\b0 dy 
\f0\b = 
\f1\b0 vec\
      next_x 
\f0\b = 
\f1\b0 x_int 
\f0\b + 
\f1\b0 dx\
      
\f0\b \cf2 if 
\f1\b0 \cf0 next_x 
\f0\b < 
\f1\b0 \cf5 0 
\f0\b \cf2 or 
\f1\b0 \cf0 next_x 
\f0\b == 
\f1\b0 walls
\f0\b .
\f1\b0 width
\f0\b : \cf2 continue\
      
\f1\b0 \cf0 next_y 
\f0\b = 
\f1\b0 y_int 
\f0\b + 
\f1\b0 dy\
      
\f0\b \cf2 if 
\f1\b0 \cf0 next_y 
\f0\b < 
\f1\b0 \cf5 0 
\f0\b \cf2 or 
\f1\b0 \cf0 next_y 
\f0\b == 
\f1\b0 walls
\f0\b .
\f1\b0 height
\f0\b : \cf2 continue\
      if not 
\f1\b0 \cf0 walls
\f0\b [
\f1\b0 next_x
\f0\b ][
\f1\b0 next_y
\f0\b ]: 
\f1\b0 neighbors
\f0\b .
\f1\b0 append
\f0\b ((
\f1\b0 next_x
\f0\b , 
\f1\b0 next_y
\f0\b ))\
    \cf2 return 
\f1\b0 \cf0 neighbors\
  getLegalNeighbors 
\f0\b = 
\f1\b0 staticmethod
\f0\b (
\f1\b0 getLegalNeighbors
\f0\b )\
  \
\cf2 class 
\f1\b0 \cf0 GameStateData
\f0\b :\
  
\f1\b0 \cf4 """\
  \
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 prevState 
\f0\b = 
\f1\b0 \cf2 None 
\f0\b \cf0 ):\
    
\f1\b0 \cf4 """ \
    Generates a new data packet by copying information from its predecessor.\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 prevState 
\f0\b != 
\f1\b0 \cf2 None
\f0\b \cf0 : \
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food 
\f0\b = 
\f1\b0 prevState
\f0\b .
\f1\b0 food
\f0\b .
\f1\b0 shallowCopy
\f0\b ()\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules 
\f0\b = 
\f1\b0 prevState
\f0\b .
\f1\b0 capsules
\f0\b [:]\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentStates 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 copyAgentStates
\f0\b ( 
\f1\b0 prevState
\f0\b .
\f1\b0 agentStates 
\f0\b )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout 
\f0\b = 
\f1\b0 prevState
\f0\b .
\f1\b0 layout\
      \cf2 self
\f0\b \cf0 .
\f1\b0 _eaten 
\f0\b = 
\f1\b0 prevState
\f0\b .
\f1\b0 _eaten\
      \cf2 self
\f0\b \cf0 .
\f1\b0 score 
\f0\b = 
\f1\b0 prevState
\f0\b .
\f1\b0 score\
    \cf2 self
\f0\b \cf0 .
\f1\b0 _foodEaten 
\f0\b = 
\f1\b0 \cf2 None\
    self
\f0\b \cf0 .
\f1\b0 _capsuleEaten 
\f0\b = 
\f1\b0 \cf2 None\
    self
\f0\b \cf0 .
\f1\b0 _agentMoved 
\f0\b = 
\f1\b0 \cf2 None\
    self
\f0\b \cf0 .
\f1\b0 _lose 
\f0\b = \cf2 False\
    
\f1\b0 self
\f0\b \cf0 .
\f1\b0 _win 
\f0\b = \cf2 False\
    
\f1\b0 self
\f0\b \cf0 .
\f1\b0 scoreChange 
\f0\b = 
\f1\b0 \cf5 0\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 deepCopy
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ):\
    
\f1\b0 state 
\f0\b = 
\f1\b0 GameStateData
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 )\
    
\f1\b0 state
\f0\b .
\f1\b0 food 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b .
\f1\b0 deepCopy
\f0\b ()\
    
\f1\b0 state
\f0\b .
\f1\b0 layout 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout
\f0\b .
\f1\b0 deepCopy
\f0\b ()\
    
\f1\b0 state
\f0\b .
\f1\b0 _agentMoved 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _agentMoved\
    state
\f0\b .
\f1\b0 _foodEaten 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _foodEaten\
    state
\f0\b .
\f1\b0 _capsuleEaten 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _capsuleEaten\
    
\f0\b \cf2 return 
\f1\b0 \cf0 state\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 copyAgentStates
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 agentStates 
\f0\b ):\
    
\f1\b0 copiedStates 
\f0\b = []\
    \cf2 for 
\f1\b0 \cf0 agentState 
\f0\b \cf2 in 
\f1\b0 \cf0 agentStates
\f0\b :\
      
\f1\b0 copiedStates
\f0\b .
\f1\b0 append
\f0\b ( 
\f1\b0 agentState
\f0\b .
\f1\b0 copy
\f0\b () )\
    \cf2 return 
\f1\b0 \cf0 copiedStates\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __eq__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 other 
\f0\b ):\
    
\f1\b0 \cf4 """\
    Allows two states to be compared.\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 other 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return False\
    
\f2\i\b0 \cf3 # TODO Check for type of other\
    
\f0\i0\b \cf2 if not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentStates 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 agentStates
\f0\b : \cf2 return False\
    if not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 food 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 food
\f0\b : \cf2 return False\
    if not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capsules 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 capsules
\f0\b : \cf2 return False\
    if not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 score 
\f0\b == 
\f1\b0 other
\f0\b .
\f1\b0 score
\f0\b : \cf2 return False\
    return True\
                                                      \
  def 
\f1\b0 \cf0 __hash__
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ):\
    
\f1\b0 \cf4 """\
    Allows states to be keys of dictionaries.\
    """\
    
\f0\b \cf2 for 
\f1\b0 \cf0 i
\f0\b , 
\f1\b0 state 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentStates 
\f0\b ):\
      \cf2 try\cf0 :\
        
\f1\b0 int
\f0\b (
\f1\b0 hash
\f0\b (
\f1\b0 state
\f0\b ))\
      \cf2 except 
\f1\b0 \cf0 TypeError
\f0\b , 
\f1\b0 e
\f0\b :\
        \cf2 print 
\f1\b0 \cf0 e\
        
\f2\i \cf3 #hash(state)\
    
\f0\i0\b \cf2 return 
\f1\b0 \cf0 int
\f0\b ((
\f1\b0 hash
\f0\b (
\f1\b0 tuple
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentStates
\f0\b )) + 
\f1\b0 \cf5 13
\f0\b \cf0 *
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b ) + 
\f1\b0 \cf5 113
\f0\b \cf0 * 
\f1\b0 hash
\f0\b (
\f1\b0 tuple
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules
\f0\b )) + 
\f1\b0 \cf5 7 
\f0\b \cf0 * 
\f1\b0 hash
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 score
\f0\b )) % 
\f1\b0 \cf5 1048575 
\f0\b \cf0 )\
\
  \cf2 def 
\f1\b0 \cf0 __str__
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ): \
    
\f1\b0 width
\f0\b , 
\f1\b0 height 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout
\f0\b .
\f1\b0 width
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout
\f0\b .
\f1\b0 height\
    map 
\f0\b = 
\f1\b0 Grid
\f0\b (
\f1\b0 width
\f0\b , 
\f1\b0 height
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 type
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b ) == 
\f1\b0 type
\f0\b ((
\f1\b0 \cf5 1
\f0\b \cf0 ,
\f1\b0 \cf5 2
\f0\b \cf0 )):\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food 
\f0\b = 
\f1\b0 reconstituteGrid
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b )\
    \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 width
\f0\b ):\
      \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 height
\f0\b ):\
        
\f1\b0 food
\f0\b , 
\f1\b0 walls 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout
\f0\b .
\f1\b0 walls\
        map
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _foodWallStr
\f0\b (
\f1\b0 food
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ], 
\f1\b0 walls
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ])\
    \
    \cf2 for 
\f1\b0 \cf0 agentState 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentStates
\f0\b :\
      \cf2 if 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 configuration 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 continue\
      
\f1\b0 \cf0 x
\f0\b ,
\f1\b0 y 
\f0\b = [
\f1\b0 int
\f0\b ( 
\f1\b0 i 
\f0\b ) \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 nearestPoint
\f0\b ( 
\f1\b0 agentState
\f0\b .
\f1\b0 configuration
\f0\b .
\f1\b0 pos 
\f0\b )]\
      
\f1\b0 agent_dir 
\f0\b = 
\f1\b0 agentState
\f0\b .
\f1\b0 configuration
\f0\b .
\f1\b0 direction\
      
\f0\b \cf2 if 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 isPacman
\f0\b :\
        
\f1\b0 map
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _pacStr
\f0\b ( 
\f1\b0 agent_dir 
\f0\b )\
      \cf2 else\cf0 :\
        
\f1\b0 map
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _ghostStr
\f0\b ( 
\f1\b0 agent_dir 
\f0\b )\
\
    \cf2 for 
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capsules
\f0\b :\
      
\f1\b0 map
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = 
\f1\b0 \cf5 'o'\
    \
    
\f0\b \cf2 return 
\f1\b0 \cf0 str
\f0\b (
\f1\b0 map
\f0\b ) + (
\f1\b0 \cf5 "\\nScore: %d\\n" 
\f0\b \cf0 % 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 score
\f0\b ) \
      \
  \cf2 def 
\f1\b0 \cf0 _foodWallStr
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 hasFood
\f0\b , 
\f1\b0 hasWall 
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 hasFood
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 '.'\
    
\f0\b \cf2 elif 
\f1\b0 \cf0 hasWall
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 '%'\
    
\f0\b \cf2 else\cf0 :\
      \cf2 return 
\f1\b0 \cf5 ' '\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 _pacStr
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 dir 
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 'v'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 '^'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 '>'\
    
\f0\b \cf2 return 
\f1\b0 \cf5 '<'\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 _ghostStr
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 dir 
\f0\b ):\
    \cf2 return 
\f1\b0 \cf5 'G'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 'M'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 'W'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b :\
      \cf2 return 
\f1\b0 \cf5 '3'\
    
\f0\b \cf2 return 
\f1\b0 \cf5 'E'\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 initialize
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 layout
\f0\b , 
\f1\b0 numGhostAgents 
\f0\b ):\
    
\f1\b0 \cf4 """\
    Creates an initial game state from a layout array (see layout.py).\
    """\
    \cf2 self
\f0\b \cf0 .
\f1\b0 food 
\f0\b = 
\f1\b0 layout
\f0\b .
\f1\b0 food
\f0\b .
\f1\b0 copy
\f0\b ()\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules 
\f0\b = 
\f1\b0 layout
\f0\b .
\f1\b0 capsules
\f0\b [:]\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout 
\f0\b = 
\f1\b0 layout\
    \cf2 self
\f0\b \cf0 .
\f1\b0 score 
\f0\b = 
\f1\b0 \cf5 0\
    \cf2 self
\f0\b \cf0 .
\f1\b0 scoreChange 
\f0\b = 
\f1\b0 \cf5 0\
        \
    \cf2 self
\f0\b \cf0 .
\f1\b0 agentStates 
\f0\b = []\
    
\f1\b0 numGhosts 
\f0\b = 
\f1\b0 \cf5 0\
    
\f0\b \cf2 for 
\f1\b0 \cf0 isPacman
\f0\b , 
\f1\b0 pos 
\f0\b \cf2 in 
\f1\b0 \cf0 layout
\f0\b .
\f1\b0 agentPositions
\f0\b :\
      \cf2 if not 
\f1\b0 \cf0 isPacman
\f0\b : \
        \cf2 if 
\f1\b0 \cf0 numGhosts 
\f0\b == 
\f1\b0 numGhostAgents
\f0\b : \cf2 continue 
\f2\i\b0 \cf3 # Max ghosts reached already\
        
\f0\i0\b \cf2 else\cf0 : 
\f1\b0 numGhosts 
\f0\b += 
\f1\b0 \cf5 1\
      \cf2 self
\f0\b \cf0 .
\f1\b0 agentStates
\f0\b .
\f1\b0 append
\f0\b ( 
\f1\b0 AgentState
\f0\b ( 
\f1\b0 Configuration
\f0\b ( 
\f1\b0 pos
\f0\b , 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP
\f0\b ), 
\f1\b0 isPacman
\f0\b ) )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 _eaten 
\f0\b = [\cf2 False for 
\f1\b0 \cf0 a 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentStates
\f0\b ]\
\
\cf2 class 
\f1\b0 \cf0 Game
\f0\b :\
  
\f1\b0 \cf4 """\
  The Game manages the control flow, soliciting actions from agents.\
  """\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 agents
\f0\b , 
\f1\b0 display
\f0\b , 
\f1\b0 rules 
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agents 
\f0\b = 
\f1\b0 agents\
    \cf2 self
\f0\b \cf0 .
\f1\b0 display 
\f0\b = 
\f1\b0 display\
    \cf2 self
\f0\b \cf0 .
\f1\b0 rules 
\f0\b = 
\f1\b0 rules\
    \cf2 self
\f0\b \cf0 .
\f1\b0 gameOver 
\f0\b = \cf2 False\
    
\f1\b0 self
\f0\b \cf0 .
\f1\b0 moveHistory 
\f0\b = []\
    \
  \cf2 def 
\f1\b0 \cf0 run
\f0\b ( 
\f1\b0 \cf2 self 
\f0\b \cf0 ):\
    
\f1\b0 \cf4 """\
    Main control loop for game play.\
    """\
    \cf2 self
\f0\b \cf0 .
\f1\b0 display
\f0\b .
\f1\b0 initialize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 data
\f0\b )\
    
\f2\i\b0 \cf3 ###self.display.initialize(self.state.makeObservation(1).data)\
    # inform learning agents of the game start\
    
\f0\i0\b \cf2 for 
\f1\b0 \cf0 agent 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agents
\f0\b :\
      
\f2\i\b0 \cf3 # if ("initial" in dir(agent)): agent.initial()\
      
\f0\i0\b \cf2 if \cf0 (
\f1\b0 \cf5 "registerInitialState" 
\f0\b \cf2 in 
\f1\b0 \cf0 dir
\f0\b (
\f1\b0 agent
\f0\b )):\
        
\f1\b0 agent
\f0\b .
\f1\b0 registerInitialState
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 deepCopy
\f0\b ())\
      \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 numMoves 
\f0\b = 
\f1\b0 \cf5 0\
    \cf0 agentIndex 
\f0\b = 
\f1\b0 \cf5 0    \
    \cf0 numAgents 
\f0\b = 
\f1\b0 len
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agents 
\f0\b )\
    \cf2 while not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 gameOver
\f0\b :\
      
\f2\i\b0 \cf3 # Fetch the next agent\
      
\f1\i0 \cf0 agent 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agents
\f0\b [
\f1\b0 agentIndex
\f0\b ]\
      
\f2\i\b0 \cf3 # Generate an observation of the state\
      
\f0\i0\b \cf2 if 
\f1\b0 \cf5 'observationFunction' 
\f0\b \cf2 in 
\f1\b0 \cf0 dir
\f0\b ( 
\f1\b0 agent 
\f0\b ):\
        
\f1\b0 observation 
\f0\b = 
\f1\b0 agent
\f0\b .
\f1\b0 observationFunction
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 deepCopy
\f0\b ())\
      \cf2 else\cf0 :\
        
\f1\b0 observation 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 deepCopy
\f0\b ()\
        \
      
\f2\i\b0 \cf3 # Solicit an action\
      
\f1\i0 \cf0 startTime 
\f0\b = 
\f1\b0 time
\f0\b .
\f1\b0 time
\f0\b ()\
      
\f1\b0 action 
\f0\b = 
\f1\b0 agent
\f0\b .
\f1\b0 getAction
\f0\b ( 
\f1\b0 observation 
\f0\b )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 moveHistory
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 agentIndex
\f0\b , 
\f1\b0 action
\f0\b ) )\
      \cf2 if 
\f1\b0 \cf5 'checkTime' 
\f0\b \cf2 in 
\f1\b0 \cf0 dir
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 rules
\f0\b ):\
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 rules
\f0\b .
\f1\b0 checkTime
\f0\b (
\f1\b0 time
\f0\b .
\f1\b0 time
\f0\b () - 
\f1\b0 startTime
\f0\b )\
      \
      
\f2\i\b0 \cf3 # Execute the action\
      
\f1\i0 \cf2 self
\f0\b \cf0 .
\f1\b0 state 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 generateSuccessor
\f0\b ( 
\f1\b0 agentIndex
\f0\b , 
\f1\b0 action 
\f0\b )\
      \
      
\f2\i\b0 \cf3 # Change the display\
      
\f1\i0 \cf2 self
\f0\b \cf0 .
\f1\b0 display
\f0\b .
\f1\b0 update
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b .
\f1\b0 data 
\f0\b )\
      
\f2\i\b0 \cf3 ###idx = agentIndex - agentIndex % 2 + 1\
      ###self.display.update( self.state.makeObservation(idx).data )\
      \
      # Allow for game specific conditions (winning, losing, etc.)\
      
\f1\i0 \cf2 self
\f0\b \cf0 .
\f1\b0 rules
\f0\b .
\f1\b0 process
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 )\
      
\f2\i\b0 \cf3 # Track progress\
      
\f0\i0\b \cf2 if 
\f1\b0 \cf0 agentIndex 
\f0\b == 
\f1\b0 numAgents 
\f0\b + 
\f1\b0 \cf5 1
\f0\b \cf0 : 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 numMoves 
\f0\b += 
\f1\b0 \cf5 1\
      
\f2\i \cf3 # Next agent\
      
\f1\i0 \cf0 agentIndex 
\f0\b = ( 
\f1\b0 agentIndex 
\f0\b + 
\f1\b0 \cf5 1 
\f0\b \cf0 ) % 
\f1\b0 numAgents\
    \
    
\f2\i \cf3 # inform a learning agent of the game result\
    
\f0\i0\b \cf2 for 
\f1\b0 \cf0 agent 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agents
\f0\b :\
      \cf2 if 
\f1\b0 \cf5 "final" 
\f0\b \cf2 in 
\f1\b0 \cf0 dir
\f0\b ( 
\f1\b0 agent 
\f0\b ) :\
        
\f1\b0 agent
\f0\b .
\f1\b0 final
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 state 
\f0\b )\
    \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 display
\f0\b .
\f1\b0 finish
\f0\b ()}