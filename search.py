# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import random

class Pacman:                                                     #Struct com status do Pacman
  
    def __init__(self, state, parent, action, stepcost):
        self.state  = state                                       #estado do proprio nodo
        self.parent = parent                                      #nodo pai
        self.action = action
        self.cost = stepcost
        if parent:
            actionsToGoal = parent.actionsToReachNode[:]
            actionsToGoal.append(action)
            self.actionsToReachNode = actionsToGoal 
        else:
            self.actionsToReachNode = []

    def getCost(self):
        return self.cost

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent
    
    def getAction(self):
        return self.action

    def pacmanRun(self):
        movimentos = []
        pacAtual = self
        while pacAtual.getAction() is not None:                   #enquanto houver acoes a fazer vai printando
            print movimentos                                      #retorna os passos necessarios para chegar no Estado Meta
            movimentos.append(pacAtual.getAction())               #add a lista o passo que cada nodo deu              
            pacAtual = pacAtual.parent                            #sobe para o pai
        movimentos.reverse()                                      #inverte a ordem para ficar na ordem certa que foi percorrido
        return movimentos
    
    def getActionsToReachNode(self):
        return self.actionsToReachNode

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           
def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  #Queue - BFS
  
  pac = util.Stack()                                                          #Pilha LIFO.
  nodosExplorados = []                                                        #Array com Nodos Explorados

  nodo = Pacman(problem.getStartState(), None, None)
  pac.push( nodo )                                                            #Guarda na Pilha o Estado Inicial do Primeiro estado do Pacman
 
  while (not pac.isEmpty()):                                                  #Enquanto ha itens na pilha para consumir
      pacAtual = pac.pop()                                                    #Consome a pilha que contem estados sucessores da raiz
      nodosExplorados.append(pacAtual.getState())                             #add nodo visitado para nao visitar novamente

      if problem.isGoalState(pacAtual.getState()):                            #Testa se o pacman esta no Estado Meta
          print "\n" 
          print " Melhor Caminho:"
          print "\n"
          return pacAtual.pacmanRun()                                         #Depois de Chegar ao estado meta coloca Pacman para andar
      else:
          nextpac = problem.getSuccessors(pacAtual.getState())                #Retorna os proximos passos
          for proxNodo in nextpac:                                            #Percorre todos os proximos nodos
              #print proxNodo
              if proxNodo[0] not in nodosExplorados:                          #se o nodo nao foi explorado add na pilha para consumir depois
                  nodo = Pacman(proxNodo[0], pacAtual, proxNodo[1])
                  pac.push( nodo )                                            #proxNodo[0] - onde o nodo esta no mapa, proxNodo[1] - acao do nodo

  print "Erro - Pacman esta sem estado inicial."

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  
  pac = util.PriorityQueue()                                       #Filas de Prioridade
  nodosExplorados = []                                             #Array com Nodos Explorados

  nodo = Pacman(problem.getStartState(), None, None, 0)
  pac.push(nodo, problem.getCostOfActions(nodo.actionsToReachNode) + heuristic(nodo.getState(),problem))

  while (not pac.isEmpty()):                                       #Enquanto ha itens na pilha para consumir
    pacAtual = pac.pop()                                           #Consome a pilha que contem estados sucessores da raiz
    nodosExplorados.append(pacAtual.getState())                    #add nodo visitado para nao visitar novamente
    
    if problem.isGoalState(pacAtual.getState()):                   #Testa se o pacman esta no Estado Meta
        print "\n" 
        print " Melhor Caminho:"
        print "\n"
        print pacAtual.getActionsToReachNode()                     #Printa melhor caminho
        return pacAtual.getActionsToReachNode()                    #Depois de Chegar ao estado meta coloca Pacman para andar
    else:
        nextpac = problem.getSuccessors(pacAtual.getState())       #Retorna os proximos passos
        for proxNodo in nextpac:                                   #Percorre todos os proximos nodos
          if proxNodo[0] not in nodosExplorados:                   #se o nodo nao foi explorado add na pilha para consumir depois
            print proxNodo
            nodo = Pacman(proxNodo[0], pacAtual, proxNodo[1], proxNodo[2])
            pac.push( nodo, problem.getCostOfActions(nodo.getActionsToReachNode()) + heuristic(nodo.getState(),problem) )
   
