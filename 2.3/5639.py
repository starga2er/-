import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

answer = []

class Node :
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def append(self, n):
        if self.root == None :
            self.root = Node(n)
        
        else :
            current = self.root
            while (True) :
                if (current.data > n):
                    if (current.left == None):
                        current.left = Node(n)
                        break
                    current = current.left
                else :
                    if (current.right == None):
                        current.right = Node(n)
                        break
                    current = current.right
                    
                       
    def print(self, n=None):
        global answer
        if n == None:
            n = self.root
        if n.left != None:
            self.print(n.left)
        if n.right != None:
            self.print(n.right)
        print(n.data)

tree = Tree()
while (True):
    try:
        tree.append(int(input()))
    except:
        break

tree.print()
