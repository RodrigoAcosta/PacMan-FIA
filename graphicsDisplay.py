{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red15\green112\blue1;\red251\green0\blue7;
\red118\green0\blue2;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
from 
\f1\b0 \cf0 graphicsUtils 
\f0\b \cf2 import \cf0 *        \
\cf2 import 
\f1\b0 \cf0 math
\f0\b , 
\f1\b0 time\

\f0\b \cf2 from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Directions\
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 ###########################\
#  GRAPHICS DISPLAY CODE  #\
###########################\
\
# Most code by Dan Klein and John Denero written or rewritten for cs188, UC Berkeley.\
# Some code from a Pacman implementation by LiveWires, and used / modified with permission.\
\
\pard\pardeftab720\partightenfactor0

\f1\i0 \cf0 FRAME_TIME
\f0\b =.
\f1\b0 \cf4 1 
\f2\i \cf3 # The time that pacman's animation last\

\f1\i0 \cf0 PAUSE_TIME
\f0\b =
\f1\b0 \cf4 0   
\f2\i \cf3 # Pause time between frames\

\f1\i0 \cf0 DEFAULT_GRID_SIZE 
\f0\b = 
\f1\b0 \cf4 30.0\
\cf0 INFO_PANE_HEIGHT 
\f0\b = 
\f1\b0 \cf4 35\
\cf0 BACKGROUND_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 )    \

\f1\b0 WALL_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 0.0
\f0\b \cf0 /
\f1\b0 \cf4 255.0
\f0\b \cf0 , 
\f1\b0 \cf4 51.0
\f0\b \cf0 /
\f1\b0 \cf4 255.0
\f0\b \cf0 , 
\f1\b0 \cf4 255.0
\f0\b \cf0 /
\f1\b0 \cf4 255.0
\f0\b \cf0 )\

\f1\b0 INFO_PANE_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 4
\f0\b \cf0 ,.
\f1\b0 \cf4 4
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 )\

\f1\b0 SCORE_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 9
\f0\b \cf0 , .
\f1\b0 \cf4 9
\f0\b \cf0 , .
\f1\b0 \cf4 9
\f0\b \cf0 )\

\f1\b0 PACMAN_OUTLINE_WIDTH 
\f0\b = 
\f1\b0 \cf4 2\
\cf0 PACMAN_CAPTURE_OUTLINE_WIDTH 
\f0\b = 
\f1\b0 \cf4 4\
\
\cf0 GHOST_COLORS 
\f0\b = []                       \

\f1\b0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 9
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Red\

\f1\i0 \cf0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 0
\f0\b \cf0 ,.
\f1\b0 \cf4 3
\f0\b \cf0 ,.
\f1\b0 \cf4 9
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Blue\

\f1\i0 \cf0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 98
\f0\b \cf0 ,.
\f1\b0 \cf4 41
\f0\b \cf0 ,.
\f1\b0 \cf4 07
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Orange\

\f1\i0 \cf0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 1
\f0\b \cf0 ,.
\f1\b0 \cf4 75
\f0\b \cf0 ,.
\f1\b0 \cf4 7
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Green\

\f1\i0 \cf0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1.0
\f0\b \cf0 ,
\f1\b0 \cf4 0.6
\f0\b \cf0 ,
\f1\b0 \cf4 0.0
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Yellow\

\f1\i0 \cf0 GHOST_COLORS
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 formatColor
\f0\b (.
\f1\b0 \cf4 4
\f0\b \cf0 ,
\f1\b0 \cf4 0.13
\f0\b \cf0 ,
\f1\b0 \cf4 0.91
\f0\b \cf0 )) 
\f2\i\b0 \cf3 # Purple\
\

\f1\i0 \cf0 TEAM_COLORS 
\f0\b = 
\f1\b0 GHOST_COLORS
\f0\b [:
\f1\b0 \cf4 2
\f0\b \cf0 ]\
\

\f1\b0 GHOST_SHAPE 
\f0\b = [                \
    ( 
\f1\b0 \cf4 0
\f0\b \cf0 ,    
\f1\b0 \cf4 0.3 
\f0\b \cf0 ),            \
    ( 
\f1\b0 \cf4 0.25
\f0\b \cf0 , 
\f1\b0 \cf4 0.75 
\f0\b \cf0 ),           \
    ( 
\f1\b0 \cf4 0.5
\f0\b \cf0 ,  
\f1\b0 \cf4 0.3 
\f0\b \cf0 ),\
    ( 
\f1\b0 \cf4 0.75
\f0\b \cf0 , 
\f1\b0 \cf4 0.75 
\f0\b \cf0 ),\
    ( 
\f1\b0 \cf4 0.75
\f0\b \cf0 , -
\f1\b0 \cf4 0.5 
\f0\b \cf0 ),\
    ( 
\f1\b0 \cf4 0.5
\f0\b \cf0 ,  -
\f1\b0 \cf4 0.75 
\f0\b \cf0 ),\
    (-
\f1\b0 \cf4 0.5
\f0\b \cf0 ,  -
\f1\b0 \cf4 0.75 
\f0\b \cf0 ),\
    (-
\f1\b0 \cf4 0.75
\f0\b \cf0 , -
\f1\b0 \cf4 0.5 
\f0\b \cf0 ),\
    (-
\f1\b0 \cf4 0.75
\f0\b \cf0 , 
\f1\b0 \cf4 0.75 
\f0\b \cf0 ),\
    (-
\f1\b0 \cf4 0.5
\f0\b \cf0 ,  
\f1\b0 \cf4 0.3 
\f0\b \cf0 ),\
    (-
\f1\b0 \cf4 0.25
\f0\b \cf0 , 
\f1\b0 \cf4 0.75 
\f0\b \cf0 )\
  ]\

\f1\b0 GHOST_SIZE 
\f0\b = 
\f1\b0 \cf4 0.65\
\cf0 SCARED_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 )    \
\

\f1\b0 GHOST_VEC_COLORS 
\f0\b = 
\f1\b0 map
\f0\b (
\f1\b0 colorToVector
\f0\b , 
\f1\b0 GHOST_COLORS
\f0\b )\
\

\f1\b0 PACMAN_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 255.0
\f0\b \cf0 /
\f1\b0 \cf4 255.0
\f0\b \cf0 ,
\f1\b0 \cf4 255.0
\f0\b \cf0 /
\f1\b0 \cf4 255.0
\f0\b \cf0 ,
\f1\b0 \cf4 61.0
\f0\b \cf0 /
\f1\b0 \cf4 255
\f0\b \cf0 )\

\f1\b0 PACMAN_SCALE 
\f0\b = 
\f1\b0 \cf4 0.5  \
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 #pacman_speed = 0.25    \
\
# Food\
\pard\pardeftab720\partightenfactor0

\f1\i0 \cf0 FOOD_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 )     \

\f1\b0 FOOD_SIZE 
\f0\b = 
\f1\b0 \cf4 0.1    \
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 # Laser\
\pard\pardeftab720\partightenfactor0

\f1\i0 \cf0 LASER_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 )     \

\f1\b0 LASER_SIZE 
\f0\b = 
\f1\b0 \cf4 0.02   \
        \
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 # Capsule graphics\
\pard\pardeftab720\partightenfactor0

\f1\i0 \cf0 CAPSULE_COLOR 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 ,
\f1\b0 \cf4 1
\f0\b \cf0 )\

\f1\b0 CAPSULE_SIZE 
\f0\b = 
\f1\b0 \cf4 0.25 \
\
\pard\pardeftab720\partightenfactor0

\f2\i \cf3 # Drawing walls\
\pard\pardeftab720\partightenfactor0

