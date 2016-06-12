#Source: http://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree-in-python

class Node:
    def __init__(self, val, name):
        self.l = None
        self.r = None
        self.v = val
        self.n = name

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val, name):
        if(self.root == None):
            self.root = Node(val, name)
        else:
            self._add(val, name, self.root)

    def _add(self, val, name, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, name, node.l)
            else:
                node.l = Node(val, name)
        else:
            if(node.r != None):
                self._add(val, name, node.r)
            else:
                node.r = Node(val, name)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(node.v) + ' ')
            self._printTree(node.r)

tree = Tree()
tree.add(3, "Brazil")
tree.add(4, 'Russia')
tree.add(0, 'USA')
tree.add(8, 'Germany')
tree.add(2, 'Canada')
print ("Printing tree")
tree.printTree()
print ((tree.find(3)).n)
print (tree.find(10))
tree.deleteTree()
tree.printTree()
