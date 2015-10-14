{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red118\green0\blue2;\red251\green0\blue7;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
import 
\f1\b0 \cf0 sys\

\f0\b \cf2 import 
\f1\b0 \cf0 inspect\

\f0\b \cf2 import 
\f1\b0 \cf0 heapq
\f0\b , 
\f1\b0 random\
\
\
\pard\pardeftab720\partightenfactor0
\cf3 """\
 Utility classes\
 \
 Data structures useful for implementing SearchAgents \
"""\
\
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 class 
\f1\b0 \cf0 Stack
\f0\b :\
  
\f1\b0 \cf3 """\
   Data structure that implements a last-in-first-out (LIFO)\
  queue policy. \
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 list 
\f0\b = []\
    \
  \cf2 def 
\f1\b0 \cf0 push
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ,
\f1\b0 item
\f0\b ):\
    
\f1\b0 \cf3 """\
        Push 'item' onto the stack\
    """\
    \cf2 self
\f0\b \cf0 .
\f1\b0 list
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 item
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 pop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
       Pop the most recently pushed item from\
       the stack\
    """\
    
\f0\b \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 list
\f0\b .
\f1\b0 pop
\f0\b ()\
\
  \cf2 def 
\f1\b0 \cf0 isEmpty
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
        Returns true if the stack is empty\
    """\
    
\f0\b \cf2 return 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 list
\f0\b ) == 
\f1\b0 \cf4 0\
\

\f0\b \cf2 class 
\f1\b0 \cf0 Queue
\f0\b :\
  
\f1\b0 \cf3 """\
    Data structure that implements a first-in-first-out (FIFO)\
  queue policy. \
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 list 
\f0\b = []\
  \
  \cf2 def 
\f1\b0 \cf0 push
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ,
\f1\b0 item
\f0\b ):\
    
\f1\b0 \cf3 """\
      Enqueue the 'item' into the queue\
    """\
    \cf2 self
\f0\b \cf0 .
\f1\b0 list
\f0\b .
\f1\b0 insert
\f0\b (
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 item
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 pop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
      Dequeue the earliest enqueued item still in the queue. This\
      operation removes the item from the queue.\
    """\
    
\f0\b \cf2 return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 list
\f0\b .
\f1\b0 pop
\f0\b ()\
\
  \cf2 def 
\f1\b0 \cf0 isEmpty
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
        Returns true if the queue is empty.\
    """\
    
\f0\b \cf2 return 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 list
\f0\b ) == 
\f1\b0 \cf4 0\
  \

\f0\b \cf2 class 
\f1\b0 \cf0 PriorityQueue
\f0\b :\
  
\f1\b0 \cf3 """\
    Implements a priority queue data structure. Each inserted item\
    has a priority associated with it and the client is usually interested\
    in quick retrieval of the lowest-priority item in the queue. This\
    data structure allows O(1) access to the lowest-priority item.\
  """\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
      heap: A binomial heap storing [priority,item]\
      lists. \
      \
      dict: Dictionary storing item -> [priorirty,item]\
      maps so we can reach into heap for a given \
      item and update the priorirty and heapify\
    """\
    \cf2 self
\f0\b \cf0 .
\f1\b0 heap 
\f0\b = []\
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 dict 
\f0\b = \{\}\
      \
  \cf2 def 
\f1\b0 \cf0 push
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ,
\f1\b0 item
\f0\b ,
\f1\b0 priority
\f0\b ):\
    
\f1\b0 \cf3 """\
        Sets the priority of the 'item' to\
    priority. If the 'item' is already\
    in the queue, then its key is changed\
    to the new priority, regardless if it\
    is higher or lower than the current \
    priority.\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 item 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b [
\f1\b0 item
\f0\b ][
\f1\b0 \cf4 0
\f0\b \cf0 ] = 
\f1\b0 priority\
      heapq
\f0\b .
\f1\b0 heapify
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b )\
    \cf2 else\cf0 :\
      
