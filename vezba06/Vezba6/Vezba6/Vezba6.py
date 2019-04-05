class HuffmanNode():
    """
    Class represents one node in the huffman tree.
    """
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

class HistogramElement():
    """
    Class that encapsulates histogram element's value and frequency.
    """
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

def GetHistogram(symbols):
    """
    Returns dictionary that represents histogram based on list symbols.
    """
    hist = {}
    for sym in symbols:
        if sym not in hist.keys():
            hist[sym] = 1
        else:
            hist[sym] += 1    
    return hist     

def zad1():
    """
    Test GetHistogram function with input lists and print result.
    """
    input1 = ['a', 'b']
    print(input1)
    print(GetHistogram(input1))

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    print(input2)
    print(GetHistogram(input2))

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    print(input3)
    print(GetHistogram(input3))

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    print(input4)
    print(GetHistogram(input4))

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    print(input5)
    print(GetHistogram(input5))

def print_histogram_elements(h_elements):
    for element in h_elements:
        print("value: ", element.value)
        print("freq: ", element.freq)
        print("***")

def extraxt_freq(h_elem):
    return h_elem.freq

def make_histogram_list(l):
    hist = GetHistogram(l)    
    h_elements = []
    for k,v in hist.items():
        h_elements.append(HistogramElement(k, v));    
    h_elements.sort(key=extraxt_freq, reverse=True)
    return h_elements

def zad2():
    l1 = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'd', 'g', 'e', 'g', 'g']
    h_elements = make_histogram_list(l1)
    print_histogram_elements(h_elements)
    huffman_tree = form_huffman_tree(h_elements)
    print_huffman_tree(huffman_tree)

def form_huffman_tree(h_elements):
    """
    Create Huffman tree based on histogram elements sorted in descending order.
    Function assumes that h_elements is list of sorted HuffmanElement types in descending order.
    """
    root = HuffmanNode(None, None)
    recursive_build(root, h_elements)
    return root

def recursive_build(root, h_elements):
    if len(h_elements) == 1:
        root.right = HuffmanNode(h_elements[0].value, h_elements[0].freq)
    if len(h_elements) == 2:
        root.left = HuffmanNode(h_elements[0].value, h_elements[0].freq)
        root.right = HuffmanNode(h_elements[1].value, h_elements[1].freq)
    else:
        root.right = HuffmanNode(h_elements[0].value, h_elements[0].freq)
        root.left = HuffmanNode(None, None)
        recursive_build(root.left, h_elements[1:])
        
def print_huffman_tree(h_tree):
    if h_tree.value != None:
        print("Value: ", h_tree.value)
        print("Frequency: ", h_tree.freq)
        print("***")
    else:
        print_huffman_tree(h_tree.right)
        print_huffman_tree(h_tree.left)

def GetEncValue(root, symbol):
    code = ""
    while root != None:
        if root.right != None and root.right.value == symbol:
            code += "1"
            break
        elif root.left != None:
            code += "0"
            if root.left.value == symbol:
                break
        root = root.left
    return code         

def zad3():
    l1 = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'd', 'g', 'e', 'g', 'g']
    h_elements = make_histogram_list(l1)
    huffman_tree = form_huffman_tree(h_elements)
    print_huffman_tree(huffman_tree)
    for element in h_elements:
        print("Code for " + str(element.value) + " : " + GetEncValue(huffman_tree, element.value))
    
if __name__ == '__main__':
    #zad1()
    #zad2()
    zad3()
