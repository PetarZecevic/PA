import tree
import copy
from random import randint

def add_left(parent_node, data):
    parent_node.left = tree.Node(d=data)
    parent_node.left.parent = parent_node

def add_right(parent_node, data):
    parent_node.right = tree.Node(d=data)
    parent_node.right.parent = parent_node

def print_node(n):
    if n != None:
        print("----------")
        print("Kljuc: ", n.data.a1)
        print("Vrednost: ", n.data.a2)
        print("----------")
    else:
        print("Empty node")

def inorder_tree_walk(t, l=False, sort_list=None):
    if t != None:
        inorder_tree_walk(t.left,l,sort_list)
        if l:
            sort_list.append(t.data.a1)
        else:
            print_node(t)
        inorder_tree_walk(t.right,l,sort_list)  

def search_tree(t, key):
    if t == None or key == t.data.a1:
        return t
    if key < t.data.a1:
        search_tree(t.left, key)
    else:
        search_tree(t.right, key)

def iterative_tree_search(t, key):
    while t != None and key != t.data.a1:
        if key < t.data.a1:
            t = t.left
        else:
            t = t.right
    return t

def tree_minimum(t):
    while t.left != None:
        t = t.left
    return t

def tree_maximum(t):
    while t.right != None:
        t = t.right
    return t

def tree_successor(t):
    if t.right != None:
        return tree_minimum(t.right)
    p = t.parent
    while p != None and t == p.right:
        t = p
        p = p.parent
    return p    

def tree_insert(t, data):
    x = t
    z = tree.Node(d=data)
    if x == None:
        x = z
    else:
        y = None
        while x != None:
            y = x
            if data.a1 < x.data.a1:
                x = x.left
            else:
                x = x.right
        z.parent = y        
        if data.a1 < y.data.a1:
            y.left = z
        else:
            y.right = z

def tree_transplant(t, u, v):
    if u.parent == None:
        t = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent
                
def tree_delete(t, z):
    x = t
    if z.left == None:
        tree_transplant(x, z, z.right)
    elif z.right == None:
        tree_transplant(x, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            tree_transplant(x, y, y.right)
            y.right = z.right
            y.right.parent = y
        tree_transplant(x, z, y)
        y.left = z.left
        y.left.parent = y

def zad1():
    tree_1 = tree.Node(d=tree.Data(5, str(5)))
    add_left(tree_1, tree.Data(4, str(4)))
    add_right(tree_1, tree.Data(6, str(6)))
    print("Head")
    print_node(tree_1)
    print("Left child")
    print_node(tree_1.left)
    print("Right child")
    print_node(tree_1.right)

def zad2():
    tree_1 = tree.Node(d=tree.Data(5, str(5)))
    add_left(tree_1, tree.Data(4, str(4)))
    add_right(tree_1, tree.Data(6, str(6)))
    inorder_tree_walk(tree_1)

def zad3():
    tree_1 = tree.Node(d=tree.Data(4, str(4)))
    add_left(tree_1, tree.Data(3, str(3)))
    add_right(tree_1, tree.Data(6, str(6)))
    print_node(search_tree(tree_1, 6))
    print_node(search_tree(tree_1, 7))
    print_node(iterative_tree_search(copy.deepcopy(tree_1), 6))
    print_node(iterative_tree_search(copy.deepcopy(tree_1), 7))

def zad4():
    tree_1 = tree.Node(d=tree.Data(4, str(4)))
    add_left(tree_1, tree.Data(3, str(3)))
    add_right(tree_1, tree.Data(6, str(6)))
    print_node(tree_minimum(tree_1))
    print_node(tree_maximum(tree_1))
    print_node(tree_successor(tree_1))

def zad5():
    tree_1 = tree.Node(d=tree.Data(4, str(4)))
    add_left(tree_1, tree.Data(3, str(3)))
    add_right(tree_1, tree.Data(6, str(6)))
    print("Pre ubacivanja elementa")
    inorder_tree_walk(tree_1)
    
    tree_insert(tree_1, tree.Data(7, str(7)))
    print("Nakon ubacivanja elementa")
    inorder_tree_walk(tree_1)

    n1 = iterative_tree_search(tree_1, 7)
    tree_delete(tree_1, n1)
    print("Nakon brisanja elementa")
    inorder_tree_walk(tree_1)

def zad6(min, max, size):
    array = [randint(min, max) for i in range(size)] # lista duzine size koja sadrzi elemente u opsegu [min,max]
    array_copy = array[:]
    sort_arr = []
    print(array)
    t = tree.Node(d=tree.Data(array[0], str(array[0])))
    for i in range(1,size):
        tree_insert(t, tree.Data(array[i], str(array[i])))
    #inorder_tree_walk(t)
    inorder_tree_walk(t, l=True, sort_list=sort_arr)
    print(sort_arr)
    array_copy.sort()
    print(array_copy)
    
if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6(1, 200, 5)