\f1\b0 pair 
\f0\b = [
\f1\b0 priority
\f0\b ,
\f1\b0 item
\f0\b ]\
      
\f1\b0 heapq
\f0\b .
\f1\b0 heappush
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b ,
\f1\b0 pair
\f0\b )\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b [
\f1\b0 item
\f0\b ] = 
\f1\b0 pair\
      \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getPriority
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ,
\f1\b0 item
\f0\b ):\
    
\f1\b0 \cf3 """\
        Get priority of 'item'. If \
    'item' is not in the queue returns None\
    """\
    
\f0\b \cf2 if not 
\f1\b0 \cf0 item 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b :\
      \cf2 return 
\f1\b0 None\
    
\f0\b return 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b [
\f1\b0 item
\f0\b ][
\f1\b0 \cf4 0
\f0\b \cf0 ]\
      \
  \cf2 def 
\f1\b0 \cf0 pop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
      Returns lowest-priority item in priority queue, or\
      None if the queue is empty\
    """\
    
\f0\b \cf2 if 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 isEmpty
\f0\b (): \cf2 return 
\f1\b0 None\
    
\f0\b \cf0 (
\f1\b0 priority
\f0\b ,
\f1\b0 item
\f0\b ) = 
\f1\b0 heapq
\f0\b .
\f1\b0 heappop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b )\
    \cf2 del 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 dict
\f0\b [
\f1\b0 item
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 item  \
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 isEmpty
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
        Returns True if the queue is empty\
    """\
    
\f0\b \cf2 return 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b ) == 
\f1\b0 \cf4 0\
\

\f0\b \cf2 class 
\f1\b0 \cf0 FasterPriorityQueue
\f0\b :\
  
\f1\b0 \cf3 """\
    Implements a priority queue data structure.  This differs from the \
    PriorityQueue in that it allows multiple copies of the same object, \
    and doesn't support getPriority or changing priority.\
  """\
  \
  
\f0\b \cf2 def  
\f1\b0 \cf0 __init__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):  \
    
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap 
\f0\b = []\
    \
  \cf2 def 
\f1\b0 \cf0 push
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 item
\f0\b , 
\f1\b0 priority
\f0\b ):\
      
\f1\b0 pair 
\f0\b = (
\f1\b0 priority
\f0\b ,
\f1\b0 item
\f0\b )\
      
\f1\b0 heapq
\f0\b .
\f1\b0 heappush
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b ,
\f1\b0 pair
\f0\b )\
\
  \cf2 def 
\f1\b0 \cf0 pop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
      (
\f1\b0 priority
\f0\b ,
\f1\b0 item
\f0\b ) = 
\f1\b0 heapq
\f0\b .
\f1\b0 heappop
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b )\
      \cf2 return 
\f1\b0 \cf0 item\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 isEmpty
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 heap
\f0\b ) == 
\f1\b0 \cf4 0\
\

\f0\b \cf2 class 
\f1\b0 \cf0 Counter
\f0\b (
\f1\b0 dict
\f0\b ):\
  
\f1\b0 \cf3 """\
  A counter keeps track of counts for a set of keys.\
  \
  The counter class is an extension of the standard python\
  dictionary type.  It is specialized to have number values  \
  (integers or floats), and includes a handful of additional\
  functions to ease the task of counting data.  In particular, \
  all keys are defaulted to have value 0.  Using a dictionary:\
  \
  a = \{\}\
  print a['test']\
  \
  would give an error, while the Counter class analogue:\
    \
  >>> a = Counter()\
  >>> print a.getCount('test')\
  0\
  \
  returns the default 0 value. Note that to reference a key \
  that you know is contained in the counter, \
  you can still use the dictionary syntax:\
    \
  >>> a = Counter()\
  >>> a['test'] = 2\
  >>> print a['test']\
  2\
  \
  The counter also includes additional functionality useful in implementing\
  the classifiers for this assignment.  Two counters can be added,\
  subtracted or multiplied together.  See below for details.  They can\
  also be normalized and their total count and arg max can be extracted.\
  """\
  
