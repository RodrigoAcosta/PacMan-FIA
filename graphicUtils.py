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
\f1\b0 \cf0 sys\

\f0\b \cf2 import 
\f1\b0 \cf0 math\

\f0\b \cf2 import 
\f1\b0 \cf0 random\

\f0\b \cf2 import 
\f1\b0 \cf0 string\

\f0\b \cf2 import 
\f1\b0 \cf0 time\

\f0\b \cf2 import 
\f1\b0 \cf0 types\

\f0\b \cf2 import 
\f1\b0 \cf0 Tkinter\
\
_Windows 
\f0\b = 
\f1\b0 sys
\f0\b .
\f1\b0 platform 
\f0\b == 
\f1\b0 \cf3 'win32'  
\f2\i \cf4 # True if on Win95/98/NT\
\

\f1\i0 \cf0 _root_window 
\f0\b = 
\f1\b0 \cf2 None      
\f2\i \cf4 # The root window for graphics output\

\f1\i0 \cf0 _canvas 
\f0\b = 
\f1\b0 \cf2 None      
\f2\i \cf4 # The canvas which holds graphics\

\f1\i0 \cf0 _canvas_xs 
\f0\b = 
\f1\b0 \cf2 None      
\f2\i \cf4 # Size of canvas object\

\f1\i0 \cf0 _canvas_ys 
\f0\b = 
\f1\b0 \cf2 None\
\cf0 _canvas_x 
\f0\b = 
\f1\b0 \cf2 None      
\f2\i \cf4 # Current position on canvas\

\f1\i0 \cf0 _canvas_y 
\f0\b = 
\f1\b0 \cf2 None\
\cf0 _canvas_col 
\f0\b = 
\f1\b0 \cf2 None      
\f2\i \cf4 # Current colour (set to black below)\

\f1\i0 \cf0 _canvas_tsize 
\f0\b = 
\f1\b0 \cf3 12\
\cf0 _canvas_tserifs 
\f0\b = 
\f1\b0 \cf3 0\
\

\f0\b \cf2 def 
\f1\b0 \cf0 formatColor
\f0\b (
\f1\b0 r
\f0\b , 
\f1\b0 g
\f0\b , 
\f1\b0 b
\f0\b ):\
  \cf2 return 
\f1\b0 \cf3 '#%02x%02x%02x' 
\f0\b \cf0 % (
\f1\b0 int
\f0\b (
\f1\b0 r 
\f0\b * 
\f1\b0 \cf3 255
\f0\b \cf0 ), 
\f1\b0 int
\f0\b (
\f1\b0 g 
\f0\b * 
\f1\b0 \cf3 255
\f0\b \cf0 ), 
\f1\b0 int
\f0\b (
\f1\b0 b 
\f0\b * 
\f1\b0 \cf3 255
\f0\b \cf0 ))\
\
\cf2 def 
\f1\b0 \cf0 colorToVector
\f0\b (
\f1\b0 color
\f0\b ):\
  \cf2 return 
\f1\b0 \cf0 map
\f0\b (\cf2 lambda 
\f1\b0 \cf0 x
\f0\b : 
\f1\b0 int
\f0\b (
\f1\b0 x
\f0\b , 
\f1\b0 \cf3 16
\f0\b \cf0 ) / 
\f1\b0 \cf3 256.0
\f0\b \cf0 , [
\f1\b0 color
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 :
\f1\b0 \cf3 3
\f0\b \cf0 ], 
\f1\b0 color
\f0\b [
\f1\b0 \cf3 3
\f0\b \cf0 :
\f1\b0 \cf3 5
\f0\b \cf0 ], 
\f1\b0 color
\f0\b [
\f1\b0 \cf3 5
\f0\b \cf0 :
\f1\b0 \cf3 7
\f0\b \cf0 ]])\
\
\cf2 if 
\f1\b0 \cf0 _Windows
\f0\b :\
    
\f1\b0 _canvas_tfonts 
\f0\b = [
\f1\b0 \cf3 'times new roman'
\f0\b \cf0 , 
\f1\b0 \cf3 'lucida console'
\f0\b \cf0 ]\
\cf2 else\cf0 :\
    
\f1\b0 _canvas_tfonts 
\f0\b = [
\f1\b0 \cf3 'times'
\f0\b \cf0 , 
\f1\b0 \cf3 'lucidasans-24'
\f0\b \cf0 ]\
    \cf2 pass 
\f2\i\b0 \cf4 # XXX need defaults here\
\

