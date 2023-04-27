
import time
import random


class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data
    def __cmp__(self,other):
      if(other == None):
        return False
      return self.x == other.x and self.y == other.y
    def __eq__(self,other):
      if(other == None):
        return False
      return self.x == other.x and self.y == other.y
    def __repr__(self):
      return "("+str(self.x)+", "+str(self.y)+")"

def operation(cnode, rule):
        x = cnode.x
        y = cnode.y

        if rule == 1:
            if x < maxjug1:
                x = maxjug1
            else:
                return None
        elif rule==2:
            if y < maxjug2:
                y = maxjug2
            else:
                return None
        elif rule==3:
            if x > 0:
                x = 0
            else:
                return None
        elif rule==4:
            if y > 0:
                y = 0
            else:
                return None
        elif rule==5:
            if x+y >= maxjug1:
                y=y-(maxjug1-x)
                x = maxjug1
            else:
                return None
        elif rule==6:
            if x+y >= maxjug2:
                x = x-(maxjug2-y)
                y = maxjug2
            else:
                 return None
        elif rule==7:
            if x+y < maxjug1:
                x = x+y
                y = 0
            else:
                return None
        elif rule==8:
            if x+y < maxjug2:
                y = x+y
                x = 0
            else:
                return None
        if(x==cnode.x and y==cnode.y):
            return None
        nextnode=node(cnode)
        nextnode.x=x
        nextnode.y=y
        nextnode.parent=cnode
        return nextnode
class BFS:
  def __init__(self,initNode,goalNode):
    self.initNode = initNode
    self.goalNode = goalNode
    self.q = []
    self.q.append(initNode)
  def pushList(self,list1):
    self.q.extend(list1)
  def popNode(self):
    return self.q.pop(0)
  def isNotEmpty(self):
    return len(self.q)>0
  def generateAllSuccessor(self,cnode):
    list1 = []
    for i in range(1,9):
      nextNode = operation(cnode,i)
      if(nextNode != None):
        list1.append(nextNode)
    return list1
  def execution(self):
    while self.isNotEmpty():
      cnode = self.popNode()
      #print("Pop Node:"+str(cnode))
      if cnode.x == self.goalNode.x:
        return cnode
      list1 = self.generateAllSuccessor(cnode)
      self.pushList(list1)
    return None
class DFS:
  def __init__(self,initNode,goalNode):
    self.initNode = initNode
    self.goalNode = goalNode
    self.q = []
    self.q.append(initNode)
    self.popList = []
  def pushList(self,list1):
    self.q.extend(list1)
  def popNode(self):
    return self.q.pop()
  def isNotEmpty(self):
    return len(self.q)>0
  def generateAllSuccessor(self,cnode):
    list1 = []
    for i in range(1,9):
      nextNode = operation(cnode,i)
      if(nextNode != None):
        list1.append(nextNode)
    return list1
  def generateAllSuccessorByRandom(self,cnode):
    list1 = []
    ruleList = []
    while(len(ruleList)!= 8):
      i = random.randint(1,8)
      if(i not in ruleList):
        ruleList.append(i)
    for i in ruleList:
      nextNode = operation(cnode,i)
      if(nextNode != None):
        list1.append(nextNode)
    return list1
  def generateAllSuccessorByRandomPopList(self,cnode):
    list1 = []
    ruleList = []
    while(len(ruleList)!= 8):
      i = random.randint(1,8)
      if(i not in ruleList):
        ruleList.append(i)
    for i in ruleList:
      nextNode = operation(cnode,i)
      if(nextNode != None and nextNode not in self.popList):
        list1.append(nextNode)
    return list1
  def execution(self):
    while self.isNotEmpty():
      cnode = self.popNode()
      self.popList.append(cnode)
      #print("Pop Node:"+str(cnode))
      if cnode.x == self.goalNode.x:
        return cnode
      list1 = self.generateAllSuccessorByRandomPopList(cnode)
      self.pushList(list1)
    return None
def printPath(cnode):
  temp = cnode
  retStr = ""
  pathCost = 0
  while(temp!=None):
    retStr = str(temp)+"\n"+retStr
    temp = temp.parent
    pathCost += 1
  print(retStr)
  print("Path Cost="+str(pathCost-1))
  
print("Malay Thakkar-20012011169")
maxjug1=int(input("Enter value of maxjug1:"))
maxjug2=int(input("Enter value of maxjug2:"))
initialNode=node(None)
initialNode.x=0
initialNode.y=0
initialNode.parent=None
GoalNode=node(None)
GoalNode.x=int(input("Enter value of goal in jug1:"))
GoalNode.y=0
GoalNode.parent=None
print("BFS Algorithm")
startTime = time.time()
bfsSolNode = BFS(initialNode,GoalNode).execution()
endTime = time.time()
diffTime = endTime - startTime
if(bfsSolNode != None):
  print("Got Solution:")
  printPath(bfsSolNode)
  print("Execution Time="+str(diffTime*1000)+"ms")
else:
  print("No Solution")
print("DFS Algorithm")
startTime = time.time()
dfsSolNode = DFS(initialNode,GoalNode).execution()
endTime = time.time()
diffTime = endTime - startTime
if(dfsSolNode != None):
  print("Got Solution:")
  printPath(dfsSolNode)
  print("Execution Time="+str(diffTime*1000)+"ms")
else:
  print("No Solution")
