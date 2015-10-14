{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red118\green0\blue2;\red251\green0\blue7;
\red15\green112\blue1;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
from 
\f1\b0 \cf0 util 
\f0\b \cf2 import 
\f1\b0 \cf0 manhattanDistance\

\f0\b \cf2 from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Grid\

\f0\b \cf2 import 
\f1\b0 \cf0 os\

\f0\b \cf2 import 
\f1\b0 \cf0 random\
\
VISIBILITY_MATRIX_CACHE 
\f0\b = \{\}\
\
\cf2 class 
\f1\b0 \cf0 Layout
\f0\b :\
  
\f1\b0 \cf3 """\
  A Layout manages the static information about the game board.\
  """\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 layoutText
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b = 
\f1\b0 len
\f0\b (
\f1\b0 layoutText
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ])\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b = 
\f1\b0 len
\f0\b (
\f1\b0 layoutText
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 walls 
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
\f0\b , \cf2 False\cf0 )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food 
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
\f0\b , \cf2 False\cf0 )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules 
\f0\b = []\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions 
\f0\b = []\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 numGhosts 
\f0\b = 
\f1\b0 \cf4 0\
    \cf2 self
\f0\b \cf0 .
\f1\b0 processLayoutText
\f0\b (
\f1\b0 layoutText
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText 
\f0\b = 
\f1\b0 layoutText\
    
\f2\i \cf5 # self.initializeVisibilityMatrix()\
    \
  
\f0\i0\b \cf2 def 
\f1\b0 \cf0 getNumGhosts
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 numGhosts\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 initializeVisibilityMatrix
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 global 
\f1\b0 \cf0 VISIBILITY_MATRIX_CACHE\
    
\f0\b \cf2 if 
\f1\b0 \cf0 reduce
\f0\b (
\f1\b0 str
\f0\b .
\f1\b0 __add__
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText
\f0\b ) \cf2 not in 
\f1\b0 \cf0 VISIBILITY_MATRIX_CACHE
\f0\b :\
      \cf2 from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Directions\
      vecs 
\f0\b = [(-
\f1\b0 \cf4 0.5
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 ), (
\f1\b0 \cf4 0.5
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 ),(
\f1\b0 \cf4 0
\f0\b \cf0 ,-
\f1\b0 \cf4 0.5
\f0\b \cf0 ),(
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0.5
\f0\b \cf0 )]\
      
\f1\b0 dirs 
\f0\b = [
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b , 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b , 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b , 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST
\f0\b ]\
      
\f1\b0 vis 
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
\f0\b , \{
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH
\f0\b :
\f1\b0 set
\f0\b (), 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH
\f0\b :
\f1\b0 set
\f0\b (), 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST
\f0\b :
\f1\b0 set
\f0\b (), 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST
\f0\b :
\f1\b0 set
\f0\b (), 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP
\f0\b :
\f1\b0 set
\f0\b ()\})\
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
\f0\b \cf0 .
\f1\b0 walls
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] == \cf2 False\cf0 :\
            \cf2 for 
\f1\b0 \cf0 vec
\f0\b , 
\f1\b0 direction 
\f0\b \cf2 in 
\f1\b0 \cf0 zip
\f0\b (
\f1\b0 vecs
\f0\b , 
\f1\b0 dirs
\f0\b ):\
              
\f1\b0 dx
\f0\b , 
\f1\b0 dy 
\f0\b = 
\f1\b0 vec\
              nextx
\f0\b , 
\f1\b0 nexty 
\f0\b = 
\f1\b0 x 
\f0\b + 
\f1\b0 dx
\f0\b , 
\f1\b0 y 
\f0\b + 
\f1\b0 dy\
              
\f0\b \cf2 while \cf0 (
\f1\b0 nextx 
\f0\b + 
\f1\b0 nexty
\f0\b ) != 
\f1\b0 int
\f0\b (
\f1\b0 nextx
\f0\b ) + 
\f1\b0 int
\f0\b (
\f1\b0 nexty
\f0\b ) \cf2 or not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 walls
\f0\b [
\f1\b0 int
\f0\b (
\f1\b0 nextx
\f0\b )][
\f1\b0 int
\f0\b (
\f1\b0 nexty
\f0\b )] :\
                
\f1\b0 vis
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ][
\f1\b0 direction
\f0\b ].
\f1\b0 add
\f0\b ((
\f1\b0 nextx
\f0\b , 
\f1\b0 nexty
\f0\b ))\
                
\f1\b0 nextx
\f0\b , 
\f1\b0 nexty 
\f0\b = 
\f1\b0 x 
\f0\b + 
\f1\b0 dx
\f0\b , 
\f1\b0 y 
\f0\b + 
\f1\b0 dy\
      \cf2 self