\f0\i0\b \cf2 def 
\f1\b0 \cf0 sleep
\f0\b (
\f1\b0 secs
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 _root_window 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 :\
        
\f1\b0 time
\f0\b .
\f1\b0 sleep
\f0\b (
\f1\b0 secs
\f0\b )\
    \cf2 else\cf0 :\
        
\f1\b0 _root_window
\f0\b .
\f1\b0 update_idletasks
\f0\b ()\
        
\f1\b0 _root_window
\f0\b .
\f1\b0 after
\f0\b (
\f1\b0 int
\f0\b (
\f1\b0 \cf3 1000 
\f0\b \cf0 * 
\f1\b0 secs
\f0\b ), 
\f1\b0 _root_window
\f0\b .
\f1\b0 quit
\f0\b )\
        
\f1\b0 _root_window
\f0\b .
\f1\b0 mainloop
\f0\b ()\
\
\cf2 def 
\f1\b0 \cf0 begin_graphics
\f0\b (
\f1\b0 width
\f0\b =
\f1\b0 \cf3 640
\f0\b \cf0 , 
\f1\b0 height
\f0\b =
\f1\b0 \cf3 480
\f0\b \cf0 , 
\f1\b0 color
\f0\b =
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 0
\f0\b \cf0 ), 
\f1\b0 title
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
\
    \cf2 global 
\f1\b0 \cf0 _root_window
\f0\b , 
\f1\b0 _canvas
\f0\b , 
\f1\b0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y
\f0\b , 
\f1\b0 _canvas_xs
\f0\b , 
\f1\b0 _canvas_ys\
\
    
\f2\i \cf4 # Check for duplicate call\
    
\f0\i0\b \cf2 if 
\f1\b0 \cf0 _root_window 
\f0\b \cf2 is not 
\f1\b0 None
\f0\b \cf0 :\
        
\f2\i\b0 \cf4 # Lose the window.\
        
\f1\i0 \cf0 _root_window
\f0\b .
\f1\b0 destroy
\f0\b ()\
        \
    
\f2\i\b0 \cf4 # Save the canvas size parameters\
    
\f1\i0 \cf0 _canvas_xs
\f0\b , 
\f1\b0 _canvas_ys 
\f0\b = 
\f1\b0 width 
\f0\b - 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 height 
\f0\b - 
\f1\b0 \cf3 1\
    \cf0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y 
\f0\b = 
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 _canvas_ys\
\
    
\f2\i \cf4 # Create the root window\
    
\f1\i0 \cf0 _root_window 
\f0\b = 
\f1\b0 Tkinter
\f0\b .
\f1\b0 Tk
\f0\b ()\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 protocol
\f0\b (
\f1\b0 \cf3 'WM_DELETE_WINDOW'
\f0\b \cf0 , 
\f1\b0 _destroy_window
\f0\b )\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 title
\f0\b (
\f1\b0 title 
\f0\b \cf2 or 
\f1\b0 \cf3 'Graphics Window'
\f0\b \cf0 )\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 resizable
\f0\b (
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 0
\f0\b \cf0 )\
\
    
\f2\i\b0 \cf4 # Create the canvas object\
    
\f0\i0\b \cf2 try\cf0 :\
      
\f1\b0 _canvas 
\f0\b = 
\f1\b0 Tkinter
\f0\b .
\f1\b0 Canvas
\f0\b (
\f1\b0 _root_window
\f0\b , 
\f1\b0 width
\f0\b =
\f1\b0 width
\f0\b , 
\f1\b0 height
\f0\b =
\f1\b0 height
\f0\b , 
\f1\b0 background
\f0\b =
\f1\b0 color
\f0\b )\
      
\f1\b0 _canvas
\f0\b .
\f1\b0 pack
\f0\b ()\
      
\f1\b0 _canvas
\f0\b .
\f1\b0 update
\f0\b ()\
    \cf2 except\cf0 :\
      
\f1\b0 _root_window 
\f0\b = 
\f1\b0 \cf2 None\
      
\f0\b raise\
\
    
\f2\i\b0 \cf4 # Bind to key-down and key-up events\
    
\f1\i0 \cf0 _root_window
\f0\b .
\f1\b0 bind
\f0\b (
\f1\b0 \cf3 "<KeyPress>"
\f0\b \cf0 , 
\f1\b0 _keypress
\f0\b )\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 bind
\f0\b (
\f1\b0 \cf3 "<KeyRelease>"
\f0\b \cf0 , 
\f1\b0 _keyrelease
\f0\b )\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 bind
\f0\b (
\f1\b0 \cf3 "<FocusIn>"
\f0\b \cf0 , 
\f1\b0 _clear_keys
\f0\b )\
    
\f1\b0 _root_window
\f0\b .
\f1\b0 bind
\f0\b (
\f1\b0 \cf3 "<FocusOut>"
\f0\b \cf0 , 
\f1\b0 _clear_keys
\f0\b )\
    
\f1\b0 _clear_keys
\f0\b ()\
\
\cf2 def 
\f1\b0 \cf0 _destroy_window
\f0\b (
\f1\b0 event
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    
\f1\b0 sys
\f0\b .
\f1\b0 exit
\f0\b (
\f1\b0 \cf3 0
\f0\b \cf0 )\

\f2\i\b0 \cf4 #    global _root_window\
#    _root_window.destroy()\
#    _root_window = None\
    #print "DESTROY"\
\

\f0\i0\b \cf2 def 
\f1\b0 \cf0 end_graphics
\f0\b ():\
    \cf2 global 
\f1\b0 \cf0 _root_window
\f0\b , 
\f1\b0 _canvas
\f0\b , 
\f1\b0 _mouse_enabled\
    
\f0\b \cf2 try\cf0 :\
      
\f1\b0 sleep
\f0\b (
\f1\b0 \cf3 1
\f0\b \cf0 )\
      
\f1\b0 _root_window
\f0\b .
\f1\b0 destroy
\f0\b ()\
    \cf2 finally\cf0 :\
      
\f1\b0 _root_window 
\f0\b = 
\f1\b0 \cf2 None\
      \cf0 _canvas 
\f0\b = 
\f1\b0 \cf2 None\
      \cf0 _mouse_enabled 
\f0\b = 
\f1\b0 \cf3 0\
      \cf0 _clear_keys
\f0\b ()\
\
\cf2 def 
\f1\b0 \cf0 clear_screen
\f0\b (
\f1\b0 background
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    \cf2 global 
\f1\b0 \cf0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y\
    _canvas
\f0\b .
\f1\b0 delete
\f0\b (
\f1\b0 \cf3 'all'
\f0\b \cf0 )\
    
\f1\b0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y 
\f0\b = 
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 _canvas_ys\
\

\f0\b \cf2 def 
\f1\b0 \cf0 polygon
\f0\b (
\f1\b0 coords
\f0\b , 
\f1\b0 outlineColor
\f0\b , 
\f1\b0 fillColor
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 , 
\f1\b0 filled
\f0\b =
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 smoothed
\f0\b =
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 behind
\f0\b =\cf2 False\cf0 , 
\f1\b0 width
\f0\b =
\f1\b0 \cf3 1
\f0\b \cf0 ):\
  
\f1\b0 c 
\f0\b = []\
  \cf2 for 
\f1\b0 \cf0 coord 
\f0\b \cf2 in 
\f1\b0 \cf0 coords
\f0\b :\
    
\f1\b0 c
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 coord
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ])\
    
\f1\b0 c
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 coord
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ])\
  \cf2 if 