\f1\i0 \cf0 WALL_RADIUS 
\f0\b = 
\f1\b0 \cf4 0.15\
\

\f0\b \cf2 class 
\f1\b0 \cf0 InfoPane
\f0\b :\
  \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 layout
\f0\b , 
\f1\b0 gridSize
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize 
\f0\b = 
\f1\b0 gridSize\
    \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b = (
\f1\b0 layout
\f0\b .
\f1\b0 width
\f0\b ) * 
\f1\b0 gridSize\
    \cf2 self
\f0\b \cf0 .
\f1\b0 base 
\f0\b = (
\f1\b0 layout
\f0\b .
\f1\b0 height 
\f0\b + 
\f1\b0 \cf4 1
\f0\b \cf0 ) * 
\f1\b0 gridSize\
    \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b = 
\f1\b0 INFO_PANE_HEIGHT \
    \cf2 self
\f0\b \cf0 .
\f1\b0 fontSize 
\f0\b = 
\f1\b0 \cf4 24\
    \cf2 self
\f0\b \cf0 .
\f1\b0 textColor 
\f0\b = 
\f1\b0 PACMAN_COLOR\
    \cf2 self
\f0\b \cf0 .
\f1\b0 drawPane
\f0\b ()\
\
  \cf2 def 
\f1\b0 \cf0 toScreen
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pos
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    
\f1\b0 \cf5 """\
      Translates a point relative from the bottom left of the info pane.\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 y 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      
\f1\b0 x
\f0\b ,
\f1\b0 y 
\f0\b = 
\f1\b0 pos\
    
\f0\b \cf2 else\cf0 :\
      
\f1\b0 x 
\f0\b = 
\f1\b0 pos\
      \
    x 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize 
\f0\b + 
\f1\b0 x 
\f2\i \cf3 # Margin\
    
\f1\i0 \cf0 y 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 base 
\f0\b + 
\f1\b0 y \
    
\f0\b \cf2 return 
\f1\b0 \cf0 x
\f0\b ,
\f1\b0 y\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 drawPane
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 scoreText 
\f0\b = 
\f1\b0 text
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 toScreen
\f0\b (
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 \cf4 0  
\f0\b \cf0 ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 textColor
\f0\b , 
\f1\b0 \cf4 "SCORE:    0"
\f0\b \cf0 , 
\f1\b0 \cf4 "Times"
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 fontSize
\f0\b , 
\f1\b0 \cf4 "bold"
\f0\b \cf0 )\
\
  \cf2 def 
\f1\b0 \cf0 initializeGhostDistances
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 distances
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 ghostDistanceText 
\f0\b = []\
    \
    
\f1\b0 size 
\f0\b = 
\f1\b0 \cf4 20\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b < 
\f1\b0 \cf4 240
\f0\b \cf0 :\
      
\f1\b0 size 
\f0\b = 
\f1\b0 \cf4 12\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b < 
\f1\b0 \cf4 160
\f0\b \cf0 :\
      
\f1\b0 size 
\f0\b = 
\f1\b0 \cf4 10\
      \
    
\f0\b \cf2 for 
\f1\b0 \cf0 i
\f0\b , 
\f1\b0 d 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 distances
\f0\b ):\
      
\f1\b0 t 
\f0\b = 
\f1\b0 text
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 toScreen
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b /
\f1\b0 \cf4 2 
\f0\b \cf0 + 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b /
\f1\b0 \cf4 8 
\f0\b \cf0 * 
\f1\b0 i
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 ), 
\f1\b0 GHOST_COLORS
\f0\b [
\f1\b0 i
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 ], 
\f1\b0 d
\f0\b , 
\f1\b0 \cf4 "Times"
\f0\b \cf0 , 
\f1\b0 size
\f0\b , 
\f1\b0 \cf4 "bold"
\f0\b \cf0 )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 ghostDistanceText
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 t
\f0\b )\
          \
  \cf2 def 
\f1\b0 \cf0 updateScore
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 score
\f0\b ):\
    
\f1\b0 changeText
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 scoreText
\f0\b , 
\f1\b0 \cf4 "SCORE: % 4d" 
\f0\b \cf0 % 
\f1\b0 score
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 setTeam
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 isBlue
\f0\b ):\
    
\f1\b0 text 
\f0\b = 
\f1\b0 \cf4 "RED TEAM"\
    
\f0\b \cf2 if 
\f1\b0 \cf0 isBlue
\f0\b : 
\f1\b0 text 
\f0\b = 
\f1\b0 \cf4 "BLUE TEAM"\
    \cf2 self
\f0\b \cf0 .
\f1\b0 teamText 
\f0\b = 
\f1\b0 text
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 toScreen
\f0\b (
\f1\b0 \cf4 300
\f0\b \cf0 , 
\f1\b0 \cf4 0  
\f0\b \cf0 ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 textColor
\f0\b , 
\f1\b0 text
\f0\b , 
\f1\b0 \cf4 "Times"
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 fontSize
\f0\b , 
\f1\b0 \cf4 "bold"
\f0\b \cf0 )\
    \
  \cf2 def 
\f1\b0 \cf0 updateGhostDistances
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 distances
\f0\b ):\
    \cf2 if 
\f1\b0 \cf4 'ghostDistanceText' 
\f0\b \cf2 not in 
\f1\b0 \cf0 dir
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ): 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 initializeGhostDistances
\f0\b (
\f1\b0 distances
\f0\b )\
    \cf2 else\cf0 :\
      \cf2 for 
\f1\b0 \cf0 i
\f0\b , 
\f1\b0 d 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 distances
\f0\b ):\
        
\f1\b0 changeText
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 ghostDistanceText
\f0\b [
\f1\b0 i
\f0\b ], 
\f1\b0 d
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 drawGhost
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
  \
  def 
\f1\b0 \cf0 drawPacman
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
    \
  def 
\f1\b0 \cf0 drawWarning
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
    \
  def 
\f1\b0 \cf0 clearIcon
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
    \
  def 
\f1\b0 \cf0 updateMessage
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 message
\f0\b ):\
    \cf2 pass\
    \
  def 
\f1\b0 \cf0 clearMessage
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
\
\
class 
\f1\b0 \cf0 PacmanGraphics
\f0\b :\
  \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 zoom
\f0\b =
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 capture 
\f0\b = \cf2 False\cf0 ):  \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 have_window 
\f0\b = 
\f1\b0 \cf4 0\
    \cf2 self
\f0\b \cf0 .
\f1\b0 currentGhostImages 
\f0\b = \{\}\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pacmanImage 
\f0\b = 
\f1\b0 \cf2 None\
    self
\f0\b \cf0 .
\f1\b0 zoom 
\f0\b = 
\f1\b0 zoom\
    \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize 
\f0\b = 
\f1\b0 DEFAULT_GRID_SIZE 
\f0\b * 
\f1\b0 zoom\
    \cf2 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b = 
\f1\b0 capture\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 initialize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b , 
\f1\b0 isBlue 
\f0\b = \cf2 False\cf0 ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isBlue 
\f0\b = 
\f1\b0 isBlue\
    \cf2 self
\f0\b \cf0 .
\f1\b0 startGraphics
\f0\b (
\f1\b0 state
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawStaticObjects
\f0\b (
\f1\b0 state
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawAgentObjects
\f0\b (
\f1\b0 state
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 startGraphics
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 layout\
    layout 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout\
    \cf2 self
\f0\b \cf0 .
\f1\b0 width 
\f0\b = 
\f1\b0 layout
\f0\b .
\f1\b0 width\
    \cf2 self
\f0\b \cf0 .
\f1\b0 height 
\f0\b = 
\f1\b0 layout
\f0\b .
\f1\b0 height\
    \cf2 self
\f0\b \cf0 .
\f1\b0 make_window
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 width
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 infoPane 
\f0\b = 
\f1\b0 InfoPane
\f0\b (
\f1\b0 layout
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 currentState 
\f0\b = 
\f1\b0 layout\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 drawStaticObjects
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    
\f1\b0 layout 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout\
    \cf2 self
\f0\b \cf0 .
\f1\b0 drawWalls
\f0\b (
\f1\b0 layout
\f0\b .
\f1\b0 walls
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawFood
\f0\b (
\f1\b0 layout
\f0\b .
\f1\b0 food
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawCapsules
\f0\b (
\f1\b0 layout
\f0\b .
\f1\b0 capsules
\f0\b )\
    
\f1\b0 refresh\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 drawAgentObjects
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages 
\f0\b = [] 
\f2\i\b0 \cf3 # (agentState, image)\
    
\f0\i0\b \cf2 for 
\f1\b0 \cf0 index
\f0\b , 
\f1\b0 agent 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 state
\f0\b .
\f1\b0 agentStates
\f0\b ):\
      \cf2 if 
\f1\b0 \cf0 agent
\f0\b .
\f1\b0 isPacman
\f0\b :\
        
\f1\b0 image 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawPacman
\f0\b (
\f1\b0 agent
\f0\b , 
\f1\b0 index
\f0\b )\
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 agent
\f0\b , 
\f1\b0 image
\f0\b ) )\
      \cf2 else\cf0 :  \
        
\f1\b0 image 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawGhost
\f0\b (
\f1\b0 agent
\f0\b , 
\f1\b0 index
\f0\b )\
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b .
\f1\b0 append
\f0\b ( (
\f1\b0 agent
\f0\b , 
\f1\b0 image
\f0\b ) )\
    
\f1\b0 refresh\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 swapImages
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 agentIndex
\f0\b , 
\f1\b0 newState
\f0\b ):\
    
\f1\b0 \cf5 """\
      Changes an image from a ghost to a pacman or vis versa (for capture)\
    """\
    \cf0 prevState
\f0\b , 
\f1\b0 prevImage 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ]\
    \cf2 for 
\f1\b0 \cf0 item 
\f0\b \cf2 in 
\f1\b0 \cf0 prevImage
\f0\b : 
\f1\b0 remove_from_screen
\f0\b (
\f1\b0 item
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 newState
\f0\b .
\f1\b0 isPacman
\f0\b :\
      
\f1\b0 image 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawPacman
\f0\b (
\f1\b0 newState
\f0\b , 
\f1\b0 agentIndex
\f0\b )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ] = (
\f1\b0 newState
\f0\b , 
\f1\b0 image 
\f0\b )\
    \cf2 else\cf0 :\
      
\f1\b0 image 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawGhost
\f0\b (
\f1\b0 newState
\f0\b , 
\f1\b0 agentIndex
\f0\b )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ] = (
\f1\b0 newState
\f0\b , 
\f1\b0 image 
\f0\b )\
    
\f1\b0 refresh\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 update
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 newState
\f0\b ):\
    
\f1\b0 agentIndex 
\f0\b = 
\f1\b0 newState
\f0\b .
\f1\b0 _agentMoved\
    agentState 
\f0\b = 
\f1\b0 newState
\f0\b .
\f1\b0 agentStates
\f0\b [
\f1\b0 agentIndex
\f0\b ]\
\
    \cf2 if 
\f1\b0 \cf0 agentIndex 
\f0\b == 
\f1\b0 \cf4 0 
\f0\b \cf2 and 
\f1\b0 \cf0 PAUSE_TIME 
\f0\b > 
\f1\b0 \cf4 0
\f0\b \cf0 :\
      
\f1\b0 sleep
\f0\b (
\f1\b0 PAUSE_TIME
\f0\b )\
      
\f1\b0 refresh\
\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ][
\f1\b0 \cf4 0
\f0\b \cf0 ].
\f1\b0 isPacman 
\f0\b != 
\f1\b0 agentState
\f0\b .
\f1\b0 isPacman
\f0\b : 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 swapImages
\f0\b (
\f1\b0 agentIndex
\f0\b , 
\f1\b0 agentState
\f0\b )\
    
\f1\b0 prevState
\f0\b , 
\f1\b0 prevImage 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ]\
    \cf2 if 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 isPacman
\f0\b :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 animatePacman
\f0\b (
\f1\b0 agentState
\f0\b , 
\f1\b0 prevState
\f0\b , 
\f1\b0 prevImage
\f0\b )\
    \cf2 else\cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 moveGhost
\f0\b (
\f1\b0 agentState
\f0\b , 
\f1\b0 agentIndex
\f0\b , 
\f1\b0 prevState
\f0\b , 
\f1\b0 prevImage
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentImages
\f0\b [
\f1\b0 agentIndex
\f0\b ] = (
\f1\b0 agentState
\f0\b , 
\f1\b0 prevImage
\f0\b )\
      \
    \cf2 if 
\f1\b0 \cf0 newState
\f0\b .
\f1\b0 _foodEaten 
\f0\b != 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 removeFood
\f0\b (
\f1\b0 newState
\f0\b .
\f1\b0 _foodEaten
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 food
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 newState
\f0\b .
\f1\b0 _capsuleEaten 
\f0\b != 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 removeCapsule
\f0\b (
\f1\b0 newState
\f0\b .
\f1\b0 _capsuleEaten
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 capsules
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 infoPane
\f0\b .
\f1\b0 updateScore
\f0\b (
\f1\b0 newState
\f0\b .
\f1\b0 score
\f0\b )\
      \
  \cf2 def 
\f1\b0 \cf0 make_window
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 width
\f0\b , 
\f1\b0 height
\f0\b ):\
    
\f1\b0 grid_width 
\f0\b = (
\f1\b0 width
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 ) * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize \
    grid_height 
\f0\b = (
\f1\b0 height
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 ) * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize \
    screen_width 
\f0\b = 
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize 
\f0\b + 
\f1\b0 grid_width\
    screen_height 
\f0\b = 
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize 
\f0\b + 
\f1\b0 grid_height 
\f0\b + 
\f1\b0 INFO_PANE_HEIGHT \
\
    begin_graphics
\f0\b (
\f1\b0 screen_width
\f0\b ,    \
                   
\f1\b0 screen_height
\f0\b ,\
                   
\f1\b0 BACKGROUND_COLOR
\f0\b ,\
                   
\f1\b0 \cf4 "CS188 Pacman"
\f0\b \cf0 )\
    \
  \cf2 def 
\f1\b0 \cf0 drawPacman
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pacman
\f0\b , 
\f1\b0 index
\f0\b ):\
    
\f1\b0 position 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 pacman
\f0\b )\
    
\f1\b0 screen_point 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 position
\f0\b )\
    
\f1\b0 endpoints 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getEndpoints
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDirection
\f0\b (
\f1\b0 pacman
\f0\b ))\
    \
    
\f1\b0 width 
\f0\b = 
\f1\b0 PACMAN_OUTLINE_WIDTH\
    outlineColor 
\f0\b = 
\f1\b0 PACMAN_COLOR\
    fillColor 
\f0\b = 
\f1\b0 PACMAN_COLOR\
\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capture
\f0\b :\
      
\f1\b0 outlineColor 
\f0\b = 
\f1\b0 TEAM_COLORS
\f0\b [
\f1\b0 index 
\f0\b % 
\f1\b0 \cf4 2
\f0\b \cf0 ]\
      
\f1\b0 fillColor 
\f0\b = 
\f1\b0 GHOST_COLORS
\f0\b [
\f1\b0 index
\f0\b ]  \
      
\f1\b0 width 
\f0\b = 
\f1\b0 PACMAN_CAPTURE_OUTLINE_WIDTH\
      \
    
\f0\b \cf2 return \cf0 [
\f1\b0 circle
\f0\b (
\f1\b0 screen_point
\f0\b , 
\f1\b0 PACMAN_SCALE 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , \
                   
\f1\b0 fillColor 
\f0\b = 
\f1\b0 fillColor
\f0\b , 
\f1\b0 outlineColor 
\f0\b = 
\f1\b0 outlineColor
\f0\b , \
                   
\f1\b0 endpoints 
\f0\b = 
\f1\b0 endpoints
\f0\b ,\
                   
\f1\b0 width 
\f0\b = 
\f1\b0 width
\f0\b )]\
    \
  \cf2 def 
\f1\b0 \cf0 getEndpoints
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 direction
\f0\b , 
\f1\b0 position
\f0\b =(
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 )):\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 position\
    pos 
\f0\b = 
\f1\b0 x 
\f0\b - 
\f1\b0 int
\f0\b (
\f1\b0 x
\f0\b ) + 
\f1\b0 y 
\f0\b - 
\f1\b0 int
\f0\b (
\f1\b0 y
\f0\b )\
    
\f1\b0 width 
\f0\b = 
\f1\b0 \cf4 30 
\f0\b \cf0 + 
\f1\b0 \cf4 80 
\f0\b \cf0 * 
\f1\b0 math
\f0\b .
\f1\b0 sin
\f0\b (
\f1\b0 math
\f0\b .
\f1\b0 pi
\f0\b *
\f1\b0 pos
\f0\b )\
    \
    
\f1\b0 delta 
\f0\b = 
\f1\b0 width 
\f0\b / 
\f1\b0 \cf4 2\
    
\f0\b \cf2 if \cf0 (
\f1\b0 direction 
\f0\b == 
\f1\b0 \cf4 'West'
\f0\b \cf0 ):\
      
\f1\b0 endpoints 
\f0\b = (
\f1\b0 \cf4 180
\f0\b \cf0 +
\f1\b0 delta
\f0\b , 
\f1\b0 \cf4 180
\f0\b \cf0 -
\f1\b0 delta
\f0\b )\
    \cf2 elif \cf0 (
\f1\b0 direction 
\f0\b == 
\f1\b0 \cf4 'North'
\f0\b \cf0 ):\
      
\f1\b0 endpoints 
\f0\b = (
\f1\b0 \cf4 90
\f0\b \cf0 +
\f1\b0 delta
\f0\b , 
\f1\b0 \cf4 90
\f0\b \cf0 -
\f1\b0 delta
\f0\b )\
    \cf2 elif \cf0 (
\f1\b0 direction 
\f0\b == 
\f1\b0 \cf4 'South'
\f0\b \cf0 ):\
      
\f1\b0 endpoints 
\f0\b = (
\f1\b0 \cf4 270
\f0\b \cf0 +
\f1\b0 delta
\f0\b , 
\f1\b0 \cf4 270
\f0\b \cf0 -
\f1\b0 delta
\f0\b )\
    \cf2 else\cf0 :\
      
\f1\b0 endpoints 
\f0\b = (
\f1\b0 \cf4 0
\f0\b \cf0 +
\f1\b0 delta
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 -
\f1\b0 delta
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 endpoints\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 movePacman
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 position
\f0\b , 
\f1\b0 direction
\f0\b , 
\f1\b0 image
\f0\b ):\
    
\f1\b0 screenPosition 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 position
\f0\b )\
    
\f1\b0 endpoints 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getEndpoints
\f0\b ( 
\f1\b0 direction
\f0\b , 
\f1\b0 position 
\f0\b )\
    
\f1\b0 r 
\f0\b = 
\f1\b0 PACMAN_SCALE 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize \
    moveCircle
\f0\b (
\f1\b0 image
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ], 
\f1\b0 screenPosition
\f0\b , 
\f1\b0 r
\f0\b , 
\f1\b0 endpoints
\f0\b )\
    
\f1\b0 refresh\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 animatePacman
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pacman
\f0\b , 
\f1\b0 prevPacman
\f0\b , 
\f1\b0 image
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 FRAME_TIME 
\f0\b > 
\f1\b0 \cf4 0.01
\f0\b \cf0 :\
      
\f1\b0 start 
\f0\b = 
\f1\b0 time
\f0\b .
\f1\b0 time
\f0\b ()\
      
\f1\b0 fx
\f0\b , 
\f1\b0 fy 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 prevPacman
\f0\b )\
      
\f1\b0 px
\f0\b , 
\f1\b0 py 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 pacman
\f0\b )\
      
\f1\b0 frames 
\f0\b = 
\f1\b0 \cf4 4.0\
      
\f0\b \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 int
\f0\b (
\f1\b0 frames
\f0\b )):\
        
\f1\b0 pos 
\f0\b = 
\f1\b0 px
\f0\b *
\f1\b0 i
\f0\b /
\f1\b0 frames 
\f0\b + 
\f1\b0 fx
\f0\b *(
\f1\b0 frames
\f0\b -
\f1\b0 i
\f0\b )/
\f1\b0 frames
\f0\b , 
\f1\b0 py
\f0\b *
\f1\b0 i
\f0\b /
\f1\b0 frames 
\f0\b + 
\f1\b0 fy
\f0\b *(
\f1\b0 frames
\f0\b -
\f1\b0 i
\f0\b )/
\f1\b0 frames \
        \cf2 self
\f0\b \cf0 .
\f1\b0 movePacman
\f0\b (
\f1\b0 pos
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDirection
\f0\b (
\f1\b0 pacman
\f0\b ), 
\f1\b0 image
\f0\b )\
        
\f2\i\b0 \cf3 # if time.time() - start > FRAME_TIME: return\
        
\f1\i0 \cf0 sleep
\f0\b (
\f1\b0 FRAME_TIME 
\f0\b / 
\f1\b0 \cf4 2 
\f0\b \cf0 / 
\f1\b0 frames
\f0\b )\
    \cf2 else\cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 movePacman
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 pacman
\f0\b ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDirection
\f0\b (
\f1\b0 pacman
\f0\b ), 
\f1\b0 image
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 getGhostColor
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghost
\f0\b , 
\f1\b0 ghostIndex
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 ghost
\f0\b .
\f1\b0 scaredTimer 
\f0\b > 
\f1\b0 \cf4 0
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 \cf0 SCARED_COLOR\
    
\f0\b \cf2 else\cf0 :\
      \cf2 return 
\f1\b0 \cf0 GHOST_COLORS
\f0\b [
\f1\b0 ghostIndex
\f0\b ]\
\
  \cf2 def 
\f1\b0 \cf0 drawGhost
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghost
\f0\b , 
\f1\b0 agentIndex
\f0\b ):\
    
\f1\b0 pos 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 ghost
\f0\b )\
    
\f1\b0 dir 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDirection
\f0\b (
\f1\b0 ghost
\f0\b )\
    (
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y
\f0\b ) = (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 pos
\f0\b ) ) \
    
\f1\b0 coords 
\f0\b = []          \
    \cf2 for \cf0 (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ) \cf2 in 
\f1\b0 \cf0 GHOST_SHAPE
\f0\b :\
      
\f1\b0 coords
\f0\b .
\f1\b0 append
\f0\b ((
\f1\b0 x
\f0\b *
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE 
\f0\b + 
\f1\b0 screen_x
\f0\b , 
\f1\b0 y
\f0\b *
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE 
\f0\b + 
\f1\b0 screen_y
\f0\b ))\
\
    
\f1\b0 colour 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getGhostColor
\f0\b (
\f1\b0 ghost
\f0\b , 
\f1\b0 agentIndex
\f0\b )\
    
\f1\b0 body 
\f0\b = 
\f1\b0 polygon
\f0\b (
\f1\b0 coords
\f0\b , 
\f1\b0 colour
\f0\b , 
\f1\b0 filled 
\f0\b = 
\f1\b0 \cf4 1
\f0\b \cf0 )\
    
\f1\b0 WHITE 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 \cf4 1.0
\f0\b \cf0 )\
    
\f1\b0 BLACK 
\f0\b = 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf4 0.0
\f0\b \cf0 , 
\f1\b0 \cf4 0.0
\f0\b \cf0 , 
\f1\b0 \cf4 0.0
\f0\b \cf0 )\
    \
    
\f1\b0 dx 
\f0\b = 
\f1\b0 \cf4 0\
    \cf0 dy 
\f0\b = 
\f1\b0 \cf4 0\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'North'
\f0\b \cf0 :\
      
\f1\b0 dy 
\f0\b = -
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'South'
\f0\b \cf0 :\
      
\f1\b0 dy 
\f0\b = 
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'East'
\f0\b \cf0 :\
      
\f1\b0 dx 
\f0\b = 
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'West'
\f0\b \cf0 :\
      
\f1\b0 dx 
\f0\b = -
\f1\b0 \cf4 0.2\
    \cf0 leftEye 
\f0\b = 
\f1\b0 circle
\f0\b ((
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(-
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.2
\f0\b \cf0 , 
\f1\b0 WHITE
\f0\b , 
\f1\b0 WHITE
\f0\b )\
    
\f1\b0 rightEye 
\f0\b = 
\f1\b0 circle
\f0\b ((
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.2
\f0\b \cf0 , 
\f1\b0 WHITE
\f0\b , 
\f1\b0 WHITE
\f0\b )\
    
\f1\b0 leftPupil 
\f0\b = 
\f1\b0 circle
\f0\b ((
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(-
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.08
\f0\b \cf0 , 
\f1\b0 BLACK
\f0\b , 
\f1\b0 BLACK
\f0\b )\
    
\f1\b0 rightPupil 
\f0\b = 
\f1\b0 circle
\f0\b ((
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.08
\f0\b \cf0 , 
\f1\b0 BLACK
\f0\b , 
\f1\b0 BLACK
\f0\b )\
    
\f1\b0 ghostImageParts 
\f0\b = []\
    
\f1\b0 ghostImageParts
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 body
\f0\b )\
    
\f1\b0 ghostImageParts
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 leftEye
\f0\b )\
    
\f1\b0 ghostImageParts
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 rightEye
\f0\b )\
    
\f1\b0 ghostImageParts
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 leftPupil
\f0\b )\
    
\f1\b0 ghostImageParts
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 rightPupil
\f0\b )\
    \
    \cf2 return 
\f1\b0 \cf0 ghostImageParts\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 moveEyes
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 pos
\f0\b , 
\f1\b0 dir
\f0\b , 
\f1\b0 eyes
\f0\b ):\
    (
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y
\f0\b ) = (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 pos
\f0\b ) ) \
    
\f1\b0 dx 
\f0\b = 
\f1\b0 \cf4 0\
    \cf0 dy 
\f0\b = 
\f1\b0 \cf4 0\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'North'
\f0\b \cf0 :\
      
\f1\b0 dy 
\f0\b = -
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'South'
\f0\b \cf0 :\
      
\f1\b0 dy 
\f0\b = 
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'East'
\f0\b \cf0 :\
      
\f1\b0 dx 
\f0\b = 
\f1\b0 \cf4 0.2\
    
\f0\b \cf2 if 
\f1\b0 \cf0 dir 
\f0\b == 
\f1\b0 \cf4 'West'
\f0\b \cf0 :\
      
\f1\b0 dx 
\f0\b = -
\f1\b0 \cf4 0.2\
    \cf0 moveCircle
\f0\b (
\f1\b0 eyes
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ],(
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(-
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.2
\f0\b \cf0 )\
    
\f1\b0 moveCircle
\f0\b (
\f1\b0 eyes
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ],(
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b /
\f1\b0 \cf4 1.5
\f0\b \cf0 )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.2
\f0\b \cf0 )\
    
\f1\b0 moveCircle
\f0\b (
\f1\b0 eyes
\f0\b [
\f1\b0 \cf4 2
\f0\b \cf0 ],(
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(-
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.08
\f0\b \cf0 )\
    
\f1\b0 moveCircle
\f0\b (
\f1\b0 eyes
\f0\b [
\f1\b0 \cf4 3
\f0\b \cf0 ],(
\f1\b0 screen_x
\f0\b +
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 +
\f1\b0 dx
\f0\b ), 
\f1\b0 screen_y
\f0\b -
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *(
\f1\b0 \cf4 0.3
\f0\b \cf0 -
\f1\b0 dy
\f0\b )), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 GHOST_SIZE
\f0\b *
\f1\b0 \cf4 0.08
\f0\b \cf0 )\
    \
  \cf2 def 
\f1\b0 \cf0 moveGhost
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghost
\f0\b , 
\f1\b0 ghostIndex
\f0\b , 
\f1\b0 prevGhost
\f0\b , 
\f1\b0 ghostImageParts
\f0\b ):\
    
\f1\b0 old_x
\f0\b , 
\f1\b0 old_y 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 prevGhost
\f0\b ))\
    
\f1\b0 new_x
\f0\b , 
\f1\b0 new_y 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 ghost
\f0\b ))\
    
\f1\b0 delta 
\f0\b = 
\f1\b0 new_x 
\f0\b - 
\f1\b0 old_x
\f0\b , 
\f1\b0 new_y 
\f0\b - 
\f1\b0 old_y\
    \
    
\f0\b \cf2 for 
\f1\b0 \cf0 ghostImagePart 
\f0\b \cf2 in 
\f1\b0 \cf0 ghostImageParts
\f0\b :\
      
\f1\b0 move_by
\f0\b (
\f1\b0 ghostImagePart
\f0\b , 
\f1\b0 delta
\f0\b )\
    
\f1\b0 refresh\
    \
    
\f0\b \cf2 if 
\f1\b0 \cf0 ghost
\f0\b .
\f1\b0 scaredTimer 
\f0\b > 
\f1\b0 \cf4 0
\f0\b \cf0 :\
      
\f1\b0 color 
\f0\b = 
\f1\b0 SCARED_COLOR\
    
\f0\b \cf2 else\cf0 :\
      
\f1\b0 color 
\f0\b = 
\f1\b0 GHOST_COLORS
\f0\b [
\f1\b0 ghostIndex
\f0\b ]\
    
\f1\b0 edit
\f0\b (
\f1\b0 ghostImageParts
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ], (
\f1\b0 \cf4 'fill'
\f0\b \cf0 , 
\f1\b0 color
\f0\b ), (
\f1\b0 \cf4 'outline'
\f0\b \cf0 , 
\f1\b0 color
\f0\b ))  \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 moveEyes
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getPosition
\f0\b (
\f1\b0 ghost
\f0\b ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getDirection
\f0\b (
\f1\b0 ghost
\f0\b ), 
\f1\b0 ghostImageParts
\f0\b [-
\f1\b0 \cf4 4
\f0\b \cf0 :])\
    
\f1\b0 refresh\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 agentState
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 configuration 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return \cf0 (-
\f1\b0 \cf4 1000
\f0\b \cf0 , -
\f1\b0 \cf4 1000
\f0\b \cf0 )\
    \cf2 return 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 getPosition
\f0\b ()\
  \
  \cf2 def 
\f1\b0 \cf0 getDirection
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 agentState
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 configuration 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : \cf2 return 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 STOP\
    
\f0\b \cf2 return 
\f1\b0 \cf0 agentState
\f0\b .
\f1\b0 configuration
\f0\b .
\f1\b0 getDirection
\f0\b ()\
  \
  \cf2 def 
\f1\b0 \cf0 finish
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 end_graphics
\f0\b ()\
  \
  \cf2 def 
\f1\b0 \cf0 to_screen
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 point
\f0\b ):\
    ( 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b ) = 
\f1\b0 point\
    
\f2\i \cf3 #y = self.height - y\
    
\f1\i0 \cf0 x 
\f0\b = (
\f1\b0 x 
\f0\b + 
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize\
    y 
\f0\b = (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height  
\f0\b - 
\f1\b0 y
\f0\b )*
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize\
    
\f0\b \cf2 return \cf0 ( 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b )\
  \
  
\f2\i\b0 \cf3 # Fixes some TK issue with off-center circles\
  
\f0\i0\b \cf2 def 
\f1\b0 \cf0 to_screen2
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 point
\f0\b ):\
    ( 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b ) = 
\f1\b0 point\
    
\f2\i \cf3 #y = self.height - y\
    
\f1\i0 \cf0 x 
\f0\b = (
\f1\b0 x 
\f0\b + 
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize\
    y 
\f0\b = (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 height  
\f0\b - 
\f1\b0 y
\f0\b )*
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize\
    
\f0\b \cf2 return \cf0 ( 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 drawWalls
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b ):\
    
\f1\b0 wallColor 
\f0\b = 
\f1\b0 WALL_COLOR\
    
\f0\b \cf2 for 
\f1\b0 \cf0 xNum
\f0\b , 
\f1\b0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 wallMatrix
\f0\b ):\
      \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b \cf2 and \cf0 (
\f1\b0 xNum 
\f0\b * 
\f1\b0 \cf4 2
\f0\b \cf0 ) < 
\f1\b0 wallMatrix
\f0\b .
\f1\b0 width
\f0\b : 
\f1\b0 wallColor 
\f0\b = 
\f1\b0 TEAM_COLORS
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ]\
      \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b \cf2 and \cf0 (
\f1\b0 xNum 
\f0\b * 
\f1\b0 \cf4 2
\f0\b \cf0 ) >= 
\f1\b0 wallMatrix
\f0\b .
\f1\b0 width
\f0\b : 
\f1\b0 wallColor 
\f0\b = 
\f1\b0 TEAM_COLORS
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ]\
\
      \cf2 for 
\f1\b0 \cf0 yNum
\f0\b , 
\f1\b0 cell 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 x
\f0\b ):\
        \cf2 if 
\f1\b0 \cf0 cell
\f0\b : 
\f2\i\b0 \cf3 # There's a wall here\
          
\f1\i0 \cf0 pos 
\f0\b = (
\f1\b0 xNum
\f0\b , 
\f1\b0 yNum
\f0\b )\
          
\f1\b0 screen 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 pos
\f0\b )\
          
\f1\b0 screen2 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen2
\f0\b (
\f1\b0 pos
\f0\b )\
          \
          
\f2\i\b0 \cf3 # draw each quadrant of the square based on adjacent walls\
          
\f1\i0 \cf0 wIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 eIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 nIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b , 
\f1\b0 yNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 sIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b , 
\f1\b0 yNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 nwIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 swIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 neIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          
\f1\b0 seIsWall 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isWall
\f0\b (
\f1\b0 xNum
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 yNum
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallMatrix
\f0\b )\
          \
          
\f2\i\b0 \cf3 # NE quadrant\
          
\f0\i0\b \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 nIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # inner circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 screen2
\f0\b , 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 91
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
          \cf2 if \cf0 (
\f1\b0 nIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # vertical line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 )-
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 nIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # horizontal line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 0.5
\f0\b \cf0 +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (
\f1\b0 nIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 eIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 neIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # outer circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen2
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 180
\f0\b \cf0 ,
\f1\b0 \cf4 271
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 WALL_RADIUS
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 0.5
\f0\b \cf0 +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 ))), 
\f1\b0 wallColor
\f0\b )\
          \
          
\f2\i\b0 \cf3 # NW quadrant\
          
\f0\i0\b \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 nIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # inner circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 screen2
\f0\b , 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 90
\f0\b \cf0 ,
\f1\b0 \cf4 181
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
          \cf2 if \cf0 (
\f1\b0 nIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # vertical line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 )-
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 nIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # horizontal line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 )-
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (
\f1\b0 nIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 wIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 nwIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # outer circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen2
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 270
\f0\b \cf0 ,
\f1\b0 \cf4 361
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 ))), 
\f1\b0 wallColor
\f0\b )\
          \
          
\f2\i\b0 \cf3 # SE quadrant\
          
\f0\i0\b \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 sIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # inner circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 screen2
\f0\b , 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 270
\f0\b \cf0 ,
\f1\b0 \cf4 361
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
          \cf2 if \cf0 (
\f1\b0 sIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # vertical line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 0.5
\f0\b \cf0 )+
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 sIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 eIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # horizontal line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 0.5
\f0\b \cf0 +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (
\f1\b0 sIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 eIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 seIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # outer circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen2
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 90
\f0\b \cf0 ,
\f1\b0 \cf4 181
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 2
\f0\b \cf0 *
\f1\b0 WALL_RADIUS
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 \cf4 0.5
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 0.5
\f0\b \cf0 ))), 
\f1\b0 wallColor
\f0\b )\
          \
          
\f2\i\b0 \cf3 # SW quadrant\
          
\f0\i0\b \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 sIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # inner circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 screen2
\f0\b , 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 180
\f0\b \cf0 ,
\f1\b0 \cf4 271
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
          \cf2 if \cf0 (
\f1\b0 sIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # vertical line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf4 0
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 0.5
\f0\b \cf0 )+
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (\cf2 not 
\f1\b0 \cf0 sIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 wIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # horizontal line\
            
\f1\i0 \cf0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 )-
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
          \cf2 if \cf0 (
\f1\b0 sIsWall
\f0\b ) \cf2 and \cf0 (
\f1\b0 wIsWall
\f0\b ) \cf2 and \cf0 (\cf2 not 
\f1\b0 \cf0 swIsWall
\f0\b ):\
            
\f2\i\b0 \cf3 # outer circle\
            
\f1\i0 \cf0 circle
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen2
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 WALL_RADIUS 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 wallColor
\f0\b , 
\f1\b0 wallColor
\f0\b , (
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 91
\f0\b \cf0 ), 
\f1\b0 \cf4 'arc'
\f0\b \cf0 )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b +
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 0.5
\f0\b \cf0 ), 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b )), 
\f1\b0 wallColor
\f0\b )\
            
\f1\b0 line
\f0\b (
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 2
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b -
\f1\b0 \cf4 1
\f0\b \cf0 )), 
\f1\b0 add
\f0\b (
\f1\b0 screen
\f0\b , (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(-
\f1\b0 \cf4 1
\f0\b \cf0 )*
\f1\b0 WALL_RADIUS
\f0\b , 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b *(
\f1\b0 \cf4 0.5
\f0\b \cf0 ))), 
\f1\b0 wallColor
\f0\b )\
          \
  \cf2 def 
\f1\b0 \cf0 isWall
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b , 
\f1\b0 walls
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 x 
\f0\b < 
\f1\b0 \cf4 0 
\f0\b \cf2 or 
\f1\b0 \cf0 y 
\f0\b < 
\f1\b0 \cf4 0
\f0\b \cf0 :\
      \cf2 return False\
    if 
\f1\b0 \cf0 x 
\f0\b >= 
\f1\b0 walls
\f0\b .
\f1\b0 width 
\f0\b \cf2 or 
\f1\b0 \cf0 y 
\f0\b >= 
\f1\b0 walls
\f0\b .
\f1\b0 height
\f0\b :\
      \cf2 return False\
    return 
\f1\b0 \cf0 walls
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 drawFood
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 foodMatrix 
\f0\b ):\
    
\f1\b0 foodImages 
\f0\b = []\
    
\f1\b0 color 
\f0\b = 
\f1\b0 FOOD_COLOR\
    
\f0\b \cf2 for 
\f1\b0 \cf0 xNum
\f0\b , 
\f1\b0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 foodMatrix
\f0\b ):\
      \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b \cf2 and \cf0 (
\f1\b0 xNum 
\f0\b * 
\f1\b0 \cf4 2
\f0\b \cf0 ) <= 
\f1\b0 foodMatrix
\f0\b .
\f1\b0 width
\f0\b : 
\f1\b0 color 
\f0\b = 
\f1\b0 TEAM_COLORS
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ]\
      \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b \cf2 and \cf0 (
\f1\b0 xNum 
\f0\b * 
\f1\b0 \cf4 2
\f0\b \cf0 ) > 
\f1\b0 foodMatrix
\f0\b .
\f1\b0 width
\f0\b : 
\f1\b0 color 
\f0\b = 
\f1\b0 TEAM_COLORS
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ]\
      
\f1\b0 imageRow 
\f0\b = []\
      
\f1\b0 foodImages
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 imageRow
\f0\b )\
      \cf2 for 
\f1\b0 \cf0 yNum
\f0\b , 
\f1\b0 cell 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 x
\f0\b ):\
        \cf2 if 
\f1\b0 \cf0 cell
\f0\b : 
\f2\i\b0 \cf3 # There's food here\
          
\f1\i0 \cf0 screen 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b ((
\f1\b0 xNum
\f0\b , 
\f1\b0 yNum 
\f0\b ))\
          
\f1\b0 dot 
\f0\b = 
\f1\b0 circle
\f0\b ( 
\f1\b0 screen
\f0\b , \
                        
\f1\b0 FOOD_SIZE 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , \
                        
\f1\b0 outlineColor 
\f0\b = 
\f1\b0 color
\f0\b , 
\f1\b0 fillColor 
\f0\b = 
\f1\b0 color
\f0\b ,\
                        
\f1\b0 width 
\f0\b = 
\f1\b0 \cf4 1
\f0\b \cf0 )\
          
\f1\b0 imageRow
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 dot
\f0\b )\
        \cf2 else\cf0 :\
          
\f1\b0 imageRow
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 \cf2 None
\f0\b \cf0 )\
    \cf2 return 
\f1\b0 \cf0 foodImages\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 drawCapsules
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 capsules 
\f0\b ):\
    
\f1\b0 capsuleImages 
\f0\b = \{\}\
    \cf2 for 
\f1\b0 \cf0 capsule 
\f0\b \cf2 in 
\f1\b0 \cf0 capsules
\f0\b :\
      ( 
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y 
\f0\b ) = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b (
\f1\b0 capsule
\f0\b )\
      
\f1\b0 dot 
\f0\b = 
\f1\b0 circle
\f0\b ( (
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y
\f0\b ), \
                        
\f1\b0 CAPSULE_SIZE 
\f0\b * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , \
                        
\f1\b0 outlineColor 
\f0\b = 
\f1\b0 CAPSULE_COLOR
\f0\b , \
                        
\f1\b0 fillColor 
\f0\b = 
\f1\b0 CAPSULE_COLOR
\f0\b , \
                        
\f1\b0 width 
\f0\b = 
\f1\b0 \cf4 1
\f0\b \cf0 )\
      
\f1\b0 capsuleImages
\f0\b [
\f1\b0 capsule
\f0\b ] = 
\f1\b0 dot\
    
\f0\b \cf2 return 
\f1\b0 \cf0 capsuleImages\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 removeFood
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 cell
\f0\b , 
\f1\b0 foodImages 
\f0\b ):\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 cell\
    remove_from_screen
\f0\b (
\f1\b0 foodImages
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ])\
    \
  \cf2 def 
\f1\b0 \cf0 removeCapsule
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 cell
\f0\b , 
\f1\b0 capsuleImages 
\f0\b ):\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 cell\
    remove_from_screen
\f0\b (
\f1\b0 capsuleImages
\f0\b [(
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b )])\
\
  \cf2 def 
\f1\b0 \cf0 drawExpandedCells
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 cells
\f0\b ):\
    
\f1\b0 \cf5 """\
    Draws an overlay of expanded grid positions for search agents\
    """\
    \cf0 n 
\f0\b = 
\f1\b0 float
\f0\b (
\f1\b0 len
\f0\b (
\f1\b0 cells
\f0\b ))\
    
\f1\b0 baseColor 
\f0\b = [
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 \cf4 0.0
\f0\b \cf0 , 
\f1\b0 \cf4 0.0
\f0\b \cf0 ]\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 clearExpandedCells
\f0\b ()\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 expandedCells 
\f0\b = []\
    \cf2 for 
\f1\b0 \cf0 k
\f0\b , 
\f1\b0 cell 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 cells
\f0\b ):\
       
\f1\b0 screenPos 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b ( 
\f1\b0 cell
\f0\b )\
       
\f1\b0 cellColor 
\f0\b = 
\f1\b0 formatColor
\f0\b (*[(
\f1\b0 n
\f0\b -
\f1\b0 k
\f0\b ) * 
\f1\b0 c 
\f0\b * .
\f1\b0 \cf4 5 
\f0\b \cf0 / 
\f1\b0 n 
\f0\b + .
\f1\b0 \cf4 25 
\f0\b \cf2 for 
\f1\b0 \cf0 c 
\f0\b \cf2 in 
\f1\b0 \cf0 baseColor
\f0\b ])\
       
\f1\b0 block 
\f0\b = 
\f1\b0 square
\f0\b (
\f1\b0 screenPos
\f0\b , \
                
\f1\b0 \cf4 0.5 
\f0\b \cf0 * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , \
                
\f1\b0 color 
\f0\b = 
\f1\b0 cellColor
\f0\b , \
                
\f1\b0 filled 
\f0\b = 
\f1\b0 \cf4 1
\f0\b \cf0 , 
\f1\b0 behind
\f0\b =\cf2 True\cf0 )\
       
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 expandedCells
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 block
\f0\b )\
  \
  \cf2 def 
\f1\b0 \cf0 clearExpandedCells
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 if 
\f1\b0 \cf4 'expandedCells' 
\f0\b \cf2 in 
\f1\b0 \cf0 dir
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ) \cf2 and 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 expandedCells
\f0\b ) > 
\f1\b0 \cf4 0
\f0\b \cf0 :\
      \cf2 for 
\f1\b0 \cf0 cell 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 expandedCells
\f0\b :\
        
\f1\b0 remove_from_screen
\f0\b (
\f1\b0 cell
\f0\b )\
\
\cf2 class 
\f1\b0 \cf0 FirstPersonPacmanGraphics
\f0\b (
\f1\b0 PacmanGraphics
\f0\b ):\
  \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 zoom 
\f0\b = 
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 showGhosts 
\f0\b = \cf2 True\cf0 , 
\f1\b0 capture 
\f0\b = \cf2 False\cf0 ):\
    
\f1\b0 PacmanGraphics
\f0\b .
\f1\b0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 zoom
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 showGhosts 
\f0\b = 
\f1\b0 showGhosts\
    \cf2 self
\f0\b \cf0 .
\f1\b0 capture 
\f0\b = 
\f1\b0 capture\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 initialize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b , 
\f1\b0 isBlue 
\f0\b = \cf2 False\cf0 ):\
    \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 isBlue 
\f0\b = 
\f1\b0 isBlue\
    PacmanGraphics
\f0\b .
\f1\b0 startGraphics
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b )\
    
\f2\i\b0 \cf3 # Initialize distribution images\
    
\f1\i0 \cf0 walls 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 layout
\f0\b .
\f1\b0 walls\
    dist 
\f0\b = []\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 layout 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 layout\
    \
    
\f0\b \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 walls
\f0\b .
\f1\b0 width
\f0\b ):\
      
\f1\b0 distx 
\f0\b = []\
      
\f1\b0 dist
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 distx
\f0\b )\
      \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 walls
\f0\b .
\f1\b0 height
\f0\b ):\
          ( 
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y 
\f0\b ) = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 to_screen
\f0\b ( (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ) )\
          
\f1\b0 block 
\f0\b = 
\f1\b0 square
\f0\b ( (
\f1\b0 screen_x
\f0\b , 
\f1\b0 screen_y
\f0\b ), \
                          
\f1\b0 \cf4 0.5 
\f0\b \cf0 * 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 gridSize
\f0\b , \
                          
\f1\b0 color 
\f0\b = 
\f1\b0 BACKGROUND_COLOR
\f0\b , \
                          
\f1\b0 filled 
\f0\b = 
\f1\b0 \cf4 1
\f0\b \cf0 )\
          
\f1\b0 distx
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 block
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 distributionImages 
\f0\b = 
\f1\b0 dist\
\
    
\f2\i \cf3 # Draw the rest\
    
\f1\i0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawStaticObjects
\f0\b (
\f1\b0 state
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawAgentObjects
\f0\b (
\f1\b0 state
\f0\b )\
    \
    
\f2\i\b0 \cf3 # Information\
    
\f1\i0 \cf2 self
\f0\b \cf0 .
\f1\b0 previousState 
\f0\b = 
\f1\b0 state\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 updateDistributions
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 distributions
\f0\b ):\
    \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 distributionImages
\f0\b )):\
      \cf2 for 
\f1\b0 \cf0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 distributionImages
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ])):\
        
\f1\b0 image 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 distributionImages
\f0\b [
\f1\b0 x
\f0\b ][
\f1\b0 y
\f0\b ]\
        
\f1\b0 weights 
\f0\b = [
\f1\b0 dist
\f0\b .
\f1\b0 getCount
\f0\b ( (
\f1\b0 x
\f0\b ,
\f1\b0 y
\f0\b ) ) \cf2 for 
\f1\b0 \cf0 dist 
\f0\b \cf2 in 
\f1\b0 \cf0 distributions
\f0\b ]\
        \
        \cf2 if 
\f1\b0 \cf0 sum
\f0\b (
\f1\b0 weights
\f0\b ) != 
\f1\b0 \cf4 0
\f0\b \cf0 :\
          \cf2 pass\
        
\f2\i\b0 \cf3 # Fog of war\
        
\f1\i0 \cf0 color 
\f0\b = [
\f1\b0 \cf4 0.0
\f0\b \cf0 ,
\f1\b0 \cf4 0.0
\f0\b \cf0 ,
\f1\b0 \cf4 0.0
\f0\b \cf0 ]\
        \cf2 for 
\f1\b0 \cf0 weight
\f0\b , 
\f1\b0 gcolor 
\f0\b \cf2 in 
\f1\b0 \cf0 zip
\f0\b (
\f1\b0 weights
\f0\b , 
\f1\b0 GHOST_VEC_COLORS
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 :]):\
          
\f1\b0 color 
\f0\b = [
\f1\b0 min
\f0\b (
\f1\b0 \cf4 1.0
\f0\b \cf0 , 
\f1\b0 c 
\f0\b + 
\f1\b0 \cf4 0.95 
\f0\b \cf0 * 
\f1\b0 g 
\f0\b * 
\f1\b0 weight 
\f0\b ** .
\f1\b0 \cf4 3
\f0\b \cf0 ) \cf2 for 
\f1\b0 \cf0 c
\f0\b ,
\f1\b0 g 
\f0\b \cf2 in 
\f1\b0 \cf0 zip
\f0\b (
\f1\b0 color
\f0\b , 
\f1\b0 gcolor
\f0\b )]\
        
\f1\b0 changeColor
\f0\b (
\f1\b0 image
\f0\b , 
\f1\b0 formatColor
\f0\b (*
\f1\b0 color
\f0\b ))\
    
\f1\b0 refresh\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 lookAhead
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 config
\f0\b , 
\f1\b0 state
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 config
\f0\b .
\f1\b0 getDirection
\f0\b () == 
\f1\b0 \cf4 'Stop'
\f0\b \cf0 :\
      \cf2 return\
    else\cf0 :\
      \cf2 pass\
      
\f2\i\b0 \cf3 # Draw relevant ghosts\
      
\f1\i0 \cf0 allGhosts 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getGhostStates
\f0\b ()\
      
\f1\b0 visibleGhosts 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getVisibleGhosts
\f0\b ()\
      \cf2 for 
\f1\b0 \cf0 i
\f0\b , 
\f1\b0 ghost 
\f0\b \cf2 in 
\f1\b0 \cf0 enumerate
\f0\b (
\f1\b0 allGhosts
\f0\b ):\
        \cf2 if 
\f1\b0 \cf0 ghost 
\f0\b \cf2 in 
\f1\b0 \cf0 visibleGhosts
\f0\b :\
          
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 drawGhost
\f0\b (
\f1\b0 ghost
\f0\b , 
\f1\b0 i
\f0\b )\
        \cf2 else\cf0 :\
          
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 currentGhostImages
\f0\b [
\f1\b0 i
\f0\b ] = 
\f1\b0 \cf2 None\
    \
  
\f0\b def 
\f1\b0 \cf0 getGhostColor
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghost
\f0\b , 
\f1\b0 ghostIndex
\f0\b ):\
    \cf2 return 
\f1\b0 \cf0 GHOST_COLORS
\f0\b [
\f1\b0 ghostIndex
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 getPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghostState
\f0\b ):\
    \cf2 if not 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 showGhosts 
\f0\b \cf2 and not 
\f1\b0 \cf0 ghostState
\f0\b .
\f1\b0 isPacman 
\f0\b \cf2 and 
\f1\b0 \cf0 ghostState
\f0\b .
\f1\b0 getPosition
\f0\b ()[
\f1\b0 \cf4 1
\f0\b \cf0 ] > 
\f1\b0 \cf4 1
\f0\b \cf0 :\
      \cf2 return \cf0 (-
\f1\b0 \cf4 1000
\f0\b \cf0 , -
\f1\b0 \cf4 1000
\f0\b \cf0 )\
    \cf2 else\cf0 :\
      \cf2 return 
\f1\b0 \cf0 PacmanGraphics
\f0\b .
\f1\b0 getPosition
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 ghostState
\f0\b )\
    \
\cf2 def 
\f1\b0 \cf0 add
\f0\b (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ):\
  \cf2 return \cf0 (
\f1\b0 x
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ] + 
\f1\b0 y
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ], 
\f1\b0 x
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] + 
\f1\b0 y
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ])}