\f0\b \cf0 .
\f1\b0 visibility 
\f0\b = 
\f1\b0 vis      \
      VISIBILITY_MATRIX_CACHE
\f0\b [
\f1\b0 reduce
\f0\b (
\f1\b0 str
\f0\b .
\f1\b0 __add__
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText
\f0\b )] = 
\f1\b0 vis\
    
\f0\b \cf2 else\cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 visibility 
\f0\b = 
\f1\b0 VISIBILITY_MATRIX_CACHE
\f0\b [
\f1\b0 reduce
\f0\b (
\f1\b0 str
\f0\b .
\f1\b0 __add__
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText
\f0\b )]\
      \
  \cf2 def 
\f1\b0 \cf0 isWall
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pos
\f0\b ):\
    
\f1\b0 x
\f0\b , 
\f1\b0 col 
\f0\b = 
\f1\b0 pos\
    
\f0\b \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 walls
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 col
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 getRandomLegalPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 x 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b ))\
    
\f1\b0 y 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b ))\
    \cf2 while 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b ( (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ) ):\
      
\f1\b0 x 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b ))\
      
\f1\b0 y 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b ))\
    \cf2 return \cf0 (
\f1\b0 x
\f0\b ,
\f1\b0 y
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 getRandomCorner
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 poses 
\f0\b = [(
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 ), (
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 ), (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 , 
\f1\b0 \cf4 1
\f0\b \cf0 ), (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 )]\
    \cf2 return 
\f1\b0 \cf0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 poses
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 getFurthestCorner
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pacPos
\f0\b ):\
    
\f1\b0 poses 
\f0\b = [(
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 ), (
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 ), (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 , 
\f1\b0 \cf4 1
\f0\b \cf0 ), (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b - 
\f1\b0 \cf4 2
\f0\b \cf0 )]\
    
\f1\b0 dist
\f0\b , 
\f1\b0 pos 
\f0\b = 
\f1\b0 max
\f0\b ([(
\f1\b0 manhattanDistance
\f0\b (
\f1\b0 p
\f0\b , 
\f1\b0 pacPos
\f0\b ), 
\f1\b0 p
\f0\b ) \cf2 for 
\f1\b0 \cf0 p 
\f0\b \cf2 in 
\f1\b0 \cf0 poses
\f0\b ])\
    \cf2 return 
\f1\b0 \cf0 pos\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 isVisibleFrom
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghostPos
\f0\b , 
\f1\b0 pacPos
\f0\b , 
\f1\b0 pacDirection
\f0\b ):\
    
\f1\b0 row
\f0\b , 
\f1\b0 col 
\f0\b = [
\f1\b0 int
\f0\b (
\f1\b0 x
\f0\b ) \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 pacPos
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 ghostPos 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 visibility
\f0\b [
\f1\b0 row
\f0\b ][
\f1\b0 col
\f0\b ][
\f1\b0 pacDirection
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 __str__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf4 "\\n"
\f0\b \cf0 .
\f1\b0 join
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 deepCopy
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf0 Layout
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layoutText
\f0\b [:])\
    \
  \cf2 def 
\f1\b0 \cf0 processLayoutText
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 layoutText
\f0\b ):\
    
\f1\b0 \cf3 """\
    Coordinates are flipped from the input format to the (x,y) convention here\
    \
    The shape of the maze.  Each character  \
    represents a different type of object.   \
     % - Wall                               \
     . - Food\
     o - Capsule\
     G - Ghost\
     P - Pacman\
    Other characters are ignored.\
    """\
    \cf0 maxY 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b - 
\f1\b0 \cf4 1\
    
\f0\b \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b ):       \
      \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b ):\
        
\f1\b0 layoutChar 
\f0\b = 
\f1\b0 layoutText
\f0\b [
\f1\b0 maxY 
\f0\b - 
\f1\b0 y
\f0\b ][
\f1\b0 x
\f0\b ]  \
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 processLayoutChar
\f0\b (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b , 
\f1\b0 layoutChar
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions
\f0\b .
\f1\b0 sort
\f0\b ()\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions 
\f0\b = [ ( 
\f1\b0 i 
\f0\b == 
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 pos
\f0\b ) \cf2 for 
\f1\b0 \cf0 i
\f0\b , 
\f1\b0 pos 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentPositions
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 processLayoutChar
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b , 
\f1\b0 layoutChar
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 layoutChar 
\f0\b == 
\f1\b0 \cf4 '%'
\f0\b \cf0 :      \
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 walls
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = \cf2 True\
    elif 
\f1\b0 \cf0 layoutChar 
\f0\b == 
\f1\b0 \cf4 '.'
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ] = \cf2 True \
    elif 
\f1\b0 \cf0 layoutChar 
\f0\b == 
\f1\b0 \cf4 'o'
\f0\b \cf0 :    \
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules
\f0\b .
\f1\b0 append
\f0\b ((
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ))   \
    \cf2 elif 
\f1\b0 \cf0 layoutChar 
\f0\b == 
\f1\b0 \cf4 'P'
\f0\b \cf0 :    \
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 \cf4 0
\f0\b \cf0 , (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ) ) )\
    \cf2 elif 