\f1\b0 \cf0 fillColor 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 : 
\f1\b0 fillColor 
\f0\b = 
\f1\b0 outlineColor\
  poly 
\f0\b = 
\f1\b0 _canvas
\f0\b .
\f1\b0 create_polygon
\f0\b (
\f1\b0 c
\f0\b , 
\f1\b0 outline
\f0\b =
\f1\b0 outlineColor
\f0\b , 
\f1\b0 fill
\f0\b =
\f1\b0 fillColor
\f0\b , 
\f1\b0 smooth
\f0\b =
\f1\b0 smoothed
\f0\b , 
\f1\b0 width
\f0\b =
\f1\b0 width
\f0\b )\
  \cf2 if  
\f1\b0 \cf0 behind
\f0\b :    
\f1\b0 _canvas
\f0\b .
\f1\b0 tag_lower
\f0\b (
\f1\b0 poly
\f0\b , 
\f1\b0 \cf3 1
\f0\b \cf0 )\
  \cf2 return 
\f1\b0 \cf0 poly\
  \

\f0\b \cf2 def 
\f1\b0 \cf0 square
\f0\b (
\f1\b0 pos
\f0\b , 
\f1\b0 r
\f0\b , 
\f1\b0 color
\f0\b , 
\f1\b0 filled
\f0\b =
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 behind
\f0\b =\cf2 False\cf0 ):\
  
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 pos\
  coords 
\f0\b = [(
\f1\b0 x 
\f0\b - 
\f1\b0 r
\f0\b , 
\f1\b0 y 
\f0\b - 
\f1\b0 r
\f0\b ), (
\f1\b0 x 
\f0\b + 
\f1\b0 r
\f0\b , 
\f1\b0 y 
\f0\b - 
\f1\b0 r
\f0\b ), (
\f1\b0 x 
\f0\b + 
\f1\b0 r
\f0\b , 
\f1\b0 y 
\f0\b + 
\f1\b0 r
\f0\b ), (
\f1\b0 x 
\f0\b - 
\f1\b0 r
\f0\b , 
\f1\b0 y 
\f0\b + 
\f1\b0 r
\f0\b )]\
  \cf2 return 
\f1\b0 \cf0 polygon
\f0\b (
\f1\b0 coords
\f0\b , 
\f1\b0 color
\f0\b , 
\f1\b0 color
\f0\b , 
\f1\b0 filled
\f0\b , 
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 behind
\f0\b =
\f1\b0 behind
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 circle
\f0\b (
\f1\b0 pos
\f0\b , 
\f1\b0 r
\f0\b , 
\f1\b0 outlineColor
\f0\b , 
\f1\b0 fillColor
\f0\b , 
\f1\b0 endpoints
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 , 
\f1\b0 style
\f0\b =
\f1\b0 \cf3 'pieslice'
\f0\b \cf0 , 
\f1\b0 width
\f0\b =
\f1\b0 \cf3 2
\f0\b \cf0 ):\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 pos\
    x0
\f0\b , 
\f1\b0 x1 
\f0\b = 
\f1\b0 x 
\f0\b - 
\f1\b0 r 
\f0\b - 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 x 
\f0\b + 
\f1\b0 r\
    y0
\f0\b , 
\f1\b0 y1 
\f0\b = 
\f1\b0 y 
\f0\b - 
\f1\b0 r 
\f0\b - 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 y 
\f0\b + 
\f1\b0 r\
    
\f0\b \cf2 if 
\f1\b0 \cf0 endpoints 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      
\f1\b0 e 
\f0\b = [
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 359
\f0\b \cf0 ]\
    \cf2 else\cf0 :\
      
\f1\b0 e 
\f0\b = 
\f1\b0 list
\f0\b (
\f1\b0 endpoints
\f0\b )\
    \cf2 while 
\f1\b0 \cf0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ] > 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ]: 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] = 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] + 
\f1\b0 \cf3 360\
\
    