\f0\b \cf2 def 
\f1\b0 \cf0 incrementCount
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 key
\f0\b , 
\f1\b0 count
\f0\b ):\
    
\f1\b0 \cf3 """\
    Increases the count of key by the specified count.  If \
    the counter does not contain the key, then the count for\
    key will be set to count.\
    \
    >>> a = Counter()\
    >>> a.incrementCount('test', 1)\
    >>> a.getCount('hello')\
    0\
    >>> a.getCount('test')\
    1\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] += 
\f1\b0 count\
    
\f0\b \cf2 else\cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] = 
\f1\b0 count\
      \
  
\f0\b \cf2 def 
\f1\b0 \cf0 incrementAll
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 keys
\f0\b , 
\f1\b0 count
\f0\b ):\
    
\f1\b0 \cf3 """\
    Increments all elements of keys by the same count.\
    \
    >>> a = Counter()\
    >>> a.incrementAll(['one','two', 'three'], 1)\
    >>> a.getCount('one')\
    1\
    >>> a.getCount('two')\
    1\
    """\
    
\f0\b \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 keys
\f0\b :\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 incrementCount
\f0\b (
\f1\b0 key
\f0\b , 
\f1\b0 count
\f0\b )\
            \
  \cf2 def 
\f1\b0 \cf0 setCount
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 key
\f0\b , 
\f1\b0 count
\f0\b ):\
    
\f1\b0 \cf3 """\
    Sets the count of key to the specified count.\
    """\
    \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] = 
\f1\b0 count\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 getCount
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 key
\f0\b ):\
    
\f1\b0 \cf3 """\
    Returns the count of key, defaulting to zero.\
    \
    >>> a = Counter()\
    >>> print a.getCount('test')\
    0\
    >>> a['test'] = 2\
    >>> print a.getCount('test')\
    2\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
      \cf2 return 
\f1\b0 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ]\
    \cf2 else\cf0 :\
      \cf2 return 
\f1\b0 \cf4 0\
  \
  
\f0\b \cf2 def 
\f1\b0 \cf0 argMax
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
    Returns the key with the highest value.\
    """\
    
\f0\b \cf2 if 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ()) == 
\f1\b0 \cf4 0
\f0\b \cf0 : \cf2 return 
\f1\b0 None\
    \cf0 all 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 items
\f0\b ()\
    
\f1\b0 values 
\f0\b = [
\f1\b0 x
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 all
\f0\b ]\
    
\f1\b0 maxIndex 
\f0\b = 
\f1\b0 values
\f0\b .
\f1\b0 index
\f0\b (
\f1\b0 max
\f0\b (
\f1\b0 values
\f0\b ))\
    \cf2 return 
\f1\b0 \cf0 all
\f0\b [
\f1\b0 maxIndex
\f0\b ][
\f1\b0 \cf4 0
\f0\b \cf0 ]\
  \
  \cf2 def 
\f1\b0 \cf0 sortedKeys
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
    Returns a list of keys sorted by their values.  Keys\
    with the highest values will appear first.\
    \
    >>> a = Counter()\
    >>> a['first'] = -2\
    >>> a['second'] = 4\
    >>> a['third'] = 1\
    >>> a.sortedKeys()\
    ['second', 'third', 'first']\
    """\
    \cf0 sortedItems 
\f0\b = 
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 items
\f0\b ()\
    
\f1\b0 compare 
\f0\b = \cf2 lambda 
\f1\b0 \cf0 x
\f0\b , 
\f1\b0 y
\f0\b :  
\f1\b0 sign
\f0\b (
\f1\b0 y
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] - 
\f1\b0 x
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ])\
    
\f1\b0 sortedItems
\f0\b .
\f1\b0 sort
\f0\b (
\f1\b0 cmp
\f0\b =
\f1\b0 compare
\f0\b )\
    \cf2 return \cf0 [
\f1\b0 x
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ] \cf2 for 
\f1\b0 \cf0 x 
\f0\b \cf2 in 
\f1\b0 \cf0 sortedItems
\f0\b ]\
  \
  \cf2 def 
