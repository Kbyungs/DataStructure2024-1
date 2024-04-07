class Node():
    def __init__(self, n):
        self.data = n
        self.left = None
        self.right = None

def printRightNode(head):
    current = head
    while current.right != None:
        print(current.data, end="")
        print(" -> ", end="")
        current = current.right
    print(current.data)

def printLeftNode(head):
    current = head
    while current.left != None:
        print(current.data, end="")
        print(" -> ", end="")
        current = current.left
    print(current.data)

def countNode(head):
   count = 0
   current = head
   while current != None:
      count += 1
      current = current.right
   return count

def insertNode(position, value, head):
    n = Node(value)
    current = head
    for i in range(position-1):
        if current is not None:
            current = current.right
    n.left = current
    if current.right is not None:
        current.right.left = n
        n.right = current.right
    current.right = n

def deleteNode(position, head):
    current = head
    if not(position > countNode(head) and position < 0):
        for _ in range(position):
            current = current.right
        current.right.left = current.left
        current.left.right = current.right

def searchNode(value, head):
    count = 0
    current = head
    while current.right != None:
        if current.data == value:  return count
        current = current.right
        count += 1
    return count

def reverseNode(head, tail):
    if head is None or head.right is None:
        return head, tail

    current = head
    new_tail = head
    while current is not None:
        temp = current.right
        current.right = current.left
        current.left = temp
        new_tail = current
        current = current.left

    new_head = tail
    tail = head
    head = new_head
    return head, tail

def swapNode(p1, p2, head):
    #값만 바꿔버려도 모르는거 아닌가?
    c1 = head
    c2 = head
    for _ in range(p1):
        c1 = c1.right
    for _ in range(p2):
        c2 = c2.right
    temp = c1.data
    c1.data = c2.data
    c2.data = temp

n0 = Node("민지")
n1 = Node("하니")
n2 = Node("다니엘")
n3 = Node("해린")
n4 = Node("혜인")

n0.right = n1
n1.right = n2
n2.right = n3
n3.right = n4

n4.left = n3
n3.left = n2
n2.left = n1
n1.left = n0
head = n0
tail = n4

#오른쪽으로 출력, 왼쪽으로 출력
printRightNode(head)
printLeftNode(tail)
# 3번에 강병수 추가 후 출력
insertNode(3, "강병수", head)
printRightNode(head)
# 3번에 있던 강병수 삭제 후 출력
deleteNode(3, head)
printRightNode(head)
#하니가 몇번째에 있는지
print(searchNode("하니", head))
#reverse
head, tail = reverseNode(head, tail)
printRightNode(head)
#swap
swapNode(1, 3, head)
printRightNode(head)