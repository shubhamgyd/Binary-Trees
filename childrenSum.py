
# Node Class:
class Node:
  def __init__(self,val):
    self.data = val
    self.left = None
    self.right = None


class Solution:
  #Function to check whether all nodes of a tree have the value 
  #equal to the sum of their child nodes.
  def preOrderTraversal(self, root):
    if root:
      print(root.data, end=" ")
      self.preOrderTraversal(root.left)
      self.preOrderTraversal(root.right)
  
  def helper(self, root):
    if not root:
      return 0
    s = 0
    if root.left:
      s += root.left.data
    if root.right:
      s += root.right.data
    if root.data > s:
      d = root.data - s
      t = d//2
      if not root.left and root.right:
        root.right.data += d
      if not root.right and root.left:
        root.left.data += d
      if root.right and root.left:
        root.left.data += t
        root.right.data += d-t
    l = self.helper(root.left)
    r = self.helper(root.right)
    if root.data < l + r:
      root.data = l + r
    return root.data
  def isSumProperty(self, root):
    # code here
    self.helper(root)
    self.preOrderTraversal(root)

if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  c1 = Solution()
  c1.preOrderTraversal(n1)
  print()
  c1.isSumProperty(n1)