\f1\b0 \cf0 totalCount
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
    Returns the sum of counts for all keys.\
    """\
    
\f0\b \cf2 return 
\f1\b0 \cf0 sum
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 values
\f0\b ())\
  \
  \cf2 def 
\f1\b0 \cf0 normalize
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 ):\
    
\f1\b0 \cf3 """\
    Edits the counter such that the total count of all\
    keys sums to 1.  The ratio of counts for all keys\
    will remain the same. Note that normalizing an empty \
    Counter will result in an error.\
    """\
    \cf0 total 
\f0\b = 
\f1\b0 float
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 totalCount
\f0\b ())\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 .
\f1\b0 keys
\f0\b ():\
      
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] / 
\f1\b0 total\
      \
  
\f0\b \cf2 def 
\f1\b0 \cf0 divideAll
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 divisor
\f0\b ):\
    
\f1\b0 \cf3 """\
    Divides all counts by divisor\
    """\
    \cf0 divisor 
\f0\b = 
\f1\b0 float
\f0\b (
\f1\b0 divisor
\f0\b )\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
      
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] /= 
\f1\b0 divisor\
\
  
\f0\b \cf2 def 
\f1\b0 \cf0 __mul__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 y 
\f0\b ):\
    
\f1\b0 \cf3 """\
    Multiplying two counters gives the dot product of their vectors where\
    each unique label is a vector element.\
    \
    >>> a = Counter()\
    >>> b = Counter()\
    >>> a['first'] = -2\
    >>> a['second'] = 4\
    >>> b['first'] = 3\
    >>> b['second'] = 5\
    >>> a['third'] = 1.5\
    >>> a['fourth'] = 2.5\
    >>> a * b\
    14\
    """\
    \cf0 sum 
\f0\b = 
\f1\b0 \cf4 0\
    \cf0 x 
\f0\b = 
\f1\b0 \cf2 self\
    
\f0\b if 
\f1\b0 \cf0 len
\f0\b (
\f1\b0 x
\f0\b ) > 
\f1\b0 len
\f0\b (
\f1\b0 y
\f0\b ):\
      
\f1\b0 x
\f0\b ,
\f1\b0 y 
\f0\b = 
\f1\b0 y
\f0\b ,
\f1\b0 x\
    
\f0\b \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 x
\f0\b :\
      \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 not in 
\f1\b0 \cf0 y
\f0\b :\
        \cf2 continue\
      
\f1\b0 \cf0 sum 
\f0\b += 
\f1\b0 x
\f0\b [
\f1\b0 key
\f0\b ] * 
\f1\b0 y
\f0\b [
\f1\b0 key
\f0\b ]      \
    \cf2 return 
\f1\b0 \cf0 sum\
      \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __radd__
\f0\b (
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 y
\f0\b ):\
    
\f1\b0 \cf3 """\
    Adding another counter to a counter increments the current counter\
    by the values stored in the second counter.\
    \
    >>> a = Counter()\
    >>> b = Counter()\
    >>> a['first'] = -2\
    >>> a['second'] = 4\
    >>> b['first'] = 3\
    >>> b['third'] = 1\
    >>> a += b\
    >>> a.getCount('first')\
    1\
    """ \
    
\f0\b \cf2 for 
\f1\b0 \cf0 key
\f0\b , 
\f1\b0 value 
\f0\b \cf2 in 
\f1\b0 \cf0 y
\f0\b .
\f1\b0 items
\f0\b ():\
      
\f1\b0 \cf2 self
\f0\b \cf0 .
\f1\b0 incrementCount
\f0\b (
\f1\b0 key
\f0\b , 
\f1\b0 value
\f0\b )   \
      \
  \cf2 def 
\f1\b0 \cf0 __add__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 y 
\f0\b ):\
    
\f1\b0 \cf3 """\
    Adding two counters gives a counter with the union of all keys and\
    counts of the second added to counts of the first.\
    \
    >>> a = Counter()\
    >>> b = Counter()\
    >>> a['first'] = -2\
    >>> a['second'] = 4\
    >>> b['first'] = 3\
    >>> b['third'] = 1\
    >>> (a + b).getCount('first')\
    1\
    """\
    \cf0 addend 
\f0\b = 
\f1\b0 Counter
\f0\b ()\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
      \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 y
\f0\b :\
        
\f1\b0 addend
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] + 
\f1\b0 y
\f0\b [
\f1\b0 key
\f0\b ]\
      \cf2 else\cf0 :\
        
\f1\b0 addend
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ]\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 y
\f0\b :\
      \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
        \cf2 continue\
      
\f1\b0 \cf0 addend
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 y
\f0\b [
\f1\b0 key
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 addend\
    \
  
\f0\b \cf2 def 
\f1\b0 \cf0 __sub__
\f0\b ( 
\f1\b0 \cf2 self
\f0\b \cf0 , 
\f1\b0 y 
\f0\b ):\
    
\f1\b0 \cf3 """\
    Subtracting a counter from another gives a counter with the union of all keys and\
    counts of the second subtracted from counts of the first.\
    \
    >>> a = Counter()\
    >>> b = Counter()\
    >>> a['first'] = -2\
    >>> a['second'] = 4\
    >>> b['first'] = 3\
    >>> b['third'] = 1\
    >>> (a - b).getCount('first')\
    -5\
    """      \
    \cf0 addend 
\f0\b = 
\f1\b0 Counter
\f0\b ()\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
      \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 y
\f0\b :\
        
\f1\b0 addend
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ] - 
\f1\b0 y
\f0\b [
\f1\b0 key
\f0\b ]\
      \cf2 else\cf0 :\
        
\f1\b0 addend
\f0\b [
\f1\b0 key
\f0\b ] = 
\f1\b0 \cf2 self
\f0\b \cf0 [
\f1\b0 key
\f0\b ]\
    \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 y
\f0\b :\
      \cf2 if 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 self
\f0\b \cf0 :\
        \cf2 continue\
      
\f1\b0 \cf0 addend
\f0\b [
\f1\b0 key
\f0\b ] = -
\f1\b0 \cf4 1 
\f0\b \cf0 * 
\f1\b0 y
\f0\b [
\f1\b0 key
\f0\b ]\
    \cf2 return 
\f1\b0 \cf0 addend\
    \

\f0\b \cf2 def 
\f1\b0 \cf0 raiseNotDefined
\f0\b ():\
  \cf2 print 
\f1\b0 \cf4 "Method not implemented: %s" 
\f0\b \cf0 % 
\f1\b0 inspect
\f0\b .
\f1\b0 stack
\f0\b ()[
\f1\b0 \cf4 1
\f0\b \cf0 ][
\f1\b0 \cf4 3
\f0\b \cf0 ]    \
  
\f1\b0 sys
\f0\b .
\f1\b0 exit
\f0\b (
\f1\b0 \cf4 1
\f0\b \cf0 )\
\
\cf2 def 
\f1\b0 \cf0 normalize
\f0\b (
\f1\b0 vectorOrCounter
\f0\b ):\
  
\f1\b0 \cf3 """\
  normalize a vector or counter by dividing each value by the sum of all values\
  """\
  \cf0 normalizedCounter 
\f0\b = 
\f1\b0 Counter
\f0\b ()\
  \cf2 if 
\f1\b0 \cf0 type
\f0\b (
\f1\b0 vectorOrCounter
\f0\b ) == 
\f1\b0 type
\f0\b (
\f1\b0 normalizedCounter
\f0\b ):\
    
\f1\b0 counter 
\f0\b = 
\f1\b0 vectorOrCounter\
    total 
\f0\b = 
\f1\b0 float
\f0\b (
\f1\b0 counter
\f0\b .
\f1\b0 totalCount
\f0\b ())\
    \cf2 if 
\f1\b0 \cf0 total 
\f0\b == 
\f1\b0 \cf4 0
\f0\b \cf0 : \cf2 return 
\f1\b0 \cf0 counter\
    
\f0\b \cf2 for 
\f1\b0 \cf0 key 
\f0\b \cf2 in 
\f1\b0 \cf0 counter
\f0\b .
\f1\b0 keys
\f0\b ():\
      
\f1\b0 value 
\f0\b = 
\f1\b0 counter
\f0\b .
\f1\b0 getCount
\f0\b (
\f1\b0 key
\f0\b )\
      
\f1\b0 normalizedCounter
\f0\b .
\f1\b0 setCount
\f0\b (
\f1\b0 key
\f0\b , 
\f1\b0 value 
\f0\b / 
\f1\b0 total
\f0\b )\
    \cf2 return 
\f1\b0 \cf0 normalizedCounter\
  
\f0\b \cf2 else\cf0 :\
    
\f1\b0 vector 
\f0\b = 
\f1\b0 vectorOrCounter\
    s 
\f0\b = 
\f1\b0 float
\f0\b (
\f1\b0 sum
\f0\b (
\f1\b0 vector
\f0\b ))\
    \cf2 return \cf0 [
\f1\b0 el 
\f0\b / 
\f1\b0 s 
\f0\b \cf2 for 
\f1\b0 \cf0 el 
\f0\b \cf2 in 
\f1\b0 \cf0 vector
\f0\b ]\
                \
\cf2 def 
\f1\b0 \cf0 nSample
\f0\b (
\f1\b0 distribution
\f0\b , 
\f1\b0 values
\f0\b , 
\f1\b0 n
\f0\b ):\
  \cf2 if 
\f1\b0 \cf0 sum
\f0\b (
\f1\b0 distribution
\f0\b ) != 
\f1\b0 \cf4 1
\f0\b \cf0 :\
    
\f1\b0 distribution 
\f0\b = 
\f1\b0 normalize
\f0\b (
\f1\b0 distribution
\f0\b )\
  
\f1\b0 rand 
\f0\b = [
\f1\b0 random
\f0\b .
\f1\b0 random
\f0\b () \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 n
\f0\b )]\
  
\f1\b0 rand
\f0\b .
\f1\b0 sort
\f0\b ()\
  
\f1\b0 samples 
\f0\b = []\
  
\f1\b0 samplePos
\f0\b , 
\f1\b0 distPos
\f0\b , 
\f1\b0 cdf 
\f0\b = 
\f1\b0 \cf4 0
\f0\b \cf0 ,
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 distribution
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ]\
  \cf2 while 
\f1\b0 \cf0 samplePos 
\f0\b < 
\f1\b0 n
\f0\b :\
    \cf2 if 
\f1\b0 \cf0 rand
\f0\b [
\f1\b0 samplePos
\f0\b ] < 
\f1\b0 cdf
\f0\b :\
      
\f1\b0 samplePos 
\f0\b += 
\f1\b0 \cf4 1\
      \cf0 samples
\f0\b .
\f1\b0 append
\f0\b (
\f1\b0 values
\f0\b [
\f1\b0 distPos
\f0\b ])\
    \cf2 else\cf0 :\
      
\f1\b0 distPos 
\f0\b += 
\f1\b0 \cf4 1\
      \cf0 cdf 
\f0\b += 
\f1\b0 distribution
\f0\b [
\f1\b0 distPos
\f0\b ]\
  \cf2 return 
\f1\b0 \cf0 samples\
    \

\f0\b \cf2 def 
\f1\b0 \cf0 sample
\f0\b (
\f1\b0 distribution
\f0\b , 
\f1\b0 values
\f0\b ):\
  \cf2 if 
\f1\b0 \cf0 sum
\f0\b (
\f1\b0 distribution
\f0\b ) != 
\f1\b0 \cf4 1
\f0\b \cf0 :\
    
\f1\b0 distribution 
\f0\b = 
\f1\b0 normalize
\f0\b (
\f1\b0 distribution
\f0\b )\
  
\f1\b0 choice 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 random
\f0\b ()\
  
\f1\b0 i
\f0\b , 
\f1\b0 total
\f0\b = 
\f1\b0 \cf4 0
\f0\b \cf0 , 
\f1\b0 distribution
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ]\
  \cf2 while 
\f1\b0 \cf0 choice 
\f0\b > 
\f1\b0 total
\f0\b :\
    
\f1\b0 i 
\f0\b += 
\f1\b0 \cf4 1\
    \cf0 total 
\f0\b += 
\f1\b0 distribution
\f0\b [
\f1\b0 i
\f0\b ]\
  \cf2 return 
\f1\b0 \cf0 values
\f0\b [
\f1\b0 i
\f0\b ]\
\
\cf2 def 
\f1\b0 \cf0 getProbability
\f0\b (
\f1\b0 value
\f0\b , 
\f1\b0 distribution
\f0\b , 
\f1\b0 values
\f0\b ):\
  
\f1\b0 \cf3 """\
    Gives the probability of a value under a discrete distribution\
    defined by (distributions, values).\
  """\
  \cf0 total 
\f0\b = 
\f1\b0 \cf4 0.0\
  
\f0\b \cf2 for 
\f1\b0 \cf0 prob
\f0\b , 
\f1\b0 val 
\f0\b \cf2 in 
\f1\b0 \cf0 zip
\f0\b (
\f1\b0 distribution
\f0\b , 
\f1\b0 values
\f0\b ):\
    \cf2 if 
\f1\b0 \cf0 val 
\f0\b == 
\f1\b0 value
\f0\b :\
      
\f1\b0 total 
\f0\b += 
\f1\b0 prob\
  
\f0\b \cf2 return 
\f1\b0 \cf0 total\
    \

\f0\b \cf2 def 
\f1\b0 \cf0 manhattanDistance
\f0\b ( 
\f1\b0 xy1
\f0\b , 
\f1\b0 xy2 
\f0\b ):\
  
\f1\b0 \cf3 """\
  Returns the Manhattan distance between points xy1 and xy2\
  """\
  
\f0\b \cf2 return 
\f1\b0 \cf0 abs
\f0\b ( 
\f1\b0 xy1
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ] - 
\f1\b0 xy2
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ] ) + 
\f1\b0 abs
\f0\b ( 
\f1\b0 xy1
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] - 
\f1\b0 xy2
\f0\b [
\f1\b0 \cf4 1
\f0\b \cf0 ] )\
\
\cf2 def 
\f1\b0 \cf0 flipCoin
\f0\b ( 
\f1\b0 p 
\f0\b ):\
  
\f1\b0 r 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 random
\f0\b ()\
  \cf2 return 
\f1\b0 \cf0 r 
\f0\b < 
\f1\b0 p \
\

\f0\b \cf2 def 
\f1\b0 \cf0 chooseFromDistribution
\f0\b ( 
\f1\b0 distribution 
\f0\b ):\
  
\f1\b0 r 
\f0\b = 
\f1\b0 random
\f0\b .
\f1\b0 random
\f0\b ()\
  
\f1\b0 base 
\f0\b = 
\f1\b0 \cf4 0.0\
  
\f0\b \cf2 for 
\f1\b0 \cf0 prob
\f0\b , 
\f1\b0 element 
\f0\b \cf2 in 
\f1\b0 \cf0 distribution
\f0\b :\
    
\f1\b0 base 
\f0\b += 
\f1\b0 prob\
    
\f0\b \cf2 if 
\f1\b0 \cf0 r 
\f0\b <= 
\f1\b0 base
\f0\b : \cf2 return 
\f1\b0 \cf0 element\
    \

\f0\b \cf2 def 
\f1\b0 \cf0 nearestPoint
\f0\b ( 
\f1\b0 pos 
\f0\b ):\
  
\f1\b0 \cf3 """\
  Finds the nearest grid point to a position (discretizes).\
  """\
  
\f0\b \cf0 ( 
\f1\b0 current_row
\f0\b , 
\f1\b0 current_col 
\f0\b ) = 
\f1\b0 pos\
\
  grid_row 
\f0\b = 
\f1\b0 int
\f0\b ( 
\f1\b0 current_row 
\f0\b + 
\f1\b0 \cf4 0.5 
\f0\b \cf0 ) \
  
\f1\b0 grid_col 
\f0\b = 
\f1\b0 int
\f0\b ( 
\f1\b0 current_col 
\f0\b + 
\f1\b0 \cf4 0.5 
\f0\b \cf0 ) \
  \cf2 return \cf0 ( 
\f1\b0 grid_row
\f0\b , 
\f1\b0 grid_col 
\f0\b )     \
\
\cf2 def 
\f1\b0 \cf0 sign
\f0\b ( 
\f1\b0 x 
\f0\b ):\
  
\f1\b0 \cf3 """\
  Returns 1 or -1 depending on the sign of x\
  """\
  
\f0\b \cf2 if\cf0 ( 
\f1\b0 x 
\f0\b >= 
\f1\b0 \cf4 0 
\f0\b \cf0 ):\
    \cf2 return 
\f1\b0 \cf4 1\
  
\f0\b \cf2 else\cf0 :\
    \cf2 return \cf0 -
\f1\b0 \cf4 1\
\

\f0\b \cf2 def 
\f1\b0 \cf0 arrayInvert
\f0\b (
\f1\b0 array
\f0\b ):\
  
\f1\b0 \cf3 """\
  Inverts a matrix stored as a list of lists.\
  """\
  \cf0 result 
\f0\b = [[] \cf2 for 
\f1\b0 \cf0 i 
\f0\b \cf2 in 
\f1\b0 \cf0 array
\f0\b ]\
  \cf2 for 
\f1\b0 \cf0 outer 
\f0\b \cf2 in 
\f1\b0 \cf0 array
\f0\b :\
    \cf2 for 
\f1\b0 \cf0 inner 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b (
\f1\b0 len
\f0\b (
\f1\b0 outer
\f0\b )):\
      
\f1\b0 result
\f0\b [
\f1\b0 inner
\f0\b ].
\f1\b0 append
\f0\b (
\f1\b0 outer
\f0\b [
\f1\b0 inner
\f0\b ])\
  \cf2 return 
\f1\b0 \cf0 result\
\

\f0\b \cf2 def 
\f1\b0 \cf0 matrixAsList
\f0\b ( 
\f1\b0 matrix
\f0\b , 
\f1\b0 value 
\f0\b = \cf2 True \cf0 ):\
  
\f1\b0 \cf3 """\
  Turns a matrix into a list of coordinates matching the specified value\
  """\
  \cf0 rows
\f0\b , 
\f1\b0 cols 
\f0\b = 
\f1\b0 len
\f0\b ( 
\f1\b0 matrix 
\f0\b ), 
\f1\b0 len
\f0\b ( 
\f1\b0 matrix
\f0\b [
\f1\b0 \cf4 0
\f0\b \cf0 ] )\
  
\f1\b0 cells 
\f0\b = []\
  \cf2 for 
\f1\b0 \cf0 row 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b ( 
\f1\b0 rows 
\f0\b ):\
    \cf2 for 
\f1\b0 \cf0 col 
\f0\b \cf2 in 
\f1\b0 \cf0 range
\f0\b ( 
\f1\b0 cols 
\f0\b ):\
      \cf2 if 
\f1\b0 \cf0 matrix
\f0\b [
\f1\b0 row
\f0\b ][
\f1\b0 col
\f0\b ] == 
\f1\b0 value
\f0\b :\
        
\f1\b0 cells
\f0\b .
\f1\b0 append
\f0\b ( ( 
\f1\b0 row
\f0\b , 
\f1\b0 col 
\f0\b ) )\
  \cf2 return 
\f1\b0 \cf0 cells}