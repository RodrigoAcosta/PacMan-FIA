{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red118\green0\blue2;\red15\green112\blue1;
\red251\green0\blue7;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Agent\

\f0\b \cf2 from 
\f1\b0 \cf0 game 
\f0\b \cf2 import 
\f1\b0 \cf0 Directions\

\f0\b \cf2 import 
\f1\b0 \cf0 random\
\

\f0\b \cf2 class 
\f1\b0 \cf0 KeyboardAgent
\f0\b (
\f1\b0 Agent
\f0\b ):\
  
\f1\b0 \cf3 """\
  An agent controlled by the keyboard.\
  """\
  
\f2\i \cf4 # NOTE: Arrow keys also work.\
  
\f1\i0 \cf0 WEST_KEY  
\f0\b = 
\f1\b0 \cf5 'a' \
  \cf0 EAST_KEY  
\f0\b = 
\f1\b0 \cf5 'd' \
  \cf0 NORTH_KEY 
\f0\b = 
\f1\b0 \cf5 'w' \
  \cf0 SOUTH_KEY 
\f0\b = 
\f1\b0 \cf5 's'\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 index 
\f0\b = 
\f1\b0 \cf5 0 
\f0\b \cf0 ):\
    \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 lastMove 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP\
    \cf2 self
\f0\b \cf0 .
\f1\b0 index 
\f0\b = 
\f1\b0 index\
    \cf2 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b = []\
    \
  \cf2 def 
\f1\b0 \cf0 getAction
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    \cf2 from 
\f1\b0 \cf0 graphicsUtils 
\f0\b \cf2 import 
\f1\b0 \cf0 keys_waiting\
    
\f0\b \cf2 from 
\f1\b0 \cf0 graphicsUtils 
\f0\b \cf2 import 
\f1\b0 \cf0 keys_pressed\
    keys 
\f0\b = 
\f1\b0 keys_waiting
\f0\b () + 
\f1\b0 keys_pressed
\f0\b ()\
    \cf2 if 
\f1\b0 \cf0 keys 
\f0\b != []:\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b = 
\f1\b0 keys\
    \
    legal 
\f0\b = 
\f1\b0 state
\f0\b .
\f1\b0 getLegalActions
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 index
\f0\b )\
    
\f1\b0 move 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 getMove
\f0\b (
\f1\b0 legal
\f0\b )\
    \
    \cf2 if 
\f1\b0 \cf0 move 
\f0\b == 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP
\f0\b :\
      
\f2\i\b0 \cf4 # Try to move in the same direction as before\
      
\f0\i0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 lastMove 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b :\
        
\f1\b0 move 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 lastMove\
        \
    
\f0\b \cf2 if 
\f1\b0 \cf0 move 
\f0\b \cf2 not in 
\f1\b0 \cf0 legal
\f0\b :\
      
\f1\b0 move 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 choice
\f0\b (
\f1\b0 legal
\f0\b )\
      \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 lastMove 
\f0\b = 
\f1\b0 move\
    
\f0\b \cf2 return 
\f1\b0 \cf0 move\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 getMove
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 legal
\f0\b ):\
    
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 WEST_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b \cf2 or 
\f1\b0 \cf5 'Left' 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 WEST 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b :  
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 EAST_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b \cf2 or 
\f1\b0 \cf5 'Right' 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 EAST 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b : 
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 NORTH_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b \cf2 or 
\f1\b0 \cf5 'Up' 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 NORTH 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b :   
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 SOUTH_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys 
\f0\b \cf2 or 
\f1\b0 \cf5 'Down' 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 SOUTH 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b : 
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH\
    
\f0\b \cf2 return 
\f1\b0 \cf0 move\
  \

\f0\b \cf2 class 
\f1\b0 \cf0 KeyboardAgent2
\f0\b (
\f1\b0 KeyboardAgent
\f0\b ):\
  
\f1\b0 \cf3 """\
  A second agent controlled by the keyboard.\
  """\
  
\f2\i \cf4 # NOTE: Arrow keys also work.\
  
\f1\i0 \cf0 WEST_KEY  
\f0\b = 
\f1\b0 \cf5 'j' \
  \cf0 EAST_KEY  
\f0\b = 
\f1\b0 \cf5 "l" \
  \cf0 NORTH_KEY 
\f0\b = 
\f1\b0 \cf5 'i' \
  \cf0 SOUTH_KEY 
\f0\b = 
\f1\b0 \cf5 'k'\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getMove
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 legal
\f0\b ):\
    
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 STOP\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 WEST_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 WEST 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b :  
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 WEST\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 EAST_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 EAST 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b : 
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 EAST\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 NORTH_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 NORTH 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b :   
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 NORTH\
    
\f0\b \cf2 if   \cf0 (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 SOUTH_KEY 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ) \cf2 and 
\f1\b0 \cf0 Directions
\f0\b .
\f1\b0 SOUTH 
\f0\b \cf2 in 
\f1\b0 \cf0 legal
\f0\b : 
\f1\b0 move 
\f0\b = 
\f1\b0 Directions
\f0\b .
\f1\b0 SOUTH\
    
\f0\b \cf2 return 
\f1\b0 \cf0 move}