\f0\b \cf2 return 
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 create_arc
\f0\b (
\f1\b0 x0
\f0\b , 
\f1\b0 y0
\f0\b , 
\f1\b0 x1
\f0\b , 
\f1\b0 y1
\f0\b , 
\f1\b0 outline
\f0\b =
\f1\b0 outlineColor
\f0\b , 
\f1\b0 fill
\f0\b =
\f1\b0 fillColor
\f0\b ,\
                              
\f1\b0 extent
\f0\b =
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] - 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ], 
\f1\b0 start
\f0\b =
\f1\b0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ], 
\f1\b0 style
\f0\b =
\f1\b0 style
\f0\b , 
\f1\b0 width
\f0\b =
\f1\b0 width
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 image
\f0\b (
\f1\b0 pos
\f0\b , 
\f1\b0 file
\f0\b =
\f1\b0 \cf3 "../../blueghost.gif"
\f0\b \cf0 ):\
    
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 pos\
    
\f2\i \cf4 # img = PhotoImage(file=file)\
    
\f0\i0\b \cf2 return 
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 create_image
\f0\b (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b , 
\f1\b0 image 
\f0\b = 
\f1\b0 Tkinter
\f0\b .
\f1\b0 PhotoImage
\f0\b (
\f1\b0 file
\f0\b =
\f1\b0 file
\f0\b ), 
\f1\b0 anchor 
\f0\b = 
\f1\b0 Tkinter
\f0\b .
\f1\b0 NW
\f0\b )\
    \
    \
\cf2 def 
\f1\b0 \cf0 refresh
\f0\b ():\
      
\f1\b0 _canvas
\f0\b .
\f1\b0 update_idletasks
\f0\b ()\
                                                    \
\cf2 def 
\f1\b0 \cf0 moveCircle
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 pos
\f0\b , 
\f1\b0 r
\f0\b , 
\f1\b0 endpoints
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    \cf2 global 
\f1\b0 \cf0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y\
    \
    x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 pos\

\f2\i \cf4 #    x0, x1 = x - r, x + r + 1\
#    y0, y1 = y - r, y + r + 1\
    
\f1\i0 \cf0 x0
\f0\b , 
\f1\b0 x1 
\f0\b = 
\f1\b0 x 
\f0\b - 
\f1\b0 r 
\f0\b - 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 x 
\f0\b + 
\f1\b0 r\
    y0
\f0\b , 
\f1\b0 y1 
\f0\b = 
\f1\b0 y 
\f0\b - 
\f1\b0 r 
\f0\b - 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 y 
\f0\b + 
\f1\b0 r\
    
\f0\b \cf2 if 
\f1\b0 \cf0 endpoints 
\f0\b == 
\f1\b0 \cf2 None
\f0\b \cf0 :\
      
\f1\b0 e 
\f0\b = [
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 359
\f0\b \cf0 ]\
    \cf2 else\cf0 :\
      
\f1\b0 e 
\f0\b = 
\f1\b0 list
\f0\b (
\f1\b0 endpoints
\f0\b )\
    \cf2 while 
\f1\b0 \cf0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ] > 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ]: 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] = 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] + 
\f1\b0 \cf3 360\
\
    \cf0 edit
\f0\b (
\f1\b0 id
\f0\b , (
\f1\b0 \cf3 'start'
\f0\b \cf0 , 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ]), (
\f1\b0 \cf3 'extent'
\f0\b \cf0 , 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ] - 
\f1\b0 e
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ]))\
    
\f1\b0 move_to
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 x0
\f0\b , 
\f1\b0 y0
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 edit
\f0\b (
\f1\b0 id
\f0\b , *
\f1\b0 args
\f0\b ):\
    
\f1\b0 _canvas
\f0\b .
\f1\b0 itemconfigure
\f0\b (
\f1\b0 id
\f0\b , **
\f1\b0 dict
\f0\b (
\f1\b0 args
\f0\b ))\
    \
\cf2 def 
\f1\b0 \cf0 text
\f0\b (
\f1\b0 pos
\f0\b , 
\f1\b0 color
\f0\b , 
\f1\b0 contents
\f0\b , 
\f1\b0 font
\f0\b =
\f1\b0 \cf3 'Helvetica'
\f0\b \cf0 , 
\f1\b0 size
\f0\b =
\f1\b0 \cf3 12
\f0\b \cf0 , 
\f1\b0 style
\f0\b =
\f1\b0 \cf3 'normal'
\f0\b \cf0 ):\
    \cf2 global 