\f1\b0 \cf0 layoutChar 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf4 'G'
\f0\b \cf0 ]:    \
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 \cf4 1
\f0\b \cf0 , (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ) ) )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 numGhosts 
\f0\b += 
\f1\b0 \cf4 1\
    
\f0\b \cf2 elif 
\f1\b0 \cf0 layoutChar 
\f0\b \cf2 in  \cf0 [
\f1\b0 \cf4 '1'
\f0\b \cf0 , 
\f1\b0 \cf4 '2'
\f0\b \cf0 , 
\f1\b0 \cf4 '3'
\f0\b \cf0 , 
\f1\b0 \cf4 '4'
\f0\b \cf0 ]:\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentPositions
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 int
\f0\b (
\f1\b0 layoutChar
\f0\b ), (
\f1\b0 x
\f0\b ,
\f1\b0 y
\f0\b )))\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 numGhosts 
\f0\b += 
\f1\b0 \cf4 1 \

\f0\b \cf2 def 
\f1\b0 \cf0 getLayout
\f0\b (
\f1\b0 name
\f0\b , 
\f1\b0 back 
\f0\b = 
\f1\b0 \cf4 2
\f0\b \cf0 ):\
  \cf2 if 
\f1\b0 \cf0 name
\f0\b .
\f1\b0 endswith
\f0\b (
\f1\b0 \cf4 '.lay'
\f0\b \cf0 ):\
    
\f1\b0 layout 
\f0\b = 
\f1\b0 tryToLoad
\f0\b (
\f1\b0 \cf4 'layouts/' 
\f0\b \cf0 + 
\f1\b0 name
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 layout 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : 
\f1\b0 layout 
\f0\b = 
\f1\b0 tryToLoad
\f0\b (
\f1\b0 name
\f0\b )\
  \cf2 else\cf0 :\
    
\f1\b0 layout 
\f0\b = 
\f1\b0 tryToLoad
\f0\b (
\f1\b0 \cf4 'layouts/' 
\f0\b \cf0 + 
\f1\b0 name 
\f0\b + 
\f1\b0 \cf4 '.lay'
\f0\b \cf0 )\
    \cf2 if 
\f1\b0 \cf0 layout 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : 
\f1\b0 layout 
\f0\b = 
\f1\b0 tryToLoad
\f0\b (
\f1\b0 name 
\f0\b + 
\f1\b0 \cf4 '.lay'
\f0\b \cf0 )\
  \cf2 if 
\f1\b0 \cf0 layout 
\f0\b == 
\f1\b0 \cf2 None 
\f0\b and 
\f1\b0 \cf0 back 
\f0\b >= 
\f1\b0 \cf4 0
\f0\b \cf0 :\
    
\f1\b0 curdir 
\f0\b = 
\f1\b0 os
\f0\b .
\f1\b0 path
\f0\b .
\f1\b0 abspath
\f0\b (
\f1\b0 \cf4 '.'
\f0\b \cf0 )\
    
\f1\b0 os
\f0\b .
\f1\b0 chdir
\f0\b (
\f1\b0 \cf4 '..'
\f0\b \cf0 )\
    
\f1\b0 layout 
\f0\b = 
\f1\b0 getLayout
\f0\b (
\f1\b0 name
\f0\b , 
\f1\b0 back 
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 )\
    
\f1\b0 os
\f0\b .
\f1\b0 chdir
\f0\b (
\f1\b0 curdir
\f0\b )\
  \cf2 return 
\f1\b0 \cf0 layout\
\

\f0\b \cf2 def 
\f1\b0 \cf0 tryToLoad
\f0\b (
\f1\b0 fullname
\f0\b ):\
  \cf2 if\cf0 (\cf2 not 
\f1\b0 \cf0 os
\f0\b .
\f1\b0 path
\f0\b .
\f1\b0 exists
\f0\b (
\f1\b0 fullname
\f0\b )): \cf2 return 
\f1\b0 None\
  
\f0\b return 
\f1\b0 \cf0 Layout
\f0\b ([
\f1\b0 line
\f0\b .
\f1\b0 strip
\f0\b () \cf2 for 
\f1\b0 \cf0 line 
\f0\b \cf2 in 
\f1\b0 \cf0 open
\f0\b (
\f1\b0 fullname
\f0\b )])}