class Node:
  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def preOrder_inOrder_postOrder(root):
  st = [(root, 1)]
  preOrder = []
  inOrder = []
  postOrder = []
  while len(st):
    it = st.pop()
    if it[1] == 1:
      preOrder.append(it[0].data)
      st.append((it[0], it[1]+1))
      if it[0].left:
        st.append((it[0].left, 1))
    elif it[1] == 2:
      inOrder.append(it[0].data)
      st.append((it[0], it[1]+1))
      if it[0].right:
        st.append((it[0].right, 1))
    else:
      postOrder.append(it[0].data)
  print("PreOrder", preOrder)
  print("InOrder", inOrder)
  print("PostOrder", postOrder)

if __name__=="__main__":
  n1,n2,n3,n4,n5,n6,n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7
  preOrder_inOrder_postOrder(n1)