\f1\b0 \cf0 _canvas_x
\f0\b , 
\f1\b0 _canvas_y\
    x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 pos\
    font 
\f0\b = (
\f1\b0 font
\f0\b , 
\f1\b0 str
\f0\b (
\f1\b0 size
\f0\b ), 
\f1\b0 style
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 create_text
\f0\b (
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b , 
\f1\b0 anchor
\f0\b =
\f1\b0 \cf3 'nw'
\f0\b \cf0 , 
\f1\b0 fill
\f0\b =
\f1\b0 color
\f0\b , 
\f1\b0 text
\f0\b =
\f1\b0 contents
\f0\b , 
\f1\b0 font
\f0\b =
\f1\b0 font
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 changeText
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 newText
\f0\b , 
\f1\b0 font
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 , 
\f1\b0 size
\f0\b =
\f1\b0 \cf3 12
\f0\b \cf0 , 
\f1\b0 style
\f0\b =
\f1\b0 \cf3 'normal'
\f0\b \cf0 ):\
  
\f1\b0 _canvas
\f0\b .
\f1\b0 itemconfigure
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 text
\f0\b =
\f1\b0 newText
\f0\b )\
  \cf2 if 
\f1\b0 \cf0 font 
\f0\b != 
\f1\b0 \cf2 None
\f0\b \cf0 :\
    
\f1\b0 _canvas
\f0\b .
\f1\b0 itemconfigure
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 font
\f0\b =(
\f1\b0 font
\f0\b , 
\f1\b0 \cf3 '-%d' 
\f0\b \cf0 % 
\f1\b0 size
\f0\b , 
\f1\b0 style
\f0\b ))\
\
\cf2 def 
\f1\b0 \cf0 changeColor
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 newColor
\f0\b ):\
  
\f1\b0 _canvas
\f0\b .
\f1\b0 itemconfigure
\f0\b (
\f1\b0 id
\f0\b , 
\f1\b0 fill
\f0\b =
\f1\b0 newColor
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 line
\f0\b (
\f1\b0 here
\f0\b , 
\f1\b0 there
\f0\b , 
\f1\b0 color
\f0\b =
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 \cf3 0
\f0\b \cf0 ), 
\f1\b0 width
\f0\b =
\f1\b0 \cf3 2
\f0\b \cf0 ):\
  
\f1\b0 x0
\f0\b , 
\f1\b0 y0 
\f0\b = 
\f1\b0 here
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ], 
\f1\b0 here
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ]\
  
\f1\b0 x1
\f0\b , 
\f1\b0 y1 
\f0\b = 
\f1\b0 there
\f0\b [
\f1\b0 \cf3 0
\f0\b \cf0 ], 
\f1\b0 there
\f0\b [
\f1\b0 \cf3 1
\f0\b \cf0 ]\
  \cf2 return 
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 create_line
\f0\b (
\f1\b0 x0
\f0\b , 
\f1\b0 y0
\f0\b , 
\f1\b0 x1
\f0\b , 
\f1\b0 y1
\f0\b , 
\f1\b0 fill
\f0\b =
\f1\b0 color
\f0\b , 
\f1\b0 width
\f0\b =
\f1\b0 width
\f0\b )\
\

\f2\i\b0 \cf4 ##############################################################################\
### Keypress handling ########################################################\
##############################################################################\
\
# We bind to key-down and key-up events.\
\

\f1\i0 \cf0 _keysdown 
\f0\b = \{\}\

\f1\b0 _keyswaiting 
\f0\b = \{\}\

\f2\i\b0 \cf4 # This holds an unprocessed key release.  We delay key releases by up to\
# one call to keys_pressed() to get round a problem with auto repeat.\

\f1\i0 \cf0 _got_release 
\f0\b = 
\f1\b0 \cf2 None\
\

\f0\b def 
\f1\b0 \cf0 _keypress
\f0\b (
\f1\b0 event
\f0\b ):\
    \cf2 global 
\f1\b0 \cf0 _got_release\
    
\f2\i \cf4 #remap_arrows(event)\
    
\f1\i0 \cf0 _keysdown
\f0\b [
\f1\b0 event
\f0\b .
\f1\b0 keysym
\f0\b ] = 
\f1\b0 \cf3 1\
    \cf0 _keyswaiting
\f0\b [
\f1\b0 event
\f0\b .
\f1\b0 keysym
\f0\b ] = 
\f1\b0 \cf3 1\

\f2\i \cf4 #    print event.char, event.keycode\
    
\f1\i0 \cf0 _got_release 
\f0\b = 
\f1\b0 \cf2 None\
\

\f0\b def 
\f1\b0 \cf0 _keyrelease
\f0\b (
\f1\b0 event
\f0\b ):\
    \cf2 global 
\f1\b0 \cf0 _got_release\
    
\f2\i \cf4 #remap_arrows(event)\
    
\f0\i0\b \cf2 try\cf0 :\
      \cf2 del 
