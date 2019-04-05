class Node:
    """
    Tree node: left child, right child and data.
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data.
    """
    def __init__(self, val1, val2):
        self.a1 = val1
        self.a2 = val2
    
if __name__ == '__main__':
    d = Data(1, 2)
    print(d.a1, d.a2)