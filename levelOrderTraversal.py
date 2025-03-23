from collections import deque
class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def levelOrderTraversal(root):
  ans = []
  queue = deque()
  queue.append(root)
  while len(queue) > 0:
    temp = []
    size = len(queue)
    for i in range(size):
      node = queue.popleft()
      temp.append(node.data)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    ans.append(temp)
  return ans

if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  print(levelOrderTraversal(n1))

'''
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.
'''