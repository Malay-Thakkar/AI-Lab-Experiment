import enum
import time


class Action(enum.Enum):
    MoveDown = 0
    MoveUp = 1
    MoveLeft = 2
    MoveRight = 3
    noAction = 4


class Node:

    def __init__(self, position, action=Action.noAction, parent=None):
        self.position = position
        self.action = action
        self.parent = parent
        self.h = 0
        self.f = 0

    def printNode(self):
        print("Position : ", self.position, "\n", "Action : ", self.action, "\n", "Parent : ", self.parent, "\n", )

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __repr__(self):
        return '\n'.join(
            ['\n', str(self.action), str(self.position[:3]), str(self.position[3:6]), str(self.position[6:])]).replace(
            '[', '').replace(']', '').replace(',', '').replace('0', '_')

    # heuristic value
    def _h(self, goal):
        return sum([1 if self.position[i] != goal[i] else 0 for i in range(9)])

    def generateValue(self, goal):
        self.h = self._h(goal)
        self.f = self.h

    # Possible Moves

    def possibleMoves(self):
        successor = []
        i = self.position.index(0)

        # MoveDown
        if i in [3, 4, 5, 6, 7, 8]:
            newValue = self.position[:]
            newValue[i], newValue[i - 3] = newValue[i - 3], newValue[i]

            successor.append(Node(position=newValue, parent=self, action=Action.MoveDown))

        # MoveUp
        if i in [0, 1, 2, 3, 4, 5]:
            newValue = self.position[:]
            newValue[i], newValue[i + 3] = newValue[i + 3], newValue[i]

            successor.append(Node(position=newValue, parent=self, action=Action.MoveUp))

        # MoveLeft
        if i in [0, 1, 3, 4, 6, 7]:
            newValue = self.position[:]
            newValue[i], newValue[i + 1] = newValue[i + 1], newValue[i]

            successor.append(Node(position=newValue, parent=self, action=Action.MoveLeft))

        # MoveRight
        if i in [1, 2, 4, 5, 7, 8]:
            newValue = self.position[:]
            newValue[i], newValue[i - 1] = newValue[i - 1], newValue[i]

            #             successor.append(Node(newValue,self,Action.MoveDown))
            successor.append(Node(position=newValue, parent=self, action=Action.MoveRight))

        return successor


def push(list1, node):
    list1.append(node)


def pop(list1):
    a = list1[0]
    del list1[0]
    return a


def not_empty(list1):
    if len(list1) != 0:
        return True
    else:
        return False


# PrintPath
def printpath(node, iniState):
    list3 = []
    while (node != iniState):
        list3.append(node)
        node = node.parent
    reversed_list = [list3[-(i + 1)] for i in range(len(list3))]

    print('The path :\n ')
    for i in range(len(reversed_list)):
        print('Action No:', i + 1, reversed_list[i])

    print('\nThe Cost :', len(reversed_list))


def can_add_to_openlist(openList, successor):
    for node in openList:
        if successor == node and successor.f >= node.f:
            return False
    return True


def EightPuzzle(initialState, goalState):
    iniState = Node(initialState)
    iniState.generateValue(goalState)

    openList = []
    closedList = []
    find = 1

    openList.append(iniState)
    while (not_empty(openList)):
        openList.sort()
        currentNode = pop(openList)
        #         print(type(currentNode))
        closedList.append(currentNode)
        if currentNode.position == goalState:
            find = 1
            printpath(currentNode, iniState)
            break
        else:
            successors = currentNode.possibleMoves()
        for succ in successors:
            if succ in closedList:
                continue
            else:
                succ.generateValue(goalState)
                if can_add_to_openlist(openList, succ):
                    openList.append(succ)

    if find == 1:
        print("Solution Found...")
    else:
        print("Solution UnFound....")


if __name__ == '__main__':
    #     initialState = [3,0,7,2,8,1,6,4,5]
    #     goalState = [1,2,3,4,5,6,7,8,0]
    print("20012011169 Malay Thakkar")
    initialState = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    startTime = time.time()
    EightPuzzle(initialState, goalState)
    endTime = time.time()

    print("Total time :", (endTime - startTime) * 1000, "ms")