\f1\b0 \cf0 _keysdown
\f0\b [
\f1\b0 event
\f0\b .
\f1\b0 keysym
\f0\b ]\
    \cf2 except\cf0 :\
      \cf2 pass\
    
\f1\b0 \cf0 _got_release 
\f0\b = 
\f1\b0 \cf3 1\
    \

\f0\b \cf2 def 
\f1\b0 \cf0 remap_arrows
\f0\b (
\f1\b0 event
\f0\b ):\
    
\f2\i\b0 \cf4 # TURN ARROW PRESSES INTO LETTERS (SHOULD BE IN KEYBOARD AGENT)\
    
\f0\i0\b \cf2 if 
\f1\b0 \cf0 event
\f0\b .
\f1\b0 char 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf3 'a'
\f0\b \cf0 , 
\f1\b0 \cf3 's'
\f0\b \cf0 , 
\f1\b0 \cf3 'd'
\f0\b \cf0 , 
\f1\b0 \cf3 'w'
\f0\b \cf0 ]:\
      \cf2 return\
    if 
\f1\b0 \cf0 event
\f0\b .
\f1\b0 keycode 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf3 37
\f0\b \cf0 , 
\f1\b0 \cf3 101
\f0\b \cf0 ]: 
\f2\i\b0 \cf4 # LEFT ARROW (win / x)\
      
\f1\i0 \cf0 event
\f0\b .
\f1\b0 char 
\f0\b = 
\f1\b0 \cf3 'a'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 event
\f0\b .
\f1\b0 keycode 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf3 38
\f0\b \cf0 , 
\f1\b0 \cf3 99
\f0\b \cf0 ]: 
\f2\i\b0 \cf4 # UP ARROW\
      
\f1\i0 \cf0 event
\f0\b .
\f1\b0 char 
\f0\b = 
\f1\b0 \cf3 'w'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 event
\f0\b .
\f1\b0 keycode 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf3 39
\f0\b \cf0 , 
\f1\b0 \cf3 102
\f0\b \cf0 ]: 
\f2\i\b0 \cf4 # RIGHT ARROW\
      
\f1\i0 \cf0 event
\f0\b .
\f1\b0 char 
\f0\b = 
\f1\b0 \cf3 'd'\
    
\f0\b \cf2 if 
\f1\b0 \cf0 event
\f0\b .
\f1\b0 keycode 
\f0\b \cf2 in \cf0 [
\f1\b0 \cf3 40
\f0\b \cf0 , 
\f1\b0 \cf3 104
\f0\b \cf0 ]: 
\f2\i\b0 \cf4 # DOWN ARROW\
      
\f1\i0 \cf0 event
\f0\b .
\f1\b0 char 
\f0\b = 
\f1\b0 \cf3 's'\
\

\f0\b \cf2 def 
\f1\b0 \cf0 _clear_keys
\f0\b (
\f1\b0 event
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ):\
    \cf2 global 
\f1\b0 \cf0 _keysdown
\f0\b , 
\f1\b0 _got_release
\f0\b , 
\f1\b0 _keyswaiting\
    _keysdown 
\f0\b = \{\}\
    
\f1\b0 _keyswaiting 
\f0\b = \{\}\
    
\f1\b0 _got_release 
\f0\b = 
\f1\b0 \cf2 None\
\

\f0\b def 
\f1\b0 \cf0 keys_pressed
\f0\b (
\f1\b0 d_o_e
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 dooneevent
\f0\b ,\
                 
\f1\b0 d_w
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 DONT_WAIT
\f0\b ):\
    
\f1\b0 d_o_e
\f0\b (
\f1\b0 d_w
\f0\b )\
    \cf2 if 
\f1\b0 \cf0 _got_release
\f0\b :\
      
\f1\b0 d_o_e
\f0\b (
\f1\b0 d_w
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 _keysdown
\f0\b .
\f1\b0 keys
\f0\b ()\
  \
\cf2 def 
\f1\b0 \cf0 keys_waiting
\f0\b ():\
  \cf2 global 
\f1\b0 \cf0 _keyswaiting\
  keys 
\f0\b = 
\f1\b0 _keyswaiting
\f0\b .
\f1\b0 keys
\f0\b ()\
  
\f1\b0 _keyswaiting 
\f0\b = \{\}\
  \cf2 return 
\f1\b0 \cf0 keys\
\

\f2\i \cf4 # Block for a list of keys...\
\

\f0\i0\b \cf2 def 
\f1\b0 \cf0 wait_for_keys
\f0\b ():\
    
\f1\b0 keys 
\f0\b = []\
    \cf2 while 
\f1\b0 \cf0 keys 
\f0\b == []:\
        
\f1\b0 keys 
\f0\b = 
\f1\b0 keys_pressed
\f0\b ()\
    
\f1\b0 thekeys 
\f0\b = 
\f1\b0 keys\
    
\f0\b \cf2 while 
\f1\b0 \cf0 keys 
\f0\b != []:\
        
\f1\b0 keys 
\f0\b = 
\f1\b0 keys_pressed
\f0\b ()\
    \cf2 return 
\f1\b0 \cf0 thekeys\
\
\

\f0\b \cf2 def 
\f1\b0 \cf0 remove_from_screen
\f0\b (
\f1\b0 x
\f0\b ,\
                       
\f1\b0 d_o_e
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 dooneevent
\f0\b ,\
                       
\f1\b0 d_w
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 DONT_WAIT
\f0\b ):\
    
\f1\b0 _canvas
\f0\b .
\f1\b0 delete
\f0\b (
\f1\b0 x
\f0\b )\
    
\f1\b0 d_o_e
\f0\b (
\f1\b0 d_w
\f0\b )\
\
\cf2 def 
\f1\b0 \cf0 _adjust_coords
\f0\b (
\f1\b0 coord_list
\f0\b , 
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b ):\
    \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 \cf3 0
\f0\b \cf0 , 
\f1\b0 len
\f0\b (
\f1\b0 coord_list
\f0\b ), 
\f1\b0 \cf3 2
\f0\b \cf0 ):\
        
