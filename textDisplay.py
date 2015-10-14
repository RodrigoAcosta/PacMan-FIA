{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Oblique;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red251\green0\blue7;\red15\green112\blue1;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
import 
\f1\b0 \cf0 pacman
\f0\b , 
\f1\b0 time\
\
DRAW_EVERY 
\f0\b = 
\f1\b0 \cf3 1\
\cf0 SLEEP_TIME 
\f0\b = 
\f1\b0 \cf3 0 
\f2\i \cf4 # This can be overwritten by __init__\

\f1\i0 \cf0 DISPLAY_MOVES 
\f0\b = \cf2 False\

\f1\b0 \cf0 QUIET 
\f0\b = \cf2 False 
\f2\i\b0 \cf4 # Supresses output\
\

\f0\i0\b \cf2 class 
\f1\b0 \cf0 NullGraphics
\f0\b :\
  \cf2 def 
\f1\b0 \cf0 initialize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b , 
\f1\b0 isBlue 
\f0\b = \cf2 False\cf0 ):\
    \cf2 pass\
  \
  def 
\f1\b0 \cf0 update
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    \cf2 pass\
  \
  def 
\f1\b0 \cf0 pause
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 time
\f0\b .
\f1\b0 sleep
\f0\b (
\f1\b0 SLEEP_TIME
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 draw
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    \cf2 print 
\f1\b0 \cf0 state\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 finish
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass\
\
class 
\f1\b0 \cf0 NoGraphics
\f0\b :\
  \cf2 def 
\f1\b0 \cf0 initialize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b , 
\f1\b0 isBlue 
\f0\b = \cf2 False\cf0 ):\
    \cf2 pass\
  \
  def 
\f1\b0 \cf0 update
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    \cf2 pass\
  \
  def 
\f1\b0 \cf0 pause
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 time
\f0\b .
\f1\b0 sleep
\f0\b (
\f1\b0 SLEEP_TIME
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 draw
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    
\f1\b0 die\
    
\f0\b \cf2 pass\
  \
  def 
\f1\b0 \cf0 finish
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
\f1\b0 speed
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    \cf2 if 
\f1\b0 \cf0 speed 
\f0\b != 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      \cf2 global 
\f1\b0 \cf0 SLEEP_TIME\
      SLEEP_TIME 
\f0\b = 
\f1\b0 speed\
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
\f1\b0 draw
\f0\b (
\f1\b0 state
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pause
\f0\b ()\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 turn 
\f0\b = 
\f1\b0 \cf3 0\
    \cf2 self
\f0\b \cf0 .
\f1\b0 agentCounter 
\f0\b = 
\f1\b0 \cf3 0\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 update
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    
\f1\b0 numAgents 
\f0\b = 
\f1\b0 len
\f0\b (
\f1\b0 state
\f0\b .
\f1\b0 agentStates
\f0\b )\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentCounter 
\f0\b = (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 agentCounter 
\f0\b + 
\f1\b0 \cf3 1
\f0\b \cf0 ) % 
\f1\b0 numAgents\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 agentCounter 
\f0\b == 
\f1\b0 \cf3 0
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 turn 
\f0\b += 
\f1\b0 \cf3 1\
      
\f0\b \cf2 if 
\f1\b0 \cf0 DISPLAY_MOVES
\f0\b :\
        
\f1\b0 ghosts 
\f0\b = [
\f1\b0 pacman
\f0\b .
\f1\b0 nearestPoint
\f0\b (
\f1\b0 state
\f0\b .
\f1\b0 getGhostPosition
\f0\b (
\f1\b0 i
\f0\b )) \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 numAgents
\f0\b )]\
        \cf2 print 
\f1\b0 \cf3 "%4d) P: %-8s" 
\f0\b \cf0 % (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 turn
\f0\b , 
\f1\b0 str
\f0\b (
\f1\b0 pacman
\f0\b .
\f1\b0 nearestPoint
\f0\b (
\f1\b0 state
\f0\b .
\f1\b0 getPacmanPosition
\f0\b ()))),
\f1\b0 \cf3 '| Score: %-5d' 
\f0\b \cf0 % 
\f1\b0 state
\f0\b .
\f1\b0 score
\f0\b ,
\f1\b0 \cf3 '| Ghosts:'
\f0\b \cf0 , 
\f1\b0 ghosts\
      
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 turn 
\f0\b % 
\f1\b0 DRAW_EVERY 
\f0\b == 
\f1\b0 \cf3 0
\f0\b \cf0 :\
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 draw
\f0\b (
\f1\b0 state
\f0\b )\
        
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 pause
\f0\b ()\
    \cf2 if 
\f1\b0 \cf0 state
\f0\b .
\f1\b0 _win 
\f0\b \cf2 or 
\f1\b0 \cf0 state
\f0\b .
\f1\b0 _lose
\f0\b :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 draw
\f0\b (
\f1\b0 state
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 pause
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 time
\f0\b .
\f1\b0 sleep
\f0\b (
\f1\b0 SLEEP_TIME
\f0\b )\
    \
  \cf2 def 
\f1\b0 \cf0 draw
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 state
\f0\b ):\
    \cf2 print 
\f1\b0 \cf0 state\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 finish
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 pass}