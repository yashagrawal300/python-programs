class Node:
  def __init__(self, left, right, val):
    self.val = val
    self.right = right
    self.left = left

def trav(root):
  if not root:
    return
  trav(root.left)
  trav(root.right)
  print(root.val)
trav(root)