\f1\b0 coord_list
\f0\b [
\f1\b0 i
\f0\b ] = 
\f1\b0 coord_list
\f0\b [
\f1\b0 i
\f0\b ] + 
\f1\b0 x\
        coord_list
\f0\b [
\f1\b0 i 
\f0\b + 
\f1\b0 \cf3 1
\f0\b \cf0 ] = 
\f1\b0 coord_list
\f0\b [
\f1\b0 i 
\f0\b + 
\f1\b0 \cf3 1
\f0\b \cf0 ] + 
\f1\b0 y\
    
\f0\b \cf2 return 
\f1\b0 \cf0 coord_list\
\

\f0\b \cf2 def 
\f1\b0 \cf0 move_to
\f0\b (
\f1\b0 object
\f0\b , 
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ,\
            
\f1\b0 d_o_e
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 dooneevent
\f0\b ,\
            
\f1\b0 d_w
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 DONT_WAIT
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 y 
\f0\b \cf2 is 
\f1\b0 None
\f0\b \cf0 :\
        \cf2 try\cf0 : 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 x\
        
\f0\b \cf2 except\cf0 : \cf2 raise  
\f1\b0 \cf3 'incomprehensible coordinates' \
        \
    \cf0 horiz 
\f0\b = \cf2 True\
    
\f1\b0 \cf0 newCoords 
\f0\b = []\
    
\f1\b0 current_x
\f0\b , 
\f1\b0 current_y 
\f0\b = 
\f1\b0 _canvas
\f0\b .
\f1\b0 coords
\f0\b (
\f1\b0 object
\f0\b )[
\f1\b0 \cf3 0
\f0\b \cf0 :
\f1\b0 \cf3 2
\f0\b \cf0 ] 
\f2\i\b0 \cf4 # first point\
    
\f0\i0\b \cf2 for 
\f1\b0 \cf0 coord 
\f0\b \cf2 in  
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 coords
\f0\b (
\f1\b0 object
\f0\b ):\
      \cf2 if 
\f1\b0 \cf0 horiz
\f0\b :  \
        
\f1\b0 inc 
\f0\b = 
\f1\b0 x 
\f0\b - 
\f1\b0 current_x\
      
\f0\b \cf2 else\cf0 :      \
        
\f1\b0 inc 
\f0\b = 
\f1\b0 y 
\f0\b - 
\f1\b0 current_y\
      horiz 
\f0\b = \cf2 not 
\f1\b0 \cf0 horiz\
      \
      newCoords
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 coord 
\f0\b + 
\f1\b0 inc
\f0\b )\
    \
    
\f1\b0 _canvas
\f0\b .
\f1\b0 coords
\f0\b (
\f1\b0 object
\f0\b , *
\f1\b0 newCoords
\f0\b )\
    
\f1\b0 d_o_e
\f0\b (
\f1\b0 d_w
\f0\b )\
    \
\cf2 def 
\f1\b0 \cf0 move_by
\f0\b (
\f1\b0 object
\f0\b , 
\f1\b0 x
\f0\b , 
\f1\b0 y
\f0\b =
\f1\b0 \cf2 None
\f0\b \cf0 ,\
            
\f1\b0 d_o_e
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 dooneevent
\f0\b ,\
            
\f1\b0 d_w
\f0\b =
\f1\b0 Tkinter
\f0\b .
\f1\b0 tkinter
\f0\b .
\f1\b0 DONT_WAIT
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 y 
\f0\b \cf2 is 
\f1\b0 None
\f0\b \cf0 :\
        \cf2 try\cf0 : 
\f1\b0 x
\f0\b , 
\f1\b0 y 
\f0\b = 
\f1\b0 x\
        
\f0\b \cf2 except\cf0 : \cf2 raise 
\f1\b0 \cf0 Exception
\f0\b , 
\f1\b0 \cf3 'incomprehensible coordinates' \
    \
    \cf0 horiz 
\f0\b = \cf2 True\
    
\f1\b0 \cf0 newCoords 
\f0\b = []\
    \cf2 for 
\f1\b0 \cf0 coord 
\f0\b \cf2 in  
\f1\b0 \cf0 _canvas
\f0\b .
\f1\b0 coords
\f0\b (
\f1\b0 object
\f0\b ):\
      \cf2 if 
\f1\b0 \cf0 horiz
\f0\b :  \
        
\f1\b0 inc 
\f0\b = 
\f1\b0 x\
      
\f0\b \cf2 else\cf0 :      \
        
\f1\b0 inc 
\f0\b = 
\f1\b0 y\
      horiz 
\f0\b = \cf2 not 
\f1\b0 \cf0 horiz\
      \
      newCoords
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 coord 
\f0\b + 
\f1\b0 inc
\f0\b )\
      \
    
