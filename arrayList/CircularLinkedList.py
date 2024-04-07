class Node():
    def __init__(self):
        self.data = None
        self.link = None

n0 = Node()
n0.data = "민지"
n1 = Node()
n1.data = "하니"
n2 = Node()
n2.data = "다니엘"
n3 = Node()
n3.data = "해린"
n4 = Node()
n4.data = "혜인"

n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4
n4.link = n0
head = n0