def hillclimb(problem, heuristic):
  
  pac = util.PriorityQueue()                                       #Filas de Prioridade
  nodosExplorados = []                                             #Array com Nodos Explorados

  nodo = Pacman(problem.getStartState(), None, None, 0)
  pac.push(nodo, problem.getCostOfActions(nodo.actionsToReachNode) + heuristic(nodo.getState(),problem))
  
  while (not pac.isEmpty()):                                       #Enquanto ha itens na pilha para consumir
    pacAtual = pac.pop()                                           #Consome a pilha que contem estados sucessores da raiz
    nodosExplorados.append(pacAtual.getState())                    #add nodo visitado para nao visitar novamente
    
    costAtual = heuristic(nodo.getState(), problem)
    if problem.isGoalState(pacAtual.getState()):                   #Testa se o pacman esta no Estado Meta
        print "\n" 
        print " Caminho Encontrado:"
        print "\n"
        print pacAtual.getActionsToReachNode()                     #Printa melhor caminho
        return pacAtual.getActionsToReachNode()                    #Depois de Chegar ao estado meta coloca Pacman para andar
    else:
        nextpac = problem.getSuccessors(pacAtual.getState())       #Retorna os proximos passos
        for proxNodo in nextpac:                                   #Percorre todos os proximos nodos
            
            if proxNodo[0] not in nodosExplorados:                   #se o nodo nao foi explorado add na pilha para consumir depois
              if  heuristic(proxNodo[0], problem) < costAtual:
                nodo = Pacman(proxNodo[0], pacAtual, proxNodo[1], proxNodo[2])
                pac.push( nodo, problem.getCostOfActions(nodo.getActionsToReachNode()) + heuristic(nodo.getState(),problem) )
  #caso nao chegue no meta e nao tenha mais sucessores melhores
  print "\n" 
  print " Caminho Encontrado:"
  print "\n"
  print pacAtual.getActionsToReachNode()                     #Printa melhor caminho
  return pacAtual.getActionsToReachNode()                    #Depois de Chegar ao estado meta coloca Pacman para andar

def SimulatedAnnealing(problem, heuristic=nullHeuristic):
  
  pac = util.PriorityQueue()                                       #Filas de Prioridade
  nodosExplorados = []                                             #Array com Nodos Explorados

  nodo = Pacman(problem.getStartState(), None, None, 0)
  pac.push(nodo, problem.getCostOfActions(nodo.actionsToReachNode) + heuristic(nodo.getState(),problem))

  while True:   #(not pac.isEmpty()):                                       #Enquanto ha itens na pilha para consumir
    pacAtual = pac.pop()                                           #Consome a pilha que contem estados sucessores da raiz
    costAtual = problem.getCostOfActions(pacAtual.actionsToReachNode)
    
    nodosExplorados.append(pacAtual.getState())                    #add nodo visitado para nao visitar novamente
    
    if problem.isGoalState(pacAtual.getState()):                   #Testa se o pacman esta no Estado Meta
        print "\n" 
        print " Caminho Encontrado:"
        print "\n"
        print pacAtual.getActionsToReachNode()                     #Printa melhor caminho
        return pacAtual.getActionsToReachNode()                    #Depois de Chegar ao estado meta coloca Pacman para andar
    else:
        nextpac = problem.getSuccessors(pacAtual.getState())       #Retorna os proximos passos
        for proxNodo in nextpac:                                   #Percorre todos os proximos nodos
            
            print problem.getCostOfActions(pacAtual.actionsToReachNode)
            #util.pause()
            
            if problem.getCostOfActions(pacAtual.actionsToReachNode) >= costAtual:
              if proxNodo[0] not in nodosExplorados:                   #se o nodo nao foi explorado add na pilha para consumir depois
                print proxNodo
                nodo = Pacman(proxNodo[0], pacAtual, proxNodo[1], proxNodo[2])
                pac.push( nodo, problem.getCostOfActions(nodo.getActionsToReachNode()) + heuristic(nodo.getState(),problem) )
            else:
              num = random.randint(0, costAtual)
              for x in range(0,  num):     #entre nao voltar nada e poder voltar ate todos os passos
                pac = pac.parent                 #vai voltando ate o numero sortiado     

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
hclimb = hillclimb
sannealing = SimulatedAnnealing
ucs = uniformCostSearch