\f1\b0 _canvas
\f0\b .
\f1\b0 coords
\f0\b (
\f1\b0 object
\f0\b , *
\f1\b0 newCoords
\f0\b )\
    
\f1\b0 d_o_e
\f0\b (
\f1\b0 d_w
\f0\b )\
    \

\f1\b0 ghost_shape 
\f0\b = [                \
    (
\f1\b0 \cf3 0
\f0\b \cf0 , - 
\f1\b0 \cf3 0.5
\f0\b \cf0 ),\
    (
\f1\b0 \cf3 0.25
\f0\b \cf0 , - 
\f1\b0 \cf3 0.75
\f0\b \cf0 ),\
    (
\f1\b0 \cf3 0.5
\f0\b \cf0 , - 
\f1\b0 \cf3 0.5
\f0\b \cf0 ),\
    (
\f1\b0 \cf3 0.75
\f0\b \cf0 , - 
\f1\b0 \cf3 0.75
\f0\b \cf0 ),\
    (
\f1\b0 \cf3 0.75
\f0\b \cf0 , 
\f1\b0 \cf3 0.5
\f0\b \cf0 ),\
    (
\f1\b0 \cf3 0.5
\f0\b \cf0 , 
\f1\b0 \cf3 0.75
\f0\b \cf0 ),\
    (- 
\f1\b0 \cf3 0.5
\f0\b \cf0 , 
\f1\b0 \cf3 0.75
\f0\b \cf0 ),\
    (- 
\f1\b0 \cf3 0.75
\f0\b \cf0 , 
\f1\b0 \cf3 0.5
\f0\b \cf0 ),\
    (- 
\f1\b0 \cf3 0.75
\f0\b \cf0 , - 
\f1\b0 \cf3 0.75
\f0\b \cf0 ),\
    (- 
\f1\b0 \cf3 0.5
\f0\b \cf0 , - 
\f1\b0 \cf3 0.5
\f0\b \cf0 ),\
    (- 
\f1\b0 \cf3 0.25
\f0\b \cf0 , - 
\f1\b0 \cf3 0.75
\f0\b \cf0 )\
  ]\
\
\cf2 if 
\f1\b0 \cf0 __name__ 
\f0\b == 
\f1\b0 \cf3 '__main__'
\f0\b \cf0 :\
  
\f1\b0 begin_graphics
\f0\b ()\
  
\f1\b0 clear_screen
\f0\b ()\
  
\f1\b0 ghost_shape 
\f0\b = [(
\f1\b0 x 
\f0\b * 
\f1\b0 \cf3 10 
\f0\b \cf0 + 
\f1\b0 \cf3 20
\f0\b \cf0 , 
\f1\b0 y 
\f0\b * 
\f1\b0 \cf3 10 
\f0\b \cf0 + 
\f1\b0 \cf3 20
\f0\b \cf0 ) \cf2 for 
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y 
\f0\b \cf2 in 
\f1\b0 \cf0 ghost_shape
\f0\b ]\
  
\f1\b0 g 
\f0\b = 
\f1\b0 polygon
\f0\b (
\f1\b0 ghost_shape
\f0\b , 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 \cf3 1
\f0\b \cf0 , 
\f1\b0 \cf3 1
\f0\b \cf0 ))\
  
\f1\b0 move_to
\f0\b (
\f1\b0 g
\f0\b , (
\f1\b0 \cf3 50
\f0\b \cf0 , 
\f1\b0 \cf3 50
\f0\b \cf0 ))\
  
\f1\b0 circle
\f0\b ((
\f1\b0 \cf3 150
\f0\b \cf0 , 
\f1\b0 \cf3 150
\f0\b \cf0 ), 
\f1\b0 \cf3 20
\f0\b \cf0 , 
\f1\b0 formatColor
\f0\b (
\f1\b0 \cf3 0.7
\f0\b \cf0 , 
\f1\b0 \cf3 0.3
\f0\b \cf0 , 
\f1\b0 \cf3 0.0
\f0\b \cf0 ), 
\f1\b0 endpoints
\f0\b =[
\f1\b0 \cf3 15
\f0\b \cf0 , - 
\f1\b0 \cf3 15
\f0\b \cf0 ])\
  
\f1\b0 sleep
\f0\b (
\f1\b0 \cf3 2
\f0\b \cf0 )}