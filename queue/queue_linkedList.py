class Queue():
  def __init__(self, n):
    self.data = n
    self.link = None

def printQueue(front):
  current = front
  while current.link != None:
    print(current.data, end="")
    print(" -> ", end="")
    current = current.link
  print(current.data)

def enqueue(rear, item):
  new_q = Queue(item)
  rear.link = new_q
  rear = new_q

def dequeue(front):
  temp = front.link
  front.data = None
  front.link = None
  return temp

def isEmpty(front):
  if front is None: return True
  else: return False


n0 = Queue("민지")
n1 = Queue("하니")
n2 = Queue("다니엘")
n3 = Queue("해린")
n4 = Queue("혜인")

n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4
front = n0
rear = n4

printQueue(front)
#맨 뒤에 "병수" 추가
enqueue(rear, "병수")
printQueue(front)
#민지 탈퇴ㅠㅠ
front = dequeue(front) 
printQueue(front)
#is empty?
print(isEmpty(front))
