from collections import deque
class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def constructBinaryTree(inStart, inEnd, preStart, preEnd, inOrder, preOrder, d):
  if inStart > inEnd or preStart > preEnd:
    return None
  root = Node(preOrder[preStart])
  inRoot = d[root.data]
  root.left = constructBinaryTree(inStart, inRoot-1, preStart+1, preStart+inRoot-inStart, inOrder, preOrder, d)
  root.right = constructBinaryTree(inRoot+1, inEnd, preStart+inRoot-inStart+1, preEnd, inOrder, preOrder, d)
  return root
def inOrderTraversal(root):
  if root:
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

if __name__=="__main__":
  inOrder = [40, 20, 50, 10, 60, 30, 70]
  preOrder = [10, 20, 40, 50, 30, 60, 70]
  d = {}
  for i in range(len(inOrder)):
    d[inOrder[i]] = i
  N = len(inOrder)
  root  = constructBinaryTree(0, N-1, 0, N-1, inOrder, preOrder, d)
  inOrderTraversal(root)
  