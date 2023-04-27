class Node:
    def __init__(self, data, parent, childlist):
        self.data = data
        self.parent = parent
        self.childlist = childlist
        self.level = 0
        if self.parent != None:
            self.level = self.parent.level + 1


    def add_child(self, child):
        self.childlist.append(child)


    def space_count(self):
        str_parent = ""
        if self.parent == None:
            str_parent = str(self.parent)
        else:
            str_parent = "None"
            temp = self.parent
            while temp != None:
                str_parent += "->" + temp.data
                temp = temp.parent
        return len(str_parent)


    def __repr__(self):
        str_parent = ""
        if self.parent == None:
            str_parent = str(self.parent)
        else:
            str_parent = str(self.parent.data)
        str_return = "\n"
        str_return += " " * self.space_count()
        str_return += "->" + str(self.data) + " " + \
            ' '.join(map(str, self.childlist))
        return str_return


class Tree:
    def __init__(self, root):
        self.root = root

    def insert_node(self, data, parent):
        node = Node(data, parent, [])
        parent.add_child(node)
        return node

    def __repr__(self):
        return str(self.root)

def bfs(tree, search_string):
    queue = []
    queue.append(tree.root)
    node = None
    while queue:
        temp = queue.pop(0)
        if temp.data == search_string:
            node = temp
            break
        queue.extend(temp.childlist)
    return node

def draw_path(node):
    list = []
    temp = node
    while temp != None:
        list.append(temp.data)
        temp = temp.parent
        if temp == None:
            break
    list.reverse()
    print("Path: ")
    print(*list, sep="->")
    print("Path Cost = " + str(len(list)-1))
tree = Tree(Node("India", None, []))
gujarat = tree.insert_node("Gujarat", tree.root)
ahmedabad = tree.insert_node("Ahmedabad", gujarat)
mehsana = tree.insert_node("Mehsana", gujarat)
gandhinagar = tree.insert_node("Gandhinagar", gujarat)
rajasthan = tree.insert_node("Rajasthan", tree.root)
jaipur = tree.insert_node("Jaipur", rajasthan)
jodhpur = tree.insert_node("Jodhpur", rajasthan)
ajmer = tree.insert_node("Ajmer", rajasthan)
kota = tree.insert_node("Kota", rajasthan)
maharashtra = tree.insert_node("Maharashtra", tree.root)
mumbai = tree.insert_node("Mumbai", maharashtra)
bandra = tree.insert_node("Bandra", mumbai)
juhu = tree.insert_node("Juhu", mumbai)
nashik = tree.insert_node("Nashik", maharashtra)
pune = tree.insert_node("Pune", maharashtra)
nagpur = tree.insert_node("Nagpur", maharashtra)
thane = tree.insert_node("Thane", maharashtra)

print("Malay Thakkar (20012011169)")
print(tree)
search_string = "Bandra"
print("Search String = " + search_string)
node = bfs(tree, search_string)
if node == None:
    print(search_string + "String can't be found in tree")
else:
    draw_path(node)
