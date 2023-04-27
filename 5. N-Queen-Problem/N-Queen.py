import time
import queue
import random
import numpy as np
import matplotlib.pyplot as plt
from heapq import heappush, heappop, heapify

N = int(input("Enter the number of Queen You want to place: "))
a = queue.Queue()
class PriorityQueue:
    
    def __init__(self):
        self.pq = []
        
    def add(self, item):
        heappush(self.pq, item)
        
    def poll(self):
        return heappop(self.pq)
    
    def peek(self):
        return self.pq[0]
    
    def remove(self, item):
        value = self.pq.remove(item)
        heapify(self.pq)
        return value is not None

    def __len__(self):
        return len(self.pq)
    
class queen:
    def __init__(self):
        self.row = -1
        self.col = -1
    def __cmp__(self, other):
        return self.row == other.row and self.cok == other.col
    
    def __eq__(self, other):
        return self.__cmp__(other)
    
    def __hash__(self):
        return hash(str(self.list_()))
    def list_(self):
        return [self.row,self.col]

class state:
    def __init__(self, data):
        self.nQueen = [queen() for i in range(N)]
        if(data != None):
            self.moves = data.moves + 1
            self.heuristicVal = data.heuristicVal
            for i in range(N):
                self.nQueen[i].row = data.nQueen[i].row
                self.nQueen[i].col = data.nQueen[i].col
        else:
            self.moves = 0
            self.initQueens()
        self.parent = data
        
    def getConflictCount(self,row,col):
        count = 0
        conflictCount = 0
        ConflictSet = []
        for i in range(N):
            if(self.nQueen[i].row == row):
                count+=1
                ConflictSet.append(self.nQueen[i])
        for i in range(N):
            if(self.nQueen[i].col == col):
                count+=1
                ConflictSet.append(self.nQueen[i])
        for i in range(N):
            if(abs(self.nQueen[i].row - row) == abs(self.nQueen[i].col -col)):
                count+=1
                ConflictSet.append(self.nQueen[i])
        for obj in ConflictSet:
            if(not(obj.row == row and obj.col == col)):
                conflictCount+=1
        return conflictCount
    
    def placeQueen(self,row,col):
        if(row >= N or col >= N):
            return
        if(self.nQueen[col].row == row and self.nQueen[col].col == col):
            return
        self.nQueen[col].row = row
        self.nQueen[col].col = col
        self.heuristicVal = self.getHeuristicCost()
        
    def printQueen(self):
        for i in range(N):
            for j in range(N):
                if(self.nQueen[j].row == i):
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
        print()
        
    def drawQueens(self):
        board = self.getMatrix()
        matrix = np.zeros ((N, N))
        matrix = matrix.astype(str)
        
        for i in range(N):
            for j in range (N):
                if board[i][j] == 1:
                    matrix[i][j] = 'Q'
                else:
                    matrix[i][j] =' '
        
        w = 5
        h = 5
        plt.figure(1, figsize=(w, h))
        tb = plt.table(cellText=matrix, loc=(0, 0), cellLoc='center')
        
        for i in range(N):
            for j in range(N):
                if board[i][j] ==1:
                    tb._cells[(i, j)]._text.set_color('#960018')
                    tb._cells[(i, j)]._text.set_weight('extra bold')
                if ((i + j) % 2) == 0:
                    tb._cells[(i, j)].set_facecolor('#CD853F')
                else:
                    tb._cells[(i, j)].set_facecolor('#FADFAD')
                tb._cells[(i, j)].set_height(1.0 / N)
                tb._cells[(i, j)].set_width(1.0 / N)
        ax = plt.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
        
    def getMatrix(self):
        board = np.zeros((N, N))
        board.astype(int)
        for j in range(N):
            for i in range(N):
                if(self.nQueen[i].row == j):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board
    
    def initQueens(self):
        for col in range(N):
            row = random.randint(0,N-1)
            self.placeQueen(row, col)
        self.moves = 0
        self.heuristicVal = self.getHeuristicCost()
        
    def getHeuristicCost(self):
        count = 0
        for i in range(N):
            count = count + self.getConflictCount(self.nQueen[i].row, self.nQueen[i].col)
        return count
    
    def score(self):
        return self._h() + self._g()
    
    def _h(self):
        return self.heuristicVal
    
    def _g(self):
        return self.moves
    
    def __cmp__(self, other):
        if(other == None):
            return False
        return self.nQueen == other.nQueen
    
    def __eq__(self, other):
        return self.__cmp__(other)
    
    def __hash__(self):
        return hash(str(self.nQueen))
    
    def __lt__(self, other):
        return self.score() < other.score()
    
    def nextAllState(self):
        list1 = []
        row = self.moves
        for i in range(N):
            if(not(self.nQueen[i].row == row and self.nQueen[i].col == i)):
                nextState = state(self)
                nextState.placeQueen(row, i)
                list1.append(nextState)
        return list1
    
def solve(initial_state):
    openset = PriorityQueue()
    openset.add(initial_state)
    closed = set()
    moves = 0
    print("Trying to solve:")
    print(openset.peek().printQueen(),'\n\n')
    start = time.time()
    while openset:
        current = openset.poll()
        if current.heuristicVal == 0:
            end = time.time()
            print('I found a solution')
            current.printQueen()
            current.drawQueens()
            print('I found the solution in %2.f milliseconds'% float((end - start)*1000))
            break
        moves += 1
        for state in current.nextAllState():
            if state not in closed:
                openset.add(state)
        closed.add(current)
    else:
        print('I couldn''t solve it!')
        
def main():
    initial_state = state(None)
    solve(initial_state)
    
if __name__ == '__main__':
    main()