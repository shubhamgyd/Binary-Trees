from collections import deque
class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def iterativeInOrderTraversal(root):
  st = []
  node = root
  ans = []
  while True:
    if node != None:
      st.append(node)
      node = node.left
    else:
      if len(st) == 0:
        break
      node = st[-1]
      st.pop()
      ans.append(node.data)
      node = node.right
  
  return ans


if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  print(iterativeInOrderTraversal(n1))