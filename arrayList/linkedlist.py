class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(head):
  current = head
  while current.link != None:
    print(current.data, end="")
    print(" -> ", end="")
    current = current.link
  print(current.data)

def countNode(head):
   count = 0
   current = head
   while current != None:
      count += 1
      current = current.link
   return count

def insertNode(position, value):
   n = Node()
   n.data = value
   current = n0
   for _ in range(position-1):
      current = current.link
   n.link = current.link
   current.link = n

def deleteNode(position, head):
   current = head
   if not(position > countNode(head) and position < 0):
      for _ in range(position - 1):
         current = current.link
      current.link = current.link.link

def reverseNode(head):
   if head is None or head.link is None:
      return head
   prev = None
   current = head
   while current is not None:
      next_node = current.link
      current.link = prev
      prev = current
      current = next_node
   return prev

def maxNode():
   max = int(0)
   current = head
   while current.link != None:
      if (current.data > max): max = current.data
      current = current.link
   if (current.data > max): max = current.data
   print("max: ", end="")
   print(max)

def minNode():
   min = float('inf')
   current = head
   while current.link != None:
      if (current.data < min): min = current.data
      current = current.link
   if (current.data < min): min = current.data
   print("min: ", end="")
   print(min)


n0 = Node()
n0.data = 1
n1 = Node() 
n1.data = 2
n2 = Node()
n2.data = 3
n3 = Node()
n3.data = 4

n0.link = n1
n1.link = n2
n2.link = n3

head = n0

printNode(head)
# 기본 1->2->3->4 순서 출력
print(countNode(head))
#노드의 개수 출력 ex) 4
insertNode(3, "강병수")
printNode(head)
#3번에 "강병수" 추가 후 출력 1->2->3->강병수->4
deleteNode(3, head)
printNode(head)
#3번 강병수 삭제 후 출력 1->2->3->4
head = reverseNode(head)
printNode(head)
#거꾸로 출력
maxNode()
minNode()
#최대, 최소 출력