FULL = 5
class Stack():
    def __init__(self, n):
        self.data = n
        self.link = None

def printStack(top):
    current = top
    while current.link != None:
        print(current.data)
        current = current.link
    print(current.data)
    print("=====")

def isStackFull():
    global FULL, top
    count = 1
    current = top
    while current.link!= None:
        current = current.link
        count += 1
    if FULL == count: return True
    else: return False

def isStackEmpty():
    global FULL, top
    current = top
    if current == None: return True
    else: return False

def push(item):
    global FULL, top
    if isStackFull():
        print("Stack is full")
        return
    new_node = Stack(item)
    new_node.link = top
    top = new_node

def pop():
    global FULL, top
    if isStackEmpty():
        print("Stack is empty")
        return None
    current = top
    top = top.link
    popped_item = current.data
    current.data = None
    current.link = None
    return popped_item

n0 = Stack(10)
n1 = Stack(30)
n2 = Stack(50)
n3 = Stack(40)
n4 = Stack(20)

n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4
top = n0

print("pop 요소: ",end="")
print(pop())
push(8765432)
printStack(top)
