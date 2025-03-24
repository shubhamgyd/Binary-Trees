from collections import deque
class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def verticalOrderTraversal(root):
  ans = []
  q = deque()
  q.append((root, 0, 0))
  while q:
    size = len(q)
    for i in range(size):
      node, index, level = q.popleft()
      ans.append((index, level, node.data))
      if node.left:
        q.append((node.left, index-1, level+1))
      if node.right:
        q.append((node.right, index+1, level+1))
  ans.sort()
  temp = [it[2] for it in ans]
  return temp

if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  print(verticalOrderTraversal(n1))