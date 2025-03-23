class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def checkForBalancedBinaryTree(root):
  if not root:
    return 0
  
  lh = checkForBalancedBinaryTree(root.left)
  if lh == -1:
    return -1
  rh = checkForBalancedBinaryTree(root.right)
  if rh == -1:
    return -1
  if abs(lh-rh) > 1: return -1
  return max(lh, rh) + 1

if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7,n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  n7.right = n8
  if checkForBalancedBinaryTree(n1) == -1:
    print(False)
  else